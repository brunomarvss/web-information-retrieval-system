import re
import nltk
import gzip
import urllib2
from bs4 import BeautifulSoup
from StringIO import StringIO
from timeit import timeit

#reload(sys)
#sys.setdefaulencoding('utf-8')

def clean_html(html):

    #Remove JavaScript/CSS:
    cleaned = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", html.strip())
    #Remove html comments
    # Tags 
    cleaned = re.sub(r"(?s)<!--(.*?)-->[\n]?", "", cleaned)
    # more Tags
    cleaned = re.sub(r"(?s)<.*?>", " ", cleaned)
    # Remove whitespace
    cleaned = re.sub(r"&nbsp;", "", cleaned)
    cleaned = re.sub(r"  ", "", cleaned)
    cleaned = re.sub(r"  ", "", cleaned)

    return cleaned.strip()


request = urllib2.Request('https://blog.hartleybrody.com/web-scraping/')
#print urllib2.urlopen('http://docs.python-guide.org/en/latest/scenarios/scrape/').getcode()
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)
if response.info().get('Content-Encoding') == 'gzip':
    buf = StringIO( response.read())
    f = gzip.GzipFile(fileobj=buf)
    data = f.read()
else:
    data = request.read()
h_data =  clean_html(data).split(' ')

h_data = ' '.join(h_data).split()

#other way in stripping whitespace on a list
#h_data = filter(None, h_data)
#h_data = [x.strip(' ') for x in h_data]
#print timeit("' '.join(h_data).split()",'argument',number=10000000)



file = open("rdata.txt", "w")

for val in h_data:
    file.write(val + ' ')
file.close()

