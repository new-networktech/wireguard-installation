import os
import subprocess
from colorama import Fore, Style

def install_prerequisites():
    """Install required packages like Docker and Docker Compose."""
    print(f"{Fore.YELLOW}Installing prerequisites...{Style.RESET_ALL}")
    subprocess.run(["sudo", "apt", "update", "-y"])
    subprocess.run(["sudo", "apt", "install", "-y", "git", "docker.io", "docker-compose"])
    print(f"{Fore.GREEN}Prerequisites installed successfully!{Style.RESET_ALL}")

def setup_wireguard():
    """Set up WireGuard using Docker."""
    print(f"{Fore.YELLOW}Setting up WireGuard as a Docker container...{Style.RESET_ALL}")
    
    # Create WireGuard configuration folder
    os.makedirs("/opt/wireguard", exist_ok=True)
    
    # Docker Compose configuration
    docker_compose_content = """
version: "2.1"
services:
  wireguard:
    image: lscr.io/linuxserver/wireguard:latest
    container_name: wireguard
    cap_add:
      - NET_ADMIN
      - SYS_MODULE
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Berlin
      - SERVERURL=auto  # Replace with your domain or public IP
      - SERVERPORT=51820
      - PEERS=5  # Number of peers to generate
      - PEERDNS=auto
      - INTERNAL_SUBNET=10.13.13.0
    volumes:
      - /opt/wireguard:/config
    ports:
      - 51820:51820/udp
    sysctls:
      - net.ipv4.conf.all.src_valid_mark=1
    restart: unless-stopped
    """
    
    # Write Docker Compose configuration
    with open("/opt/wireguard/docker-compose.yml", "w") as f:
        f.write(docker_compose_content)
    
    # Deploy the container
    subprocess.run(["sudo", "docker-compose", "-f", "/opt/wireguard/docker-compose.yml", "up", "-d"])
    print(f"{Fore.GREEN}WireGuard container set up successfully!{Style.RESET_ALL}")

def display_instructions():
    """Display client configuration instructions."""
    print(f"{Fore.CYAN}To add clients, check the /opt/wireguard/ directory for configuration files.{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Use these files to configure WireGuard clients on your devices.{Style.RESET_ALL}")

def main():
    print(f"{Fore.BLUE}Welcome to the WireGuard VPN Automation Setup!{Style.RESET_ALL}")
    install_prerequisites()
    setup_wireguard()
    display_instructions()

if __name__ == "__main__":
    main()
