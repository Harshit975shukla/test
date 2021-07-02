def removeadj(st):
    if len(st) == 1:
        return st
    elif st[0] != st[1]:
       return st[0] + removeadj(st[1:])
    else:
       return removeadj(st[1:])


def main():
    s = input()
    print(removeadj(s))


if __name__ == '__main__':
    main()
