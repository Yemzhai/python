n = int(input())

def stepen(val, i):
    sm = 1
    while(i != 0):
        sm *= val
        i -= 1
    return sm

for i in range(0, n+1):
    val = stepen(2, i)
    if(val == n):
        print("YES")
        break
    if(val > n):
        print("NO")
        break
    
    