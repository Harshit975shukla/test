import math


def sieve(n):
    sieve = [1] * (n+1)
    sieve[1] = 0
    sieve[0] = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if sieve[i] == 1:
            for j in range(i*i, n + 1, i):
                sieve[j] = i ##use 1 to convert sieve
    for i in range(n+1): ##extra condition to change 1 into i
        if sieve[i] == 1 or sieve[i] == 0:
            sieve[i] = i
    return sieve


def main():
    n = int(input())
    arr = sieve(n)
    for i in range(len(arr)):
        print(i,"=",arr[i],end = " ")
        print(" ")
        #if arr[i] == 1:  ## printing only prime number
           # print(i, end=" ")


if __name__ == '__main__':
    main()
