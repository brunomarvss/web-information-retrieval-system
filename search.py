#!/usr/bin/env python2.7


import requests
import json
import re
from urllib2 import urlopen


class Search(object):

    #def __init__(self):
        
        #do something
    #@staticmethod --- not using sel to call a function
    
    def fetch_url(self, query):
        googleAPI = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='

        r = requests.get(googleAPI + query + '&rsz=8')
        theJson = r.content
        return json.loads(theJson)

    
    #@staticmethod
    def process_url(self, obj):
        title_url = []
        for index,result in enumerate(obj['responseData']['results']):
            x = str(index+1) + ") " + result['titleNoFormatting']
            x = re.sub('[^A-Za-z]+', ' ', x)
            tup = (x, result['url'])
            title_url.append(tup)


        return title_url

    
