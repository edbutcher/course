# Uses python3

n = (input().split())
a, b = int(n[0]), int(n[1])


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(gcd(a, b))