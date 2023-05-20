#!/usr/bin/env python3

import os
import subprocess
import shutil

# Check if the ELRepo repository is already installed
elrepo_installed = subprocess.call("rpm -qa | grep -q elrepo-release", shell=True) == 0

if not elrepo_installed:
    # Install the ELRepo repository if it's not already installed
    subprocess.call("yum install -y https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm", shell=True)

# Check if the Nvidia drivers are already installed
nvidia_installed = subprocess.call("rpm -qa | grep -q kmod-nvidia", shell=True) == 0

if not nvidia_installed:
    # Install the Nvidia drivers if they're not already installed
    subprocess.call("yum install -y kmod-nvidia nvidia-x11-drv", shell=True)

# Check if the nouveau blacklist file already exists
blacklist_file = "/etc/modprobe.d/blacklist-nouveau.conf"
if not os.path.exists(blacklist_file):
    # Create a new file to blacklist the nouveau drivers if it doesn't exist
    with open(blacklist_file, "w") as file:
        file.write("blacklist nouveau\n")
        file.write("options nouveau modeset=0\n")

# Reboot the system to load the new drivers and the blacklist
subprocess.call("reboot", shell=True)
