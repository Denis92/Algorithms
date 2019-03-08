# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
third_number = int(input('Введите третье число: '))
print('Средним является следующее число: ')
if (first_number >= second_number) and (first_number >= third_number):
    if second_number > third_number:
        print(second_number)
    else:
        print(third_number)

elif (second_number >= first_number) and (second_number >= third_number):
    if first_number > third_number:
        print(first_number)
    else:
        print(third_number)

else:
    if first_number > second_number:
        print(first_number)
    else:
        print(second_number)
