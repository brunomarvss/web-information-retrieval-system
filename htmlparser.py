#!/usr/bin/env python2.7


import re
import nltk
import gzip
import socket
import urllib2
import string
from nltk.tokenize import WhitespaceTokenizer
from bs4 import BeautifulSoup
from StringIO import StringIO
from timeit import timeit

class htmlParser:


    #def __init__(self):
        #do something

    def clean_html(self, html):

        #Remove JavaScript/CSS:
        
        cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
        #Remove html comments
        # Tags 
        cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
        # more Tags
        cleaned = re.sub(r"(?s)<.*?>", "", cleaned)
        # Remove whitespace
        cleaned = re.sub(r"&nbsp;", "", cleaned)
        cleaned = re.sub(r"  ", "", cleaned)
        cleaned = re.sub(r"  ", "", cleaned)
        cleaned = re.sub("(?m)^\s+", "", cleaned)
        #cleaned = ' '.join(cleaned.split())
        return cleaned.strip('')

    def url_opener(self, url):

        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:
            data = request.read()
        
        return data
    def url_ip(self, url):
        ip = socket.gethostbyname(url)

        return ip

#if __name__ == '__main__':
#    htmlParser()



