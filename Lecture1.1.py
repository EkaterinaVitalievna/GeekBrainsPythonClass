#Ввод и вывод данных
print('Введите a')
a = input()
print("Введите b")
b = input()
print(a, b)
print (a, ' + ', b, ' = ', a+b) #по умолчанию Python работает со строками
# если требуется целое число (для математического вычисления, строка 7), перед input ставим int -> строка 9
# b = int(input())
print('{} {}'.format(a, b))
print(f'{a} {b}')