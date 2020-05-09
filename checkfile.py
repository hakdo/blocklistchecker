import sys

wordfile = sys.argv[1]
domainlist = []
urlhaus = open('maldomains.txt','r')
mydomains = urlhaus.readlines()
urlhaus.close()

sansdomains = open('sanslow.txt','r')
sansdata = sansdomains.readlines()
sansdomains.close()

phishdomains = open('phishtank.txt','r')
phishdata = phishdomains.readlines()
phishdomains.close()

# Remove first text, strip newlines, strip http://, strip https://
mydomains = mydomains[9:]

def cleanhaus(item):
  item = item.replace("http://",'')
  item = item.replace("https://",'')
  item = item.replace("\n",'')
  return item


domainlist = map(cleanhaus, mydomains)
sansdata = map(cleanhaus, sansdata)
phishdata = map(cleanhaus, phishdata)
domainlist = list(domainlist) + list(sansdata) + list(phishdata)
words = open(wordfile,'r')
mywords = words.readlines()
words.close()
mywords = map(cleanhaus, mywords)

try:
  if (sys.argv[2]) == 'l':
    print('Checking against ' + str(len(domainlist)) + ' bad domains.')
    runit = False
  else:
    runit = True
except:
  runit = True

if runit:
  for word in mywords:
    for domain in domainlist:
      if domain.find(word) > - 1:
        print(domain)
