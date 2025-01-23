#!/usr/bin/env python3
import requests
import sys
from argparse import ArgumentParser

#############################################################
### Purpose: Test to see if a given list of URLs are active
### Author: CadmusOfThebes@protonmail.com
#############################################################

def main(file):
    aliveURLs = []
    with open(file) as f:
        urls = f.readlines()
        for url in urls:
            url = url.strip()
            try:
                print(f"[*] Scanning {url}")
                r = requests.get(cleanURL(url), timeout=10)
                aliveURLs.append(url)
            except requests.exceptions.ConnectionError:
                pass
    print("\n[*] Reachable targets")
    for url in aliveURLs:
        print(url)

def cleanURL(url):
    try:
        url.split(":")[1]
        return(url)
    except IndexError:
        url = f"https://{url}"
        return(url)

def checkArguments():
    parser = ArgumentParser()

    parser.add_argument("--file", help="Provide list of URLs for scanning", required=True)

    args = parser.parse_args()

    if not args.file:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        main(args.file)
    
if __name__ == '__main__':
    checkArguments()
