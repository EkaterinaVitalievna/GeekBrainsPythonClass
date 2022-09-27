# Математические операции
# унарный минус (инверсия числа: число со знаком -, напр. -321),
# унарный плюс (классическая запись числа, но с +. Напр.: +321)
# +, -, *, /, %, //, **
# // - результат деления в целых числах. Например, 12/8=1 (а не 1,5)
# % - остаток от деления
# ** - возведение в степень. Напр.: 2 ** 8 = 256
# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# () меняют приоритет
# ВАЖНО! В Python для десятичных чисел не "," а "."
a = 123
b = -321
c = a + b
print(c)
v = 2
d = 8
t = v ** d
print(t)
k = 1.323454
m = 3
# n = g * u
## если просто умножить 1,3 на 3, появится остаток
## для округления используется функция Round
n = round(k * m, 3)
print(n)

f = 5
f = f + 7
## f = f + 7 тоже самое, что f += 5
f += 5

## Логические операции
## >, >=, <, <=, ==, !=
## not, and, or – не путать с &, |, ^
# is, is not, in, not i - python функционал
h = 1 < 4 and 5 > 2
h = 1 == 2
h = 1 != 2
print (h)

# сравнение строк
s = 'qwe'
p = 'qwe'
print (s==b)

# сравнение списков: элементы сравниваются поэлементно
q = [1,2]
w = [2,3]

# возможны тройные неравенства
u = 2
i = 5
o = 9
u < i < o

func = 1
R = 4
y = 2
print (func<R>(y))

j = 1 > 2 or 4 < 6 # дизъюнкция
print (j)
# выводится True

e = [1,2,3,4]
print (e)
print(2 in e) # вывод True
print (not 2 in e) # вывод False

# проверить факт чётности числа
is_odd = e[0] % 2 == 0 # где e[0]-нулевой элемент в списке (см.выше)
# проверка выражения: остаток от деление на 2 = 0, вывод false
# ещё один вариант записи
is_odd = not e[0] % 2 # вывод false
print (is_odd)
