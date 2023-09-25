n = input('введите ваше число- ')
 
suma = 0
mult = 1
 
for i in n:
    suma += int(i)
    mult *= int(i)
 
print (f'сумма равняется:  {suma}')
print (f'произведение будет равно:  {mult}')
