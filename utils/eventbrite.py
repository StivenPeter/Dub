import json
import urllib
import urllib2
## returns a list of dictionaries




def getEvents(keyword):
        keyz=iGotTheKeys()['event']
        keyword='&q='+keyword
        location='&location.address=new+york'
        url = "https://www.eventbriteapi.com/v3/events/search/?token="+keyz+keyword+location
        response = urllib2.urlopen(url)
        eventdata = response.read()
        dic = json.loads(eventdata)
        dic=dic['events']
        print dic
        eventdict = {}
        eventlist=[]
        for events in dic:
            eventdict['name']=events['name']['text'] 
            eventdict['url']=events['url']
            #eventdict['description']=events["description"]["text"]
            eventlist.append(eventdict)
        #print eventlist[0]['url']
        #print eventlist[0]['name']
        #print eventlist
        return eventlist
        
            

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



getEvents('marathon')

#print getEvents('marathon')

