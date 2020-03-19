cnt = 0
n = int(input())
while(n != 0):
    x = int(input())
    if(x == 0):
        cnt += 1;
    n -= 1
print(cnt)