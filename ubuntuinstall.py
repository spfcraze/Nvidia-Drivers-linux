#!/usr/bin/env python3

import os
import subprocess

# Check if the Nvidia drivers are already installed
nvidia_installed = subprocess.call("dpkg -l | grep -q nvidia-driver", shell=True) == 0

if not nvidia_installed:
    # Add the graphics drivers PPA
    subprocess.call("add-apt-repository -y ppa:graphics-drivers/ppa", shell=True)
    subprocess.call("apt-get update", shell=True)

    # Install the Nvidia drivers
    subprocess.call("apt-get install -y nvidia-driver", shell=True)

# Create a new file to blacklist the nouveau drivers
blacklist_file = "/etc/modprobe.d/blacklist-nouveau.conf"
if not os.path.exists(blacklist_file):
    # Create a new file to blacklist the nouveau drivers if it doesn't exist
    with open(blacklist_file, "w") as file:
        file.write("blacklist nouveau\n")
        file.write("options nouveau modeset=0\n")

# Reboot the system to load the new drivers and the blacklist
subprocess.call("reboot", shell=True)
