def suma(n):
    if n == 1 or n == 0:
        return n
    return n + suma(n - 1)
from sys import setrecursionlimit
setrecursionlimit(11000)
def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(suma(n),end="")
        print("")
if __name__ == '__main__':
    main()
