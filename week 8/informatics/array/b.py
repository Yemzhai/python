n = int(input())
v = [int(i) for i in input().split()]
for i in range(0, n):
    if(v[i]%2 == 0):
        print(v[i], end=' ')
