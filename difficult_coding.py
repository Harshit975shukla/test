t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    flag = 0
    for j in range(len(arr)):
        if arr[j] == 1:
            flag = 1
            break
    if flag == 0:
        print("easy")
    else:
        print("hard")