f = open("file.txt", "r")
digits = []
for i in f.read():
    if i.isdigit():
        digits.append(i)

print sum(digits)
