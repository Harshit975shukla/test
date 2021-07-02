i = int(input())
e = int(input())
inter = []
exter = []
itotal = 0
etotal = 0
total = 0
for j in range(i):
    x = float(input())
    inter.append(x)
for j in range(e):
    x = float(input())
    exter.append(x)
for j in range(len(inter)):
    itotal = itotal + (inter[j]*18)
for j in range(len(exter)):
    etotal = etotal + (exter[j]*12)
total = itotal + etotal
print(total)