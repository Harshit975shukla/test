import math


def sieve(n):
    sieve = [1] * (n+1)
    sieve[1] = 0
    sieve[0] = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if sieve[i] == 1:
            for j in range(i*i, n + 1, i):
                sieve[j] = 0
    return sieve
def odd_prime(a):
    while a != 0:
        y = a % 10
        if y == 3 or y == 5 or y ==7:
            return False
        else:
            a = a // 10
    return True

def main():
    t = int(input())
    for j in range(t):
        x = int(input())
        n = 75000
        arr = sieve(n)
        result = []
        final = []
        sum = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                result.append(i)
        for i in range(len(result)):
            if (odd_prime(result[i])):
                final.append(result[i])
        for i in range(x):
            sum = sum + final[i]
        print(sum)


if __name__ == '__main__':
    main()