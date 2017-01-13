import json
import urllib
import urllib2


def getEvents(keyword):
        keyword='&q='+keyword
        location='&location.address=new+york'
        url = "https://www.eventbriteapi.com/v3/events/search/?token=KEY"+keyword+location
        response = urllib2.urlopen(url)
        eventdata = response.read()
        dic = json.loads(eventdata)
        dic=dic['events']
        eventdict = {}
        eventlist=[]
        for events in dic:
            eventdict['name']=events['name']['text']
            eventdict['url']=events['url']
            eventdict['description']=events["description"]["text"]
            eventlist.append(eventdict)
        print eventlist[0]['url']
        print eventlist[0]['name']
        print eventlist[0]['description']
        return eventlist
        
            

        



#getEvents('marathon')
