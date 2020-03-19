n = int(input())
v = [int(i) for i in input().split()]
ok = False
for i in range(1, n):
    if(v[i-1] < 0 and v[i] < 0):
        ok = True
        break
    elif(v[i-1] >= 0 and v[i] >= 0):
        ok = True
        break
if(ok):
     print("YES")
else:
     print("NO")
