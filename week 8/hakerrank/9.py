n = int(input())
dic = {} 
for i in range(0, n):
    arr = input().split()
    m = list(map(float, arr[1:]))
    dic[arr[0]] = sum(m)/float(len(m)) 
print("%.2f" % dic[input()])