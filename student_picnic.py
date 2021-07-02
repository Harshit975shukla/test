import math
def isprime(n):
    if n == 1 or n == 0:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return 1



def main():
    n, k = map(int, (input().split()))
    arr = []
    for i in range(n):
        r = int(input())
        while r != 0:
            x = r % 10
            arr.append(x)
            r = r // 10
        a = isprime(arr[0])
        b = isprime(arr[-1])
        if arr[0] + arr[-1] > k:
            c = 1
        else:
            c = 0
        if a + b + c == 3:
            print("Yes")
        else:
            print("No")
        arr =[]
if __name__ == '__main__':
    main()