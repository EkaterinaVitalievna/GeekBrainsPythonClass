# 8. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

# 1. с помощью математических формул нахождения корней квадратного уравнения
# 2. с помощью math

from operator import truediv
import math

A = float(input('Введите А '))
B = float(input('Введите B '))
C = float(input('Введите C '))
D = B ** 2 - 4 * A * C
x = 0
x1 = 0
if D == 0:
    x = -B/(2*A)
    print(f'Уравнение имеет корень = {x}')
elif D > 0:
    x1 = (-B + D ** 0.5)/(2*A)
    x = (-B - D ** 0.5)/(2*A)
    print(f'Уравнение имеет корни = {x} {x1}')
else:
    print('Уравнение не имеет корней')

D = pow(B,2) - 4 * A * C
if D == 0:
    x = -B/(2*A)
    print(f'Уравнение имеет корень = {x}')
elif D > 0:
    x1 = (-B + math.sqrt(D))/(2*A)
    x = (-B - math.sqrt(D))/(2*A)
    print(f'Уравнение имеет корни = {x} {x1}')
else:
    print('Уравнение не имеет корней')