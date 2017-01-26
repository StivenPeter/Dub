from flask import request
import rauth
import urllib
import urllib2
import json
from requests_oauth2 import OAuth2


def iGotTheKeys():
    files = open('keys.txt','r')
    keydata=files.readlines()
    d={}
    l=[]
    for keys in keydata:
        l.append(keys)
    d['ConsumerK']=l[0]
    d['ConsumerS']=l[1]
    d['Token']=l[2]
    d['TokenS']=l[3]
    d['event']=l[4]
    files.close()
    return d


kdict=iGotTheKeys()
#print kdict

consumer_key = kdict['ConsumerK'].strip()

consumer_secret = kdict['ConsumerS'].strip()
token = kdict['Token'].strip()
token_secret = kdict['TokenS'].strip()




session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)

def getResult(location, food):
    payload={}
    payload['term']=food
    payload['location']=location
    data= session.get('https://api.yelp.com/v2/search', params=payload)
    data=data.json()
    places=[]
    for x in data['businesses']:
        print x
        i=[]
        i.append(x['name'])
        i.append(x['location']['display_address'][0])
        i.append(x['rating'])
        i.append(x['image_url'])
        i.append(x['mobile_url'])
        places.append(i)
        i=[]
    return places


print getResult('Brooklyn','sushi')

