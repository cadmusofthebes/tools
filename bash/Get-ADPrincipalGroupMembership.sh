#!/bin/bash

#############################################################
### Purpose: Lookup domain group membership on MacOS
### Author: CadmusOfThebes@protonmail.com
#############################################################

# Validate a group was given
if [[ $# -eq 0 ]] ; then
    echo "[!] ERROR: Missing group and/or domain parameter"
    echo "[*] Usage: $0 <group> <domain>"
    exit 0
fi


# Run dscl against the given group
groupName=$1
domain=$2

border="=============================="

echo ""
echo $border
echo "Group Membership: $groupName"
echo $border

dscl "/Active Directory/$domain/All Domains" cat /Groups/$groupName GroupMembership | awk -F "\\" '{print $2}'
