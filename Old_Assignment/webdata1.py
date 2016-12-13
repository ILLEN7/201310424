import urllib
response=urllib.urlopen('http://www.python.org')
_html=response.read()
print response.info()
print len(_html)
print type(_html)

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r=requests.get('http://python.org/')

html=lxml.html.fromstring(r.text)
sel=CSSSelector('a[href]')
nodes=sel(html)

for node in nodes:
    print node.get('href'), node.text