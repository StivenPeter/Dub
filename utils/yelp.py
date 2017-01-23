from flask import request
import rauth
import urllib
import urllib2
import json
from requests_oauth2 import OAuth2


consumer_key = "7_EwDMS6kxqq1s1xryfX2Q"
consumer_secret = "rt2PahWel9AuFUXH9YgZm0rriKk"
token = "LZK4mRye4lC0tH1piE7niTkQiXKa_GD_"
token_secret = "7fu_bhr4zcJ4Je4Cl487unVTsrg"

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
        i=[]
        i.append(x['name'])
        i.append(x['location']['display_address'][0])
        i.append(x['display_phone'])
        i.append(x['rating'])
        i.append(x['image_url'])
        places.append(i)
        i=[]
    return places

#print getResult('Brooklyn','sushi')

