n = int(input("Введите число - "))

a = 0
b = 1

while n > 0:
    d = n % 10
    a = a + d
    b = b * d
    n = n // 10

print("Сумма:", a)
print("Произведение:", b)
