# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# import math
# def diff(list):
#     return [list[i] % 1 for i in range(len(list))]
# n = [1.1, 1.2, 3.1, 5, 10.01]


# print(int((max(diff(n)) - min(diff(n))) * 100) / 100)

import math

n = [1.1, 1.2, 3.1, 5, 10.01]

print(int((max([n[i] % 1 for i in range(len(n))]) - min([n[i] % 1 for i in range(len(n))])) * 100) / 100)