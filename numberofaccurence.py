def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list((input().split()))
        c = 0
        for j in range(n):
            if arr[j] == 'x':
                c += 1
        print(c)
if __name__ == '__main__':
    main()
