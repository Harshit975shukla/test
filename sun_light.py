t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    c = 1
    curr_max = arr[0]
    for j in range(1, n):
        if (arr[j] > curr_max or arr[j] == curr_max):
            c += 1
            curr_max = arr[j]
    print(c)
