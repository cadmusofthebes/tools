#!/bin/bash

#############################################################
### Purpose: Enable/Disable a proxy via a bash command
### Author: CadmusOfThebes@protonmail.com
### Usage: Add the following line to your ~/.zshrc then turn it on or off with "proxy on" or "proxy off"
###        source "/path/to/proxy.sh"
#############################################################

excludedDomains="localhost,127.0.0.1/8"
proxy=""

function proxy() {
	if [[ $1 == "on" ]]; then
		export https_proxy=$proxy
		export http_proxy=$proxy
		export HTTPS_PROXY=$proxy
		export HTTP_PROXY=$proxy
		export no_proxy=$excludedDomains
		export NO_PROXY=$excludedDomains
	else
		unset https_proxy
		unset http_proxy
		unset HTTP_PROXY
		unset HTTPS_PROXY
		unset no_proxy
		unset NO_PROXY
	fi
}
