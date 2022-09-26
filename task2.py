#Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

a = str(input('Введите число: '))
# sum = 0
# for i in a:
#     if i.isdigit():
#         sum = sum + int(i)
# print(sum)

print(sum([int(i) for i in a if i.isdigit()]))