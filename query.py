import json, urllib2
key = "bc493743-092d-4f6f-8716-2d3097d603a9"
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
