#Управляющие конструкции while и for - убирают рутинные действия
original = 125
inverted = 0
while original != 0:# origin не равен нулю
 inverted = inverted * 10 + (original % 10)
 original //= 10
print(inverted)
print('Далее')

original = 23
inverted = 0
while original != 0:
 inverted = inverted * 10 + (original % 10)
 original //= 10
else:
 print('Пожалуй')
 print('хватит )')
print(inverted)
print('Далее')

for i in 1,2,3,4,5:
    print(i**2)
print('Далее')

#for i in 1, 2, 3, 4, 5:
list = [1,2,3,4,10,5]
for i in list:
    print (i)
print('Далее')

#for i in range(10) чтобы не писать отдел.перемен.как ниже
r = range(10)
for i in r:
    print (i)
print('Далее')

for y in range(0, 31, 5):#от 0, но до 30 НЕ включительно!
    #первый аргумент-от какого числа, второй-до какого,
    # трети-приращение, т.е. шаг увеличения
    print (y)
print('Далее')

for t in 'qwe - rty':
    print(t)


