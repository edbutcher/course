import re

f = open('actual.txt')
s = f.read()
y = re.findall('[0-9]+', s)

x = 0
for i in y:
        x = x + int(i)
print x
