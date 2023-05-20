Title: CentOS 7 Nvidia Driver Updater 

Description: This repository contains a Python script for updating Nvidia drivers on CentOS 7 with support for the ELRepo repository. The script checks if the ELRepo repository is installed and installs it if necessary. It then installs the latest Nvidia drivers and creates a blacklist file to prevent the loading of the nouveau drivers. The script provides a convenient way to ensure up-to-date Nvidia drivers and a smooth GPU experience on CentOS 7 systems.

Key Features:
- Automatic installation of ELRepo repository for CentOS 7
- Update and installation of the latest Nvidia drivers
- Creation of a nouveau blacklist file to avoid driver conflicts
- Simplified script execution and system reboot

Usage:
1. Clone or download the repository.
2. Make the script executable: `chmod +x update_nvidia.py`.
3. Run the script as root: `./update_nvidia.py`. added Ubuntu Verison -ubuntuinstall.py

Note: This script assumes CentOS 7 as the target operating system and requires root access for installing packages and rebooting the system.

Contributions, bug reports, and feature requests are welcome!
Paypal: Entri3@aol.com
