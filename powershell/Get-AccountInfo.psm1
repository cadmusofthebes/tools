<#
 .Synopsis
 Display important information about a given AD account

 .Description
 Display important information about a given AD account

 .Parameter Username
 The samAccountName to query

 .Example
    # Perform a basic search
    # Get-ADAccountInfo -username USERNAME
    # Get-ADAccountInfo USERNAME
#>

# Validate Parameters
[CmdletBinding()]
Param(
    [switch] $help,
    $username
)

echo $PSScriptRoot
. $PSScriptRoot\Get-ADAccountInfo.ps1 $username

# Add this to profile to auto-import
# Import-Module C:\<path>\Get-AccountInfo.psm1
