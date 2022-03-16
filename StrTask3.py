# Базовые операции.
# Уравнение прямой вида y = kx + b задано в виде строки. Определить координату y точки с заданной координатой x.

EQUATION = 'y = -12x + 11111140.2121'
x = 2.5
NAME = equation.split(' ')
print(NAME)
first_name = str(NAME[2])
NAME[2] = first_name[:-1]
print(NAME[2])
two_name = float(NAME[2]) * x + float(NAME[4])
print('y =', two_name)
