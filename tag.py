# Simple autotagging script - for infosec texts

"""
To use: from tag import tagit
tagit(str) returns a list of tags
Made by hakon@cybehave.com
"""

data = 'Hackers were planning to use COVID-19-themed malicious emails to phish and infect Romanian hospitals with ransomware and disrupt operations.'

tagback = {
  'malware': ['malware','ransomware','virus','trojan','emotet','infect','ruyk','crypter'],
  'attack': ['target', 'phishing attack', 'brute force','password spray','attack'],
  'socialengineering': ['phish', 'malicious email', 'maldoc','smishing','vishing','bce','business email compromise','social engineering'],
  'atp': ['atp','fancy bear'],
  'appsec': ['appsec','cross site scriptin','cross-site scripting','application security','web security','websec','owasp','xss','clickjacking','sqli','csrf','xsrf','security headers','secheaders','csp','content security policy'] ,
  'privacy': ['gdpr','ccpa','privacy','databreach','ico','dpo','general data protection regulation','personal data', 'pii','data protection officer']
}

normalizers = {
  'phishingattack': 'phishing',
  'businessemailcompromise': 'bce',
  'maliciousemail': 'phishing',
  'phish': 'phishing',
  'infect': 'malware',
  'applicationsecurity': 'appsec',
  'websecurity': 'appsec',
  'xsrf': 'csrf', 
  'secheaders': 'securityheaders',
  'contentsecuritypolicy': 'csp',
  'sqlinjection': 'sqli',
  'cross-sitescripting': 'xss',
  'target': 'attack',
  'crosssitescripting': 'xss',
  'generaldataprotectionregulation': 'gdpr',
  'personaldata': 'privacy',
  'pii': 'privacy',
  'dataprotectionofficer': 'dpo'
}

import re

def cleaner(raw_data):
  # Naive cleaner to remove some tags and special characters
  subber = re.compile('<*?>')
  subber2 = re.compile('[<>/\n]+')
  out = re.sub(subber, '', raw_data)
  out = re.sub(subber2, '', out)
  out = out.lower()
  return out

def normtag(tag):
  # Tag normalisation to avoid multiple tags with the same meaning
  tag = tag.replace(" ","")
  if tag in normalizers.keys():
    tag = normalizers[tag]
  return tag

def dumbtag(data):
  # Traverses a tree to add tags
  taglist = []
  for mothertag in tagback.keys():
    for tag in tagback[mothertag]:
      checkit = data.find(tag)
      if checkit > -1:
        newtag = normtag(tag)
        taglist.append('#' + newtag)
  return list(set(taglist))

def cvetagger(data):
  # Find CVE references in the input string
  cvem = re.compile('CVE-\d{4}-\d{4,7}', re.I) # case insensitive although CVE's should be capitalized, for normalization
  out = re.findall(cvem, data)
  if len(out) > 0:
    out.append('CVE')
  return list(set(out))

def tagit(raw_data):
  cdata = cleaner(raw_data)
  taglist = dumbtag(cdata)
  cvelist = cvetagger(cdata)
  # cap cve tags
  cvelistc = []
  for cve in cvelist:
    cvelistc.append('#' + cve.upper())
  taglist = taglist + cvelistc
  return list(set(taglist))



