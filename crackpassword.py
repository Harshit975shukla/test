def reccombi(arr, op, i, index, n, k):
    if k == 0:
        for j in range(len(op)):
            print(op[j], end="")
        print("")
        return
    for j in range(0, n):#if need all possible then use 0 index instant of i
        op[index] = arr[j]
        reccombi(arr, op, j + 1, index + 1, n, k - 1)


def main():
    t = int(input())
    for x in range(t):
        n = 9
        arr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        k = int(input())
        op = [0] * k
        reccombi(arr, op, 0, 0, n, k)


if __name__ == "__main__":
    main()
