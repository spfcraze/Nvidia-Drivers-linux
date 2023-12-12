#!/bin/bash

# Check if the ELRepo repository is already installed
if ! rpm -qa | grep -q elrepo-release; then
  # Install the ELRepo repository if it's not already installed
  yum install -y https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm
fi

# Check if the Nvidia drivers are already installed
if ! rpm -qa | grep -q kmod-nvidia; then
  # Install the Nvidia drivers if they're not already installed
  yum install -y kmod-nvidia nvidia-x11-drv
fi

# Check if the nouveau blacklist file already exists
if [ ! -f /etc/modprobe.d/blacklist-nouveau.conf ]; then
  # Create a new file to blacklist the nouveau drivers if it doesn't exist
  echo "blacklist nouveau" > /etc/modprobe.d/blacklist-nouveau.conf
  echo "options nouveau modeset=0" >> /etc/modprobe.d/blacklist-nouveau.conf
fi

# Reboot the system to load the new drivers and the blacklist
reboot
