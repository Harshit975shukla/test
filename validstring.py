n = int(input())
for j in range(n):
    s = list(input())
    stack = list()
    print(stack)
    f = 0
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                f += 1
                if f == 2:
                    break
            else:
                stack.pop()
        print(stack)
    if f == 2 or len(stack) != f:
        print("No")
    else:
        print("Yes")
