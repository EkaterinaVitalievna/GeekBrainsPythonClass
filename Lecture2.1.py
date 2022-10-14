# файлы
# первый способ работы с файлами
with open('file.txt', 'w') as data: #as data=указываем, что конструкцию with open('file.txt', 'w')
# необходимо воспринимать как переменную data
 data.write('line 1\n')
 data.write('\nline 2\n')
 # при таком способе закрытие файла происходит автоматически без команды data.close()

 # второй способ работы с файлами
colors = ['red', 'green', 'blue'] # источник данных - список
data = open('file.txt', 'a') # задаём переменную data и связываем её с текстовым файлом 'file.text'
# и задаём режим работы с файлом'a'
data.writelines(colors) # разделителей не будет||writelines(colors)-запись набора данных color,
#color - аргумент
data.write('\nLine 12\n')
data.write('LINE 31\n')
data.close() #разрыв соединения с файлом на диске во избежание утечек памяти

# чтение файла
path = 'file.txt'
data = open(path, 'r')
for line in data: 
 print(line)
data.close()




exit()#оператор, позволяющий не выполнять код введённый ниже
path = 'file.txt'
data = open(path, 'r')
for line in data: 
 print(line)
data.close()