# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.

first_point_x = int(input('Ввдите координату x первой точки: '))
first_point_y = int(input('Ввдите координату y первой точки: '))
second_point_x = int(input('Введите координату x второй точки: '))
second_point_y = int(input('Введите координату y второй точки: '))
k = (first_point_y - second_point_y) / (first_point_x - second_point_x)
b = second_point_y - second_point_x * k
print(f'Уравнение прямой будет иметь следующий вид: y = {k}x + {b}')