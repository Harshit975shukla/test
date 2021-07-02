def rigrotate(arr,i,j):
    while i <= j:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
        i += 1
        j -= 1




def main():
    t = int(input())
    for i in range(t):
        n , k = map(int,input().split())
        arr = list(map(int,input().split()))
        rigrotate(arr,k,n-1)
        print(arr)
        rigrotate(arr,0,k-1)
        print(arr)
        rigrotate(arr,0,n-1)
        print(arr)
if __name__ == "__main__":
    main()