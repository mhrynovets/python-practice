#!/usr/bin/python3
""" Show information about domain """
# 5. Write a program, which
# will take domain name (e.g. google.com) as a script parameter
# and print next domain info:
# domain name,
# domain’s date of creation,
# A and MX(if present) records info (IP address).
# Use search API: https://api.domainsdb.info/search?query={domain_name}

import argparse
import sys
import requests


def main():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Domain to search information about')
    parser.add_argument('-c', '--created', action='store_true',
                        help='show domain’s date of creation')
    parser.add_argument('-a', '--arecords', action='store_true',
                        help='show domain’s A records')
    parser.add_argument('-m', '--mxrecords',
                        action='store_true', help='show domain’s MX records')
    args = parser.parse_args()
    url = f"https://api.domainsdb.info/search?query={args.url}"

    try:
        resp = requests.get(url)
        jresp = resp.json()
    except requests.exceptions.ConnectionError:
        print('Connection error. Check internet connection or try later.')
        sys.exit(1)
    except AttributeError:
        print('Got unexpected answer from server. Exit.')
        sys.exit(1)

    print("Found {} record for this domain.".format(len(jresp['domains'])))
    for domain in jresp['domains']:
        print("Domain <{}> :".format(domain['domain']))
        if args.created:
            print("  Created:", domain['create_date'])
        if args.arecords and domain.get('A') is not None:
            print("  A records:")
            for arec in domain['A']:
                print("   ", arec)
        if args.mxrecords and domain.get('MX') is not None:
            print("  MX records:")
            for mxrec in domain['MX']:
                print("   ", mxrec['exchange'])


if __name__ == "__main__":
    main()
