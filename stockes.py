arr = []
result = 0
for i in range(7):
    x = int(input())
    arr.append(x)
tmp = arr[0]
try:
    for i in range(7):
        if tmp < arr[i]:
            result = result + (arr[i] - tmp)
            tmp = arr[i + 1]
        elif max(arr) == arr[0]:
            result = 0
except:
    pass
print(result)
