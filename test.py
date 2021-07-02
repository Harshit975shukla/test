def merge(S1, S2, N):
    s = ""
    la = len(S1)
    lb = len(S2)
    l = la + lb
    indexa = indexb = 0

    while l:
        pa = pb = 0

        if la - indexa >= N:
            s = s + a[indexa: indexa + N]
            indexa = indexa + N
            pa = N
        elif la - indexa < N and la - indexa:
            s = s + a[indexa: la]
            pa = la - indexa
            indexa = la
        elif indexa >= la:
            pa = 0
        if lb - indexb >= N:
            s = s + b[indexb: indexb + N]
            pb = N
            indexb = indexb + N
        elif lb - indexb < N and lb - indexb:
            s = s + b[indexb: lb]
            pb = lb - indexb
            indexb = lb
        elif indexb >= lb:
            pb = 0
        l = l - pa - pb

    print(s)
N = int(input())
a = input()
b = input()
merge(a,b,N)