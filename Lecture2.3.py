# Рекурсия и Кортежи
# Рекурсия - функция, вызывающая саму себя. Важно указать, в какой момент необходимо остановиться
# и перестать её вызывать
def fib(n): # def-указали, что это функция, fib-название функции, (n)-аргумент функции
    #вычисление чисел фибоначи
    if n in [1, 2]:# логика выхода из выполнения функции
    #если попали в первый элемент, возвращаем единицу, если попали
    # во второй элемент тоже возвращаем единицу
        return 1
    else:
        return fib(n-1) + fib(n-2)#иначе - возвращаем рекурсивный вызов для n-1 и n-2
list = []
for e in range(1, 10):
 list.append(fib(e))
print(list) # 1 1 2 3 5 8 13 21 34

# Кортежи - неизменяемые списки. Для обозначения список берётся в круглые скобки
t = tuple(['red', 'green', 'blue'])
print(t[0]) # red
print(t[2]) # blue
# print(t[10]) # IndexError: tuple index out of range
print(t[-2]) # green
# print(t[-200]) # IndexError: tuple index out of range
for e in t:
 print(e) # red green blue
t[0] = 'black' # TypeError: 'tuple' object does not support 
# item assignmen
#a = (3) - число
#a = (3,) - кортеж
