# File to fetch bad domains
import requests, os

api_phish = os.getenv('PHISHTANK_API_KEY')


blocklists = {
    'phishtank': {
        'url': 'http://data.phishtank.com/data/' + api_phish + 'online-valid.csv', 
        'update': '10min',
        'target': 'verified_online.csv'
    },
    'urlhaus': {
        'url': 'https://urlhaus.abuse.ch/downloads/text/',
        'update': '5min',
        'target': 'maldomains.txt'
    },
    'sans': {
        'url': 'https://isc.sans.edu/feeds/suspiciousdomains_Low.txt',
        'update': 'daily',
        'target': 'sanslow.txt'
    }
}

def badstuff(source):
    mydata = requests.get(source["url"])
    outdata = mydata.text
    outfile = open(source["target"],'w')
    outfile.write(outdata)
    outfile.close()

for key in blocklists.keys():
    badstuff(blocklists[key])


