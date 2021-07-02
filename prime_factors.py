import math
arr = []
n = int(input())
for i in range(2,int(math.sqrt(n)+1)):
    while (n % i == 0):
        n = n // i
        arr.append(i)
    if n == 1:
        break
if n > 1:
    arr.append(n)
print(arr)