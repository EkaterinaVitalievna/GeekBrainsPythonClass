#Описание функции
# Функция начинается с ключевого слова def
# далее название функции
# далее в круглых скобках аргумент
# def function_name(x):

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 1
print(f(arg))
print(type(f(arg)))

print(f(1)) # Целое
print(f(2.3)) # 23
print(f(28)) # None
print(type(f(1))) # str
print(type(f(2.3))) # int
print(type(f(28))) # NoneTyp
