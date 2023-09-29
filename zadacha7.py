a = int(input("Введите число - "))
b = 0

while a > 0:
    if a % 2 == 0:
        b += a % 10
    a //= 10

print(b)
