t = int(input())
arr = [0] * 10**6
for i in range(t):
    n = int(input())
    arr1 =list(map(int,input().split()))
    for j in range(n):
        x = arr1[j]
        arr[x] += 1
    y = max(arr)
    if y > (n//2):
        res = arr.index(y)
    else:
        res = -1
    print(res)
    arr = [0] * 10**6
