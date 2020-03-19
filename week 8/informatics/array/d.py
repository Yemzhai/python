n = int(input())
v = [int(i) for i in input().split()]
cnt = 0
for i in range(1, n):
    if(v[i] > v[i-1]):
        cnt += 1
print(cnt)
