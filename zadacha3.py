a = int(input('введите число- '))
b = int(input('введите степень '))
r = 1

if b > 0:
        for i in range(b+1):
            if i == 0:
                continue

            r*=a
        print(r)