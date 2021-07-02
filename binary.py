def binary(n,prv,out, i):
    if n == 0:
        for j in range(len(out)):
            print(out[j], end="")
        print("")
        return
    if (prv == 0 or prv == -1):
        out[i] = 0
        binary(n - 1,0, out, i + 1)
        out[i] = 1
        binary(n - 1, 1,out,i + 1)
    else:
        out[i] = 0
        binary(n - 1, 0, out, i + 1)

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        out = [-1] * n
        (binary(n, -1, out, 0))


if __name__ == "__main__":
    main()
