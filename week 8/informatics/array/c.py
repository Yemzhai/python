n = int(input())
v = [int(i) for i in input().split()]
cnt = 0
for i in range(0, n):
    if(v[i] > 0):
        cnt += 1
print(cnt)
