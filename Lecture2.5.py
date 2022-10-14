# Множества
# Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8} одно множество
# b = {'2', '5', 8, 13, 21} второе множество
# print(type(a)) # set
# print(type(b)) # set

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}

exit()
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red')#удаление элемента. Если укажем несуществующий элемент - будет ошибка
print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok удаление значений без ошибки (если нет значения, ошибки не будет)
print(colors) # {'green', 'blue','gray'}
colors.clear() # { } - очистка множеств, работа "с чистого листа"
print(colors) # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} объединение множеств
i = a.intersection(b) # i = {8, 2, 5} пересечение множеств
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a \
 .union(b) \
 .difference(a.intersection(b))
# {1, 21, 3, 13}

# Неизменяемые множества
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
