#!/bin/bash

#############################################################
### Purpose: Enable/Disable Smartcard on MacOS
### Author: CadmusOfThebes@protonmail.com
#############################################################

# Check if user is root
if [[ $EUID -ne 0 ]]; then
   echo "[!] This script must be run with sudo (not as root due to bashrc updates)" 
   echo "[!] Exiting"
   exit 1
fi


# Get current smartcard setting
currentStatus=$(defaults read /Library/Preferences/com.apple.security.smartcard enforceSmartCard) 


# Check current status of smartcard authentication
if [ $currentStatus = 1 ]; then
    echo "[*] Smartcard is currently Enabled"
elif [ $currentStatus = 0 ]; then
    echo "[*] Smartcard is currently Disabled"
fi


# Give user a chance to exit
read -p "[*] Hit <enter> to change status or CTRL+C to exit"


# Change if the user chooses
if [ $currentStatus = 1 ]; then
    defaults write /Library/Preferences/com.apple.security.smartcard enforceSmartCard -bool false
    echo "[*] Smartcard is now DISABLED"

elif [ $currentStatus = 0 ]; then
    defaults write /Library/Preferences/com.apple.security.smartcard enforceSmartCard -bool true
    echo "[*] Smartcard is now ENABLED"

else
    echo "[!] Something went wrong"

fi
