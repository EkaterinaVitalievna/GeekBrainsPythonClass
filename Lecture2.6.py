# Списки
list1 = [1,2,3,444,5,666,7,8]
print(len(list1))
print(list1.pop())#удаление последнего элемента
print(list1)
print(list1.pop())
print(list1)
print(list1.pop(3))#указываем какой элемент надо удалить
print(list1)
print(list.insert(2, 11))#insert добавляет позицию. 2 - указали индекс, куда добавить,
# 11 - значение, которое необходимо добавить
# оператор append добавляет значение в конец
list1[0] = 1221

list2 = list1
list2[1] = 373
for e in list1:
    print(e)
print()

for e in list2:
    print(e)
