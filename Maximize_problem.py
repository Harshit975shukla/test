n, k = map(int, (input().split()))
ele = 240 - k
arr = [0]
for i in range(1, n + 1):
    arr.append((5 * i) + arr[i-1])
print(arr)
print(ele)
ans = 0
for j in range(n+1):
    if arr[j] > ele:
        ans = j - 1
        break
    if arr[j] == ele:
        ans = j
        break
    else:
        ans = n
print(ans)