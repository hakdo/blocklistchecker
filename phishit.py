# Convert phishtank CSV to plaintext list
phishdata = open('verified_online.csv','r')
# Read it into a list
myphishdata = phishdata.readlines()
phishdata.close()

urls = []
for line in myphishdata[1:]:
    datasplit = line.split(',')
    urls.append(datasplit[1])

# OK, we got the phishes, now add them to a file
myfile = open('phishtank.txt','w')
for item in urls:
    myfile.write(item + '\n')
myfile.close()
