# line = ""
# for i in range(5):
#  line = ""
#  for j in range(5):
#  line += "*"
#  print(line)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # len - узнать количество символов в строке (39)
# print('ещё' in text) # проверить наличие подстроки в строке (True)
# print(text.isdigit()) # пров-ть явл. ли все символы в строке числами (False)
# print(text.islower()) # пров-ть явл. ли все символы в строке строчными (нижн.регистра)(True)
# print(text.replace('ещё','ЕЩЁ')) # заменить и указываем что и на что
# for c in text:
#  print(c)

#help(int)#встроенная справка языка python

text = 'съешь ещё этих мягких французских булок'
print(text[0]) # c
print(text[1]) # ъ
#print(text[len(text)] ОШИБКА, т.к.индексация с 0
print(text[len(text)-1]) # к
print(text[-5]) # т.к. индексация с 0, то последний символ строки это i-1,
#а -5 - это б ('б' улок)
print(text[:]) # если просто :, то по умолчанию print(text[0:len(text)-1]), то есть
# от первого до последнего символа print(text)
print(text[:2]) # от 0 до 2-го символа - съ. Если перед : указать значение символа,
#то будет от этого символа
print(text[len(text)-2:]) # ок
print(text[2:9]) # ешь ещё
print(text[6:-18]) # ещё этих мягких
print(text[0:len(text):6]) # сеикакл
print(text[::6]) # сеикакл
text = text[2:9] + text[-5] + text[:2] # ...

numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
ran = range(1,6)
print(type(ran))
numbers = list(ran)
print(type(numbers))
numbers = list(range(1, 6))
print(numbers) # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')# интерполяция
print(numbers) # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2#в текущую переменную кладём новое значение, не в список
 print(i) # [20, 4, 6, 8, 10]
print(numbers) # [10, 2, 3, 4, 5

colors = ['red', 'green', 'blue']
for e in colors:
 print(e) # red green blue
for e in colors:
 print(e*2) # redred greengreen blueblue
colors.append('gray') # добавить в конец списка
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red') #del colors[0] # удалить элемент
del colors [0]