n = 3
arr1 = []
arr2 = []
arr3 = []
fit = []
for i in range(3):
    x = int(input())
    arr1.append(x)
if sum(arr1) // 3 > 70:
    fit.append(sum(arr1) // 3)
for i in range(3):
    x = int(input())
    arr2.append(x)
if sum(arr1) // 3 > 70:
    fit.append(sum(arr2) // 3)
for i in range(3):
    x = int(input())
    arr3.append(x)
if sum(arr1) // 3 > 70:
    fit.append(sum(arr3) // 3)
print(fit)
max = fit[0]
c = 0
final = []
for i in range(1,len(fit)):
    if max < fit[i]:
        max = fit[i]
        c = i
    if max == fit[i]:
        final.append(i)
if fit[0] == max and 0 not in final:
    final.append(0)
final.sort()
if len(final) > 1:
    for i in range(len(final)):
        print("most fit candided is {} with {} level".format(i,max))
else:
    print("most fit candided is{} with {} level".format(c, max))
print(fit)
print(final)

