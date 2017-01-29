import urllib
from BeautifulSoup import *
url = 'http://python-data.dr-chuck.net/known_by_Kofi.html'
for i in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    s = []

    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
    print s[17]
    url = s[17]
print "ansver:", s[17]
