def factorsListFunc(first, each_prod, n, single_result_list):
    if first > n or each_prod > n:
        return
    if each_prod == n:
        print(*single_result_list)
        return
    for i in range(first, n + 1):
        if i * each_prod > n:
            break
        if n % i == 0:
            single_result_list.append(i)
            factorsListFunc(i, i * each_prod, n, single_result_list)
            single_result_list.remove(single_result_list[-1])


def factcomb(n):
    single_result_list = [1]
    factorsListFunc(2, 1, n, single_result_list)


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        factcomb(n)


if __name__ == '__main__':
    main()
