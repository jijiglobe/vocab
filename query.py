import json, urllib2
key = "b4e2408f-1ee2-4917-95d9-c0ff9eff196f"
domain = "http://www.dictionaryapi.com/"
api = "/api/v1/references/sd4/xml/%s?key="+key

hdr = {
    'User-Agent': 'Mozilla',
    'Accept': 'xml',
    'Accept-Language': 'en-us',
}

def getXML(word):
    req = urllib2.Request((domain+api) % word,headers=hdr)
    request = urllib2.urlopen(req)
    result = request.read()
    
    return result

print getXML(raw_input())
