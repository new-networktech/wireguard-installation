---

# **WireGuard One-Click Installer**

This project automates the installation and setup of WireGuard VPN as a Docker container on your server. It provides a quick and straightforward way to deploy a secure VPN.

---

## **Features**

- Sets up WireGuard VPN using Docker.
- Automatically generates client configuration files.
- Allows customization of server settings (e.g., peers, timezone, and ports).
- Provides an uninstallation option to clean up.

---

## **Prerequisites**

1. A fresh Ubuntu 22 or later server.
2. Basic familiarity with using the command line (no technical expertise required).
3. Install **Python 3** and **Git** (explained below).
4. Ensure your server has sufficient permissions (run commands as root or with `sudo`).

---

## **How to Use**

### **1. Clone the Repository**

First, download this project to your server:

```bash
git clone https://github.com/new-networktech/wireguard-installation.git
```

Navigate into the project directory:

```bash
cd wireguard-installation
```

---

### **2. Run the Installation Command**

Install the necessary tools and dependencies by running:

```bash
sudo apt update -y && sudo apt install -y git python3 python3-pip && pip3 install colorama
```

---

### **3. Run the Script**

Run the installer script to set up WireGuard:

```bash
python3 setup_wireguard.py
```

---

### **4. Follow the Prompts**

The script will:

- Set up WireGuard VPN as a Docker container.
- Generate client configuration files in `/opt/wireguard/`.

You can use these files to configure your devices with WireGuard.

---

## **Customizing the Setup**

If you need to modify the default settings (e.g., number of peers or timezone), edit the `setup_wireguard.py` file before running it.

### **Important Parameters You Can Customize**

1. **Peers**: The number of client configurations to generate.
   - Open the `setup_wireguard.py` file.
   - Locate the `PEERS=5` line in the Docker Compose configuration section.
   - Change the number `5` to the desired number of clients. For example `3`.
2. **Timezone (TZ)**:
   - In the same section, find `- TZ=Europe/Berlin`.
   - Replace `Europe/Berlin` with your timezone (e.g., `America/New_York`).
3. **Server Port**:
   - Find the `- SERVERPORT=51820` line and update the port number if needed.
4. **Internal Subnet**:
   - Modify `- INTERNAL_SUBNET=10.13.13.0` to change the internal subnet of the VPN.

After editing, save the file and run the setup script as usual.

---

## **Access Client Configurations**

After the setup is complete, the script generates configuration files for each peer (client). These files are located in:

```bash
/opt/wireguard/
```

Each peer (client) has its own folder, named peer1, peer2, etc., depending on the number of peers you specified during setup.

To view the files for a specific peer, navigate to its folder:

```bash
cd /opt/wireguard/peer1
ls
```

You will see the following files:

- `peer1.conf`: The primary configuration file for this peer. This file can be imported directly into any WireGuard-compatible app to configure your VPN.
- `peer1.png`: A QR code that represents the `peer1.conf` configuration file. This is especially useful for mobile devices—scan the QR code to set up the VPN automatically.
- `presharedkey-peer1`: A preshared key to enhance security for this peer.
- `privatekey-peer1`: The private key for this peer. **DO NOT** share this key.
- `publickey-peer1`: The public key for this peer.

---

## **How to Configure Your Devices**

### **1. Desktop or Laptop**

- Copy the `peer1.conf` file from `/opt/wireguard/peer1` to your device.
- Open the WireGuard application on your desktop or laptop.
- Import the `peer1.conf` file into the app.
- Save the configuration and activate the VPN.

### **2. Mobile Devices**

- Open the WireGuard app on your smartphone or tablet.
- Select the "Add Tunnel" option and choose "Scan QR Code."
- Point your device's camera at the `peer1.png` QR code from the `peer1` folder.
- The VPN settings will be automatically imported into your WireGuard app.

---

## **Important Notes**

- **Security**: Protect the private keys (e.g., `privatekey-peer1`) and do not share them with anyone.
- **Additional Peers**: If you have multiple devices, each peer (peer2, peer3, etc.) will have its own folder with a similar set of files.
- **Customizing Peers**: You can specify the number of peers during setup by editing the `PEERS` parameter in the `setup_wireguard.py` script.
- **Backup**: Make a backup of the `/opt/wireguard/` directory to ensure you don’t lose important configuration files.

---

## **Uninstallation**

To remove WireGuard and all configurations, follow these steps:

1. Navigate to the project directory:

   ```bash
   cd wireguard-installation
   ```

2. Run the uninstallation script:

   ```bash
   python3 uninstall_wireguard.py
   ```

This will:

- Stop and remove the WireGuard Docker container.
- Delete WireGuard configuration files.
- Clean up the Docker image.

---

## **Troubleshooting**

If you encounter issues:

- Ensure you entered the correct server settings (e.g., IP, timezone).
- Confirm Docker and Docker Compose are installed and running.
- Check the logs of the WireGuard container:

  ```bash
  docker logs wireguard
  ```

Re-run the setup script if necessary:

```bash
python3 setup_wireguard.py
```

---

## **Contributing**

If you have suggestions or improvements, feel free to fork this repository and submit a pull request. Non-technical feedback is also welcome!

---

## **License**

This project is licensed under the MIT License.

---

## **Support**

For additional help, please contact:

- **Email**: [support@new-networktech.com](mailto:support@new-networktech.com)
- **Telegram**: [Support Group](https://t.me/new_networktech_support)

---

## **Example Screenshot**

Below is an example of how the script will look when running:

```plaintext
Welcome to the WireGuard VPN Automation Setup!
Installing prerequisites...
Prerequisites installed successfully.
WireGuard container set up successfully!
To add clients, check the /opt/wireguard/ directory for configuration files.
```

---
