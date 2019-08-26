#!/usr/bin/python3

# 5. Write a program, which will take domain name (e.g. google.com) as a script parameter 
# and print next domain info: 
# domain name, 
# domain’s date of creation, 
# A and MX(if present) records info (IP address). 
# Use search API: https://api.domainsdb.info/search?query={domain_name}
    
import json
import sys
import requests

if (len(sys.argv) != 2):
    print("You should type a domain name as argument!")
    sys.exit(1)

url = "https://api.domainsdb.info/search?query=%s" % (sys.argv[1])

s = requests.Session()
r = s.get(url)
jresp = r.json()


print("Found %s record for this domain." % len(jresp['domains']))
for domain in jresp['domains']:
    print("Domain <%s> :" % domain['domain'])
    print("  Created:", domain['create_date'])
    if domain.get('A') != None :
        print("  A records:")
        for arec in domain['A']:
            print("   ",arec)
    if domain.get('MX') != None :
        print("  MX records:")
        for mxrec in domain['MX']:
            print("   ",mxrec['exchange'])
    print()
