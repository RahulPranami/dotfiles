#!/bin/bash

# Check if yay is installed for AUR packages
if [ -f aur_packages.txt ] && ! command -v yay &> /dev/null; then
    echo "yay is not installed. Please install yay to proceed with AUR packages."
    exit 1
fi

# Install Pacman packages
sudo pacman -S --needed - < pacman_packages.txt

# Install AUR packages with yay (if aur_packages.txt exists)
if [ -f aur_packages.txt ]; then
    yay -S --needed - < aur_packages.txt
fi

# Stow dotfiles
cd ~/dotfiles
for dir in */; do
    stow "${dir%/}"
done