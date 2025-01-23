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
  $username
)

function Get-ADAccountInfo($username){
    # Validate RSAT tools are installed
    if(Get-Module -list ActiveDirectory){
        Import-Module ActiveDirectory

        # Validate the user exists in the domain
        foreach ($user in $username){
            $aduser = Get-ADUser -filter "samAccountName -eq '$user'"

            # If account exists, pull details
            if ($aduser -ne $null){
                # Get PDC Emulator to get proper bad password count
                $PDCEmulator = (Get-ADDomain).PDCEmulator

                # Display account information
                $border = "=" * 30
                Write-Host "`n$border`nAccount Information: $user`n$border"
                Get-ADUser $user -properties * -Server $PDCEmulator | select name, samaccountname, EmailAddress, Title,`
                                                                      Lockedout, badpwdcount, Enabled, PasswordLastSet,`
                                                                      PasswordNeverExpires, PasswordExpired, AccountExpirationDate | fl

                # Check for locked account
                if ((Get-ADUser $user -properties LockedOut | Select-Object LockedOut) -match "True"){
                    $lockout = Get-ADUser $user -properties AccountLockoutTime | Select-Object AccountLockoutTime
                    Write-Host "[!] The account is locked" -ForegroundColor Red
                    Write-Host "[!] It was locked on $lockout" -ForegroundColor Red
                }
                else{
                    Write-Host "[*] The account is not locked"
                }

                # Check for disabled account
                if ((Get-ADUser $user -properties Enabled | Select-Object Enabled) -match "True"){
                    Write-Host "[!] The account is disabled" -ForegroundColor Red
                }
                else{
                    Write-Host "[*] The account is not disabled"
                }

                # Check for expired account
                if ((Get-ADUser $user -properties PasswordExpired | Select-Object PasswordExpired) -match "True"){
                    Write-Host "[!] The account is expired" -ForegroundColor Red
                }
                else{
                    Write-Host "[*] The account is not expired"
                }

                # Check for expired account
                if ($accountExpires -eq 0 -or $accountExpires -eq 9223372036854775807){
                    Write-Host "[*] The account never expires"
                }
                else{
                    $today = Get-Date
                    $expirationDate = Get-ADUser $user -Properties AccountExpirationDate | Select -ExpandProperty AccountExpirationDate
                    if ($expirationDate -eq $null){
                        Write-Host "[*] The account never expires"
                    }
                    elseif ($expirationDate -lt $today){
                        Write-Host "[!] The account expired on $expirationDate" -ForegroundColor Red
                    }
                    else{
                        Write-Host "[+] The account is not expired but does expire on $expirationDate"
                    }
                }
            }
            else{
                $border = "`n" + "=" * 30 + "`n"
                Write-Host "$border[!] Username $user does not exist in Active Directory" -ForegroundColor Red
            }
        }
    }
    else{
        Write-Host "[!] RSAT tools are not installed" -ForegroundColor Red
    }
}

Export-ModuleMember -Function Get-ADAccountInfo
