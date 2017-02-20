# Uses python3
n = int(input())

a, b = 0, 1

for i in range(1,n):
    a, b = b, (a+b) % 10
print(b)
