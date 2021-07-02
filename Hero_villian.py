import math
t = int(input())
for i in range(t):
    n =int(input())
    arr = list(map(int,input().split()))
   # print(arr)
    c = 0
    res = math.gcd(arr[0],arr[1])
    for j in range(2,len(arr)):
      #  print(res,arr[j])
        res = math.gcd(res,arr[j])
    for j in range(1,res+1):
        if res % j == 0:
            c += 1
    print(c)