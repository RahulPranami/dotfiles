# Comprehensive Guide to Creating a Dotfiles Management System for Arch Linux with Hyprland

## Introduction

Dotfiles are configuration files (e.g., `.bashrc`, `.config/hypr/hyprland.conf`) that customize your Linux environment. For Arch Linux users with Hyprland, managing dotfiles is crucial for replicating a personalized setup across systems or after a reinstall. This guide provides a detailed walkthrough to create a dotfiles management system using Git and GNU Stow, hosted on GitHub, with scripts to automate package installation and configuration setup. It’s designed to work on a bare minimal Arch Linux installation, ensuring all required packages and Hyprland configurations are restored.

## Why Use Git and GNU Stow?

- **Git**: Provides version control and cloud storage on GitHub, making your dotfiles accessible and trackable.
- **GNU Stow**: A symlink manager that organizes dotfiles in a repository and creates symlinks to their correct locations, simplifying setup and updates.
- **Simplicity**: Compared to tools like Ansible, Git and Stow are lightweight and easier for users familiar with Arch Linux and Hyprland.

## Prerequisites

- A working Arch Linux installation with Hyprland.
- Basic familiarity with terminal commands, Git, and Hyprland configuration.
- Internet access to install packages and push to GitHub.
- A GitHub account.

## Step-by-Step Walkthrough

### Step 1: Install Necessary Tools

Install Git for version control and GNU Stow for symlink management:

```bash
sudo pacman -S git stow
```

If your setup includes AUR packages (e.g., Hyprland or related tools), install an AUR helper like `yay`. Follow the Arch Wiki AUR helpers guide to install `yay` by cloning its repository and building it:

```bash
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

### Step 2: Create Dotfiles Directory

Create a directory to store your dotfiles:

```bash
mkdir ~/dotfiles
```

This directory will hold all your configuration files and scripts, organized in a structure compatible with Stow.

### Step 3: Organize Your Dotfiles

Copy your configuration files into `~/dotfiles`, maintaining a directory structure that mirrors your home directory. This ensures Stow can create symlinks correctly.

#### For Files in Home Directory

For dotfiles like `.bashrc` or `.zshrc`:

```bash
mkdir ~/dotfiles/bash
cp ~/.bashrc ~/dotfiles/bash/.bashrc
```

If you use Zsh, common with Hyprland:

```bash
mkdir ~/dotfiles/zsh
cp ~/.zshrc ~/dotfiles/zsh/.zshrc
```

#### For Hyprland Configurations

Hyprland stores its configuration in `~/.config/hypr/`. Copy the entire directory:

```bash
mkdir -p ~/dotfiles/hypr/.config/hypr
cp -r ~/.config/hypr/* ~/dotfiles/hypr/.config/hypr/
```

#### For Other Configurations

For other applications with configurations in `~/.config/`, such as `alacritty` or `waybar` (common in Hyprland setups):

```bash
mkdir -p ~/dotfiles/alacritty/.config/alacritty
cp -r ~/.config/alacritty/* ~/dotfiles/alacritty/.config/alacritty/
mkdir -p ~/dotfiles/waybar/.config/waybar
cp -r ~/.config/waybar/* ~/dotfiles/waybar/.config/waybar/
```

Repeat for all dotfiles you wish to manage. Be cautious to copy files rather than move them to avoid breaking your current setup until symlinks are created.

### Step 4: Generate Package Lists

To ensure your packages are reinstalled, create lists of explicitly installed packages:

- **Official Repository Packages**:

  ```bash
  pacman -Qqe | grep -v "$(pacman -Qqm)" > ~/dotfiles/pacman_packages.txt
  ```

  This lists packages installed explicitly from Arch’s official repositories, excluding AUR packages.
- **AUR Packages**:

  ```bash
  pacman -Qqm > ~/dotfiles/aur_packages.txt
  ```

  This lists foreign packages, typically from the AUR.

These lists will be used by your setup script to reinstall packages. You may review `pacman_packages.txt` and `aur_packages.txt` to exclude unnecessary packages, but including all explicitly installed packages is generally safe.

### Step 5: Set Up Git Repository

Initialize a Git repository in `~/dotfiles`, commit your files, and push them to GitHub:

```bash
cd ~/dotfiles
git init
git add .
git commit -m "Initial commit of dotfiles"
```

Create a new repository on GitHub and add it as a remote:

```bash
git remote add origin https://github.com/yourusername/dotfiles.git
git push -u origin master
```

Replace `yourusername` with your GitHub username. This stores your dotfiles on GitHub for easy access.

### Step 6: Create Setup Script

Create a script named `install.sh` in `~/dotfiles` to automate package installation and dotfile setup:

```bash
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
```

Make the script executable:

```bash
chmod +x ~/dotfiles/install.sh
```

This script:

- Checks for `yay` if AUR packages are present.
- Installs packages from `pacman_packages.txt` using `pacman`.
- Installs AUR packages from `aur_packages.txt` using `yay` if applicable.
- Uses Stow to create symlinks for all dotfiles, including Hyprland configurations.

### Step 7: Test Your Setup

Before relying on your dotfiles, test the setup on your current system:

1. Back up critical dotfiles (e.g., `~/.bashrc`, `~/.config/hypr/`).

2. Remove a test dotfile (e.g., `rm ~/.bashrc`) and run:

   ```bash
   cd ~/dotfiles
   stow bash
   ```

   Verify that `~/.bashrc` is restored as a symlink to `~/dotfiles/bash/.bashrc`.

3. Check that your package lists include essential Hyprland packages (e.g., `hyprland`, `waybar`).

### Step 8: Restore on a New System

On a fresh Arch Linux installation:

1. Complete the base installation as per the Arch Linux Installation Guide.

2. Install Git and Stow:

   ```bash
   sudo pacman -S git stow
   ```

3. If `aur_packages.txt` exists, install `yay` (see Step 1).

4. Clone your dotfiles repository:

   ```bash
   git clone https://github.com/yourusername/dotfiles.git ~/dotfiles
   ```

5. Run the setup script:

   ```bash
   ~/dotfiles/install.sh
   ```

This will install all packages and set up your dotfiles, restoring your Hyprland environment.

### Step 9: Updating Dotfiles

To update your dotfiles with new configurations or packages:

1. Update your local `~/dotfiles` directory with new or modified files.

2. Regenerate package lists if needed:

   ```bash
   pacman -Qqe | grep -v "$(pacman -Qqm)" > ~/dotfiles/pacman_packages.txt
   pacman -Qqm > ~/dotfiles/aur_packages.txt
   ```

3. Commit and push changes:

   ```bash
   cd ~/dotfiles
   git add .
   git commit -m "Updated dotfiles"
   git push
   ```

4. On other systems, pull and restow:

   ```bash
   cd ~/dotfiles
   git pull
   for dir in */; do
       stow -R "${dir%/}"
   done
   ```

The `-R` option ensures Stow updates symlinks to reflect changes.

## Example Repository Structure

Here’s how your `~/dotfiles` directory might look:

```
~/dotfiles/
├── bash/
│   └── .bashrc
├── zsh/
│   └── .zshrc
├── hypr/
│   └── .config/hypr/hyprland.conf
├── waybar/
│   └── .config/waybar/config
├── alacritty/
│   └── .config/alacritty/alacritty.yml
├── pacman_packages.txt
├── aur_packages.txt
└── install.sh
```

| File/Directory | Purpose |
| --- | --- |
| `bash/.bashrc` | Shell configuration for Bash |
| `zsh/.zshrc` | Shell configuration for Zsh |
| `hypr/.config/hypr/` | Hyprland window manager configuration |
| `waybar/.config/waybar/` | Waybar configuration for status bar |
| `alacritty/.config/alacritty/` | Alacritty terminal configuration |
| `pacman_packages.txt` | List of official repository packages |
| `aur_packages.txt` | List of AUR packages |
| `install.sh` | Script to automate setup |

## Tips and Best Practices

- **Backup Before Moving Files**: Always back up dotfiles before reorganizing to prevent accidental loss.
- **Curate Package Lists**: Review `pacman_packages.txt` and `aur_packages.txt` to exclude unnecessary packages.
- **Test Incrementally**: Test Stow commands on individual directories before running the full script.
- **Secure Sensitive Data**: Avoid including sensitive information (e.g., API keys) in public GitHub repositories.
- **Document Your Setup**: Add a `README.md` in `~/dotfiles` to document your setup process and dependencies.
- **Explore Examples**: Check repositories like filiparag/dotfiles for inspiration on structuring dotfiles.

## Troubleshooting

- **Stow Conflicts**: If Stow reports conflicts (e.g., existing files), remove or back up the conflicting files and restow.
- **Package Installation Errors**: Ensure your system is updated (`sudo pacman -Syu`) and check package names in your lists.
- **Hyprland Issues**: Verify that `hyprland` and dependencies are in `pacman_packages.txt` or `aur_packages.txt`.
- **Git Push Errors**: Ensure your GitHub repository is set up correctly and your SSH keys are configured.

## Conclusion

This guide enables you to create a robust dotfiles management system for your Arch Linux setup with Hyprland. By using Git and GNU Stow, you can store your configurations on GitHub and automate their restoration, including all necessary packages. This approach is lightweight, aligns with Arch’s philosophy, and ensures your Hyprland environment is easily reproducible.