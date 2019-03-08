"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""
length_side_a = int(input('Ведите длину стороны a: '))
length_side_b = int(input('Ведите длину стороны b: '))
length_side_c = int(input('Ведите длину стороны c: '))
print(f'Треугольник со сторонами a = {length_side_a}, b = {length_side_b}, c = {length_side_c}')
flag = False
if length_side_a > length_side_b:
    if length_side_a > length_side_c:
        if length_side_a < (length_side_c + length_side_b):
            print('Существует')
            flag = True
        else:
            print('Не существует')
    else:
        if length_side_c < (length_side_a + length_side_b):
            print('Существует')
            flag = True
        else:
            print('Не существует')
else:
    if length_side_b > length_side_c:
        if length_side_b < (length_side_c + length_side_a):
            print('Существует')
            flag = True
        else:
            print('Не существует')
    else:
        if length_side_c < (length_side_a + length_side_b):
            print('Существует')
            flag = True
        else:
            print('Не существует')

if flag:
    if length_side_a == length_side_b == length_side_c:
        print('Является равносторонним')
    elif (length_side_a == length_side_b) or (length_side_a == length_side_c) or (length_side_b == length_side_c):
        print('Является ранобедренным')
