#вывести квадрат числа
number = int(input('Введите число: '))
#print(type(number))
print('Квадрат числа {} равен {}'.format(number, number**2, end=' ')) #end не обязателен, др. вывод строки
print(f'Квадрат числа {number} равен {number**2}')
print('Квадрат числа', number, 'равен', number**2)