# Uses python3

n = (input().split())
a = int(n[0])
b = int(n[1])

def gcd(a, b):
    while a != b:
        if a > b:
            a = a / b
        else:
            b = b / a
    return a
