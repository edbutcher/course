import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_333669.json'
data = urllib.urlopen(url).read()

info = json.loads(data)
y = []
x = info["comments"]
for item in x:
    y.append(item['count'])
print sum(y)
