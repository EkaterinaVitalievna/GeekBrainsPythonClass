# 19.	Реализуйте алгоритм задания случайных чисел без использования
# встроенного генератора псевдослучайных чисел
# изучаем Слеповичев И.И. "Генератор псевдослучайных чисел"

c = 9
a = 8
b = 3
x = 7
m = 10

list = [x]

for i in range(c):
    x = (a * x + b) % m
    list.append(x)

print(list)

# второе решение

import time
number = time.time()
print(number)
def Random_Set(start = 0, end = 1):
    number = time.time()
    Next = True
    while Next:
        Rand = end * (number % 1)#берём остаток от деления
        if Rand >= start or Rand > end: Next = False

    return int(Rand)

print(Random_Set(1,1000))