n = int(input())
x = input()
q = x.split()
v = list(map(int, q))
mx = max(v)
for i in range(0, n):
    if max(v) == mx:
        v.remove(max(v))
print(max(v))