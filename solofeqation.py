
def countSolutions(n, val):
    total = 0
    if n == 1 and val >= 0:
        return 1
    for i in range(val + 1):
        total += countSolutions(n - 1, val - i)
    return total
def main():
    t = int(input())
    for j in range(t):
        n,z = map(int,(input().split()))
        print(countSolutions(n, z))
        print("")
if __name__ == '__main__':
    main()