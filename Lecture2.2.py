# Функции
# import Lecture1.6.function / указывая оператор import далее указываем название файла,
# из которого импортируем данные. НАЗВАНИЕ ФАЙЛОВ НЕЛЬЗЯ УКАЗЫВАТЬ С ТОЧКАМИ?

# import hello
# import hello as h - присвоили названию файла название h,
# чтобы короче дальше писать было
# print(hello.f(1))
# print(h.f(1))

def new_string(symbol, count): #задаём функцию new_string с некоторым символом и некоторым числом
 return symbol * count # возвращаем символ умноженный на число

print(new_string('!', 5)) # !!!!!
print(new_string('!')) # TypeError missing 1 required ..

def new_string(symbol, count=3): #задаём функцию new_string с некоторым символом и некоторым числом
 return symbol * count # возвращаем символ умноженный на число
print(new_string('!', 5)) # !!!!!
print(new_string('!'))
print(new_string(4))# python распознаёт тип данных в момент вызова функции, т.е.
# прописывая 4, 4 будет умножаться на 3 (count=3)

def concatenatio(*params):
 res: str = ""#переменная двоеточие и тип данных str, НО указание типа не обязательно
 for item in params:
    res += item
 return res
print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ..

