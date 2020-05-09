#!/usr/local/bin/python3
import sys, re

linkurl = sys.argv[1]
domainlist = []
urlhaus = open('maldomains.txt','r')
mydomains = urlhaus.readlines()
urlhaus.close()

sansdomains = open('sanslow.txt','r')
sansdata = sansdomains.readlines()
sansdomains.close()
mydomains = mydomains[9:]

def cleanhaus(item):
  item = item.replace("http://",'')
  item = item.replace("https://",'')
  item = item.replace("\n",'')
  item.strip()
  return item

def undress(link):
    # get only the naked domain. Should not contain http://, https://, run cleanhaus first
    mydata = link.split('/')
    try:
        target = mydata[0]
    except:
        print('No SLASH found, taking full link as domain')
        target = link
    # Check if target is an ip address
    out = re.search('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', target)
    if not out:
        # We have a domain
        targetsplit = target.split('.')
        try:
            target = ''.join(targetsplit[-2:],'.')
        except:
            pass
    return target


domainlist = map(cleanhaus, mydomains)
sansdata = map(cleanhaus, sansdata[16:])
domainlist = list(domainlist) + list(sansdata)

linkurl = cleanhaus(linkurl)
tldlist = list(map(undress, domainlist))
target = undress(linkurl)
stopsearch = False
for domain in domainlist:
    if linkurl == domain:
        # Checking exact match
        print('Bad: ' + domain)
        stopsearch = True
        break
    # Check also if there is a naked domain match
if not stopsearch:
    for domain in tldlist:
        if target == domain:
            print('Match on top level domain (NOT EXACT): ', domain)
            break
if not stopsearch:
    print('URL not found in tracked blocklists.')