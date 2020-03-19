a, b, c, d = map(int, input().split())


def Min(a, b, c, d):
    mn = min(min(a, b), min(c,d))
    return mn

mn = Min(a, b, c, d) 
print(mn)