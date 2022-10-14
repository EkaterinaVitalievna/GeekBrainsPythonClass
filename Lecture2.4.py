#Словари - Неупорядоченные коллекции произвольных объектов с доступом по ключу
# В списках в качестве ключа указываем индекс, а для словаря ключ определяется при описании.
# Это может быть строка, число и т.д.
dictionary = {}# - пустой словарь
# ниже используем обратный слеш, чтобы не писать всё в одну строку
dictionary = \
{
 'up': '↑',# ключ - слева, значение - справа, ключ up, значение - стрелочка
 'left': '←',
 'down': '↓',
 'right': '→'
 }
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться

# for k in dictionary.keys(): - получить все ключи
    # print(k)

print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
 print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: 