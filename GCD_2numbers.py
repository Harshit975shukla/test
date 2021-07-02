t = int(input())
for i in range(t):
    n , m = map(int,(input().split()))
    gcd = 1
    for j in range(2,min(n,m)+1): # +1 to check if both no. are same
        if n % j == 0 and m % j == 0:
            gcd = j
    print(gcd)
