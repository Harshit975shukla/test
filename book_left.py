n , k = map(int,input().split())
arr = list(map(int,input().split()))
c = 0
f = 0
for i in range(n):
    if arr[i] > k:
        f = 1
        break
    else:
        c += 1
if f == 1:
    arr.reverse()
    for i in range(n):
        if arr[i] > k:
            f = 1
            break
        else:
            c += 1
print(n-c)