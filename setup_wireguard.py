import os
import subprocess
import json

def install_prerequisites():
    """Install necessary tools and dependencies."""
    print("Installing prerequisites...")
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "install", "-y", "wireguard", "ansible", "python3", "python3-pip", "git"])
    print("Prerequisites installed successfully.")

def get_user_input():
    """Get user input for WireGuard setup."""
    print("Please provide the following details for WireGuard setup:")
    telegram_bot_token = input("Enter your Telegram bot token (leave blank to skip notification): ").strip()
    telegram_chat_id = input("Enter your Telegram chat ID (leave blank to skip notification): ").strip()
    wg_server_ip = input("Enter your server's public IP address: ").strip()
    wg_server_port = input("Enter the WireGuard server port (default: 51820): ").strip() or "51820"
    return {
        "telegram_bot_token": telegram_bot_token,
        "telegram_chat_id": telegram_chat_id,
        "wg_server_ip": wg_server_ip,
        "wg_server_port": wg_server_port
    }

def create_wireguard_config(config):
    """Create WireGuard server and client configurations."""
    print("Creating WireGuard configuration...")
    os.makedirs("/etc/wireguard", exist_ok=True)

    # Generate server keys
    server_private_key = subprocess.run(["wg", "genkey"], capture_output=True, text=True).stdout.strip()
    server_public_key = subprocess.run(
        ["echo", server_private_key], capture_output=True, text=True
    ).stdout.strip()

    # Generate client keys
    client_private_key = subprocess.run(["wg", "genkey"], capture_output=True, text=True).stdout.strip()
    client_public_key = subprocess.run(
        ["echo", client_private_key], capture_output=True, text=True
    ).stdout.strip()

    # Write server configuration file
    wg_config = f"""
[Interface]
PrivateKey = {server_private_key}
Address = 10.0.0.1/24
ListenPort = {config['wg_server_port']}
SaveConfig = true

[Peer]
PublicKey = {client_public_key}
AllowedIPs = 10.0.0.2/32
    """

    with open("/etc/wireguard/wg0.conf", "w") as f:
        f.write(wg_config)

    # Write client configuration file
    client_config = f"""
[Interface]
PrivateKey = {client_private_key}
Address = 10.0.0.2/24
DNS = 8.8.8.8

[Peer]
PublicKey = {server_public_key}
Endpoint = {config['wg_server_ip']}:{config['wg_server_port']}
AllowedIPs = 0.0.0.0/0, ::/0
    """

    with open("/etc/wireguard/client.conf", "w") as f:
        f.write(client_config)

    subprocess.run(["sudo", "chmod", "600", "/etc/wireguard/wg0.conf"])
    print("WireGuard configuration created.")

    return server_public_key

def start_wireguard():
    """Enable and start WireGuard service."""
    print("Starting WireGuard...")
    subprocess.run(["sudo", "wg-quick", "up", "wg0"])
    subprocess.run(["sudo", "systemctl", "enable", "wg-quick@wg0"])
    print("WireGuard started and enabled on boot.")

def send_telegram_notification(config, server_public_key):
    """Send a Telegram notification about the setup."""
    if not config["telegram_bot_token"] or not config["telegram_chat_id"]:
        print("Telegram notification skipped.")
        return

    print("Sending Telegram notification...")
    message = f"WireGuard VPN setup complete.\nServer Public Key: {server_public_key}\nServer IP: {config['wg_server_ip']}"
    url = f"https://api.telegram.org/bot{config['telegram_bot_token']}/sendMessage"
    payload = {
        "chat_id": config["telegram_chat_id"],
        "text": message
    }
    response = subprocess.run(
        ["curl", "-s", "-X", "POST", url, "-H", "Content-Type: application/json", "-d", json.dumps(payload)],
        capture_output=True
    )
    if response.returncode == 0:
        print("Telegram notification sent.")
    else:
        print("Failed to send Telegram notification.")

def main():
    """Main function for WireGuard setup."""
    print("Welcome to the WireGuard VPN One-Click Installer!")
    install_prerequisites()
    config = get_user_input()
    server_public_key = create_wireguard_config(config)
    start_wireguard()
    send_telegram_notification(config, server_public_key)
    print("WireGuard setup complete!")

if __name__ == "__main__":
    main()
