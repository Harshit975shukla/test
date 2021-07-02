def tower(n,s,d,h):
    if n == 1:
        print("move disk from",s," to ",d)
        return
    tower(n-1,s,h,d)
    print("move disk from",s," to ",d)
    tower(n-1,h,s,d)

def main():
    n = int(input())
    tower(n,1,3,2)

if __name__ == '__main__':
    main()
