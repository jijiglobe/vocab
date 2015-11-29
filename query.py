import json, urllib2
from temboo.Library.Wordnik.Word import GetEtymology
from temboo.core.session import TembooSession

websterKey = "bc493743-092d-4f6f-8716-2d3097d603a9"
wordnikKey = "e832a6ca17874df39200204fc350926dc62d219664357eb3e"

domain = "http://www.dictionaryapi.com/"
api = "/api/v1/references/sd4/xml/%s?key="+websterKey

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

def breakIntoElements(xml):
    xml = xml.split("<entry id=")
    return xml;

def findTag(xml,tag): 
    xml = xml.split(tag)
    tag = "</"+tag[1:]
    xml[1] = xml[1].split(tag)
    return xml[1][0]

def getPartOfSpeech(xml,word):
    xml = breakIntoElements(xml)
    return findTag(xml[1],"<fl>")

#print getPartOfSpeech(getXML("test"),"test")

def getEtymology(word):
    #Code snippets stolen from Temboo.com

    # Create a session with your Temboo account details
    session = TembooSession("jijiglobe", "myFirstApp", "44421ac2aaac44d9961d65193aa6c26d")
    
    # Instantiate the Choreo
    getEtymologyChoreo = GetEtymology(session)
    
    # Get an InputSet object for the Choreo
    getEtymologyInputs = getEtymologyChoreo.new_input_set()
    
    # Set the Choreo inputs
    getEtymologyInputs.set_APIKey(wordnikKey)
    getEtymologyInputs.set_Word(word)
    
    # Execute the Choreo
    getEtymologyResults = getEtymologyChoreo.execute_with_results(getEtymologyInputs)
    
    # Print the Choreo outputs
    return getEtymologyResults.get_Response()

print getEtymology(raw_input())
