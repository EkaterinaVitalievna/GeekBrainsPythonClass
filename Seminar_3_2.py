# 20. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
n = int(input ("Введите искомое в строке число: "))
my_list = ["err567", "iu5", "rtu456t", "ffg567"]
length = len(my_list)
n = str(n)
Flag = False
for i in range (length):
    if my_list[i].find(n) != -1:
        Flag = True
        break
print (Flag)

lst = ['err567', 'iu5', 'rtu456t', 'ffg567']
num = int(input('Введите искомое в строке число: '))
count = 0
for elem in lst:
    if str(num) in elem:
        count += 1
if count > 0:
    print ("Да, такое число в строке есть")
else:
    print ("Указанное число в строке отсутствует")

