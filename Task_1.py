# 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = int(input('Введите трехзначное число: '))
res_sum = f'Сумма цифр введенного числа равна: {number % 10 + (number // 10) % 10 + number // 100}'
res_mull = f'Произведе цифр введенного числа равно: {(number % 10) * ((number // 10) % 10) * (number // 100)}'
print(f'{res_sum}\n{res_mull}')
