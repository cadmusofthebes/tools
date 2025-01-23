#!/bin/bash

#############################################################
### Purpose: Lookup domain account details on MacOS
### Author: CadmusOfThebes@protonmail.com
#############################################################

# Validate a username was given
if [[ $# -eq 0 ]] ; then
	echo "[!] ERROR: Missing username and/or domain parameter"
	echo "[*] Usage: $0 <username> <domain>"
	exit 0
fi


# Run dscl against the given name
userName=$1
domain=$2
name=$(dscl "/Active Directory/$domain/All Domains" cat /Users/$userName name | awk 'BEGIN{ RS = "" ; FS = "\n"{print $2}')
lockoutTime=$(dscl "/Active Directory/$domain/All Domains" cat /Users/$userName lockoutTime | awk -F ":" '{printf $3}')
accountExpires=$(dscl "/Active Directory/$domain/All Domains" cat /Users/$userName accountExpires | awk -F ":" '{print $3}')
jobTitle=$(dscl "/Active Directory/$domain/All Domains" cat /Users/$userName JobTitle | awk BEGIN'{ RS = "" ; FS = "\n"}{print $2}')


# Do manipulation on passwrod values to determine dates
timeNow=$(date +"%s")
pwdLastSet=$(dscl "/Active Directory/$domain/All Domains/" cat /Users/$userName pwdLastSet | awk '{print $NF}')
pwdLastSetHuman=$(date -j -f "%s" "$((($pwdLastSet/10000000)-11644473600))" "+%x %X")
lastPWChangeTrue=$((pwdLastSet/10000000-11644473600))
lastChangedDaysAgo=$((((lastPWChangeTrue-timeNow))/60/60/24))
convertLastChange="$(echo $lastChangedDaysAgo | awk -F "-" '{print $2}')"


# Print results and test account
border="=============================="

echo ""
echo $border
echo "Account Information: $userName"
echo $border

echo ""
echo "Name:$name"
echo "Job Title:$jobTitle"
echo "Password Last Set: $pwdLastSetHuman"
echo "Account Lockout:$lockoutTime"
echo "Account Expiration:$accountExpires"
echo ""

if [[ $lockoutTime -eq 0 ]]; then
	echo "[*] Account is not locked"
else
	echo "[!] Account is locked out!"
	echo "[!] Lockout Time: $lockoutTime"
fi

# TODO: Add a check for if expiration date is greater than today's date
if [[ $accountExpires -eq 0 ]]; then
	echo "[*] Account never expires"
else
	echo "[!] Account Expiration Date: $accountExpires"
fi

echo "[*] Password was last changed $convertLastChange days ago"
