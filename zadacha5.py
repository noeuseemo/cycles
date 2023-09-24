n = int(input('введите значение n-  '))

r = [0, 1]

for i in range(n+1):
    if n <= 1:
            break
    elif i == 0:
            continue

    r.append(r[i-1]+r[i])

if n > 1:
    r.pop(-1)

print(r)