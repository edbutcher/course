import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_333665.xml'
data = urllib.urlopen(url).read()

mn = []

stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
print len(lst)
for item in lst:
    x = int(item.find('count').text)
    mn.append(x)
print sum(mn)
