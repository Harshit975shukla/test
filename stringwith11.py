def countSubStr(st, n):
    m = 0
    for i in range(0, n):
        if (st[i] == '1'):
            m = m + 1
    return m+(m * (m - 1) // 2)
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input()
        arr = list(arr)
        res = countSubStr(arr,n)
        print(res)
if __name__ == '__main__':
    main()