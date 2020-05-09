# blocklist checkers
This is a simple collection of Python scripts to fetch and check links and words against spam and malware blocklists. 

## Phishtank API key
You will need a phishtank API key to use the `fetchbadness.py` script as-is. 

Set your  phishtank API key as an environment variable called 

`PHISHTANK_API_KEY`.

## Get the blocklists
You collect the blocklists by running  `python fetchbadness.py`. The script then collects 3 blocklists: 

- URLhaus: a malware blocklist (TXT)
- SANS low sensitivity list: a collection list by SANS, may contain false positives (TXT)
- Phishtank list (CSV)

These lists are updated frequently, if you want to use these scripts in your daily workflow you may want to set 
up a scheduled task to pull data.

The scripts operate on simple text files, so the CSV file from Phishtank must be converted. This can be done by running
the utility script `phishit.py` with no arguments. 

## Check a link
To check a link run: `python3 links.py mylink.com`.

The output depends on the finding: 
- Not found in blocklists
- Exact match of URL
- Domain found

## Check a list of words
If you want to check if a list of words is found in any of the blocklists, you create a file with one word on each line and use as input to `checkfile.py`. We can use this to check if typosquatting domains are found in the blocklists, or to find such domains for typical keywords. Let's look for blocklist entries mactching the names of common communication platforms: 

- skype
- zoom
- meet
- webex

This will print every found domain wiht that word match to the standard output. Counting these matches we see there is a lot of this type of abuse of brand names: 

```bash  
>> python3 checkfile.py test.txt |wc -l
  173
```
