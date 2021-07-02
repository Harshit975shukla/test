def stockBuySell(price, n):
    if (n == 1):
        return
    i = 0
    while (i < (n - 1)):
        while ((i < (n - 1)) and
               (price[i + 1] <= price[i])):
            i += 1
        if i == n - 1:
            break
        buy = i
        i += 1

        while (i < n) and (price[i] >= price[i - 1]):
            i += 1
        sell = i - 1

        x = price[buy]
        y = price[sell]
        print(y-x)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        stockBuySell(arr,n)


if __name__ == '__main__':
    main()
