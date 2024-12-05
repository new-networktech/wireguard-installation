import os
import subprocess
from colorama import Fore, Style

def remove_wireguard_container():
    """Stop and remove the WireGuard container."""
    print(f"{Fore.YELLOW}Stopping and removing WireGuard container...{Style.RESET_ALL}")
    subprocess.run(["sudo", "docker-compose", "-f", "/opt/wireguard/docker-compose.yml", "down"])
    print(f"{Fore.GREEN}WireGuard container removed.{Style.RESET_ALL}")

def remove_wireguard_files():
    """Remove WireGuard configuration files."""
    print(f"{Fore.YELLOW}Removing WireGuard configuration files...{Style.RESET_ALL}")
    subprocess.run(["sudo", "rm", "-rf", "/opt/wireguard"])
    print(f"{Fore.GREEN}Configuration files removed.{Style.RESET_ALL}")

def main():
    print(f"{Fore.BLUE}Starting WireGuard uninstallation process...{Style.RESET_ALL}")
    remove_wireguard_container()
    remove_wireguard_files()
    print(f"{Fore.GREEN}Uninstallation complete.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
