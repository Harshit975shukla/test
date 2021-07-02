import math
def ncr(n, r):
    ans = 1
    for i in range(1,r+1):
        ans *= (n - r + i)
        ans //= i
    return ans
def totalways(X, Y, M, W):

    return (ncr(M, X) * ncr(W, Y))

def main():
    t = int(input())
    for i in range(t):
        m,w,x,y = map(int,(input().split()))
        res = (totalways(x,y,m,w))
        res = res * math.factorial(x+y)
        print(res)
if __name__ == '__main__':
    main()
