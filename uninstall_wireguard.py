import os
import subprocess

def stop_wireguard():
    """Stop and disable WireGuard."""
    print("Stopping WireGuard...")
    subprocess.run(["sudo", "wg-quick", "down", "wg0"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "systemctl", "disable", "wg-quick@wg0"])
    print("WireGuard stopped and disabled.")

def remove_wireguard_files():
    """Remove WireGuard configuration files."""
    print("Removing WireGuard configuration files...")
    subprocess.run(["sudo", "rm", "-rf", "/etc/wireguard"])
    print("WireGuard configuration files removed.")

def uninstall_wireguard():
    """Uninstall WireGuard."""
    print("Uninstalling WireGuard...")
    subprocess.run(["sudo", "apt", "remove", "--purge", "-y", "wireguard"])
    subprocess.run(["sudo", "apt", "autoremove", "-y"])
    print("WireGuard uninstalled.")

def main():
    """Main function for uninstallation."""
    print("Starting WireGuard uninstallation...")
    stop_wireguard()
    remove_wireguard_files()
    uninstall_wireguard()
    print("WireGuard uninstallation complete.")

if __name__ == "__main__":
    main()
