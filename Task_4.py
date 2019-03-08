"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""
import random

first_number = int(input('Веддите первое целое число: '))
second_number = int(input('Введите второе целое число: '))
if first_number > second_number:
    print(f'Случайное число из диапозона ({first_number}, {second_number}) {random.randint(first_number, second_number)}')
else:
    print(f'Случайное число из диапозона ({second_number}, {first_number}) {random.randint(second_number, first_number)}')

first_number = float(input('Веддите первое вещественное число: '))
second_number = float(input('Введите второе вещественное число: '))
print(f'Случайное число из диапозона ({first_number}, {second_number}) {random.uniform(first_number, second_number)}')

first_letter = input('Введите первый случайный символ из диапозона a-f : ')
second_letter = input('Введите второй случайный символ из диапозона a-f : ')
if ord(first_letter) >= 102 or ord(second_letter) >= 102:
    if ord(first_letter) < ord(second_letter):
        print(f'Случайное символ из диапозона ({first_letter}, {second_letter}) '
              f'{chr(random.randint(ord(first_letter), ord(second_letter)))}')
    else:
        print(f'Случайное символ из диапозона ({second_letter}, {first_letter}) '
              f'{chr(random.randint(ord(second_letter), ord(first_letter)))}')
else:
    print('Вы ввели символ не из диапозона a-f')
