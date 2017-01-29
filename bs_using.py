import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup('span')

x = None
s = []

for tag in tags:
    x = int(tag.contents[0])
    s.append(x)

print sum(s)
