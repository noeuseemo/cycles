n = int(input('введите целое число- '))
v = []

if n < 0:
        print('error')
else:
        while n != 0:
            v.append(n % 10)
            n = n // 10

v.reverse()
print(v)