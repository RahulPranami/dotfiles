#!/bin/bash
chosen=$(echo -e "Logout\nReboot\nShutdown" | wofi -dmenu -p "Power Menu")
case "$chosen" in
    "Logout")
        killall Hyprland
        ;;
    "Reboot")
        reboot
        ;;
    "Shutdown")
        poweroff
        ;;
esac
