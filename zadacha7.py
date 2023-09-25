n = int(input('Введите ваше число-  '))
summa = 0
if n > 0:
        for i in str(n):
            if int(i) % 2 == 0:
                summa += int(i)
        print(f"получается = {summa}")
else:
        print("неправильное число")
