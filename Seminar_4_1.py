# 27. Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.
a = "1 2 3 45 5"
str_1 = a.split()
new_str_1 = []
for i in str_1:
    new_str_1.append(int(i))
    print(new_str_1)
print(max(new_str_1), min(new_str_1))

print()
new_str_1.sort()
print(new_str_1[-1], new_str_1[0])
