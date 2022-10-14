# Для натурального n создать список, состоящий из элементов последовательности
# 3n + 1.
# Пример:
# o Для n = 6: [4, 7, 10, 13, 16, 19]
numbers = []
count = int(input("Введите число, обозначающее длину списка: "))
for i in range (1, count + 1):
    numbers.append (3 * i + 1)
print(numbers)

num = int(input('Введите число D: '))
list = []
for i in range(1, num +1):
    element = 3*i+1
    list.append(element)
print(list)
