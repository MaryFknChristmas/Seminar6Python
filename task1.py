# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

a = [2, 3, 5, 9, 3, 8]

# def summa(a):
#     sum = 0
#     i = 0
#     while i < len(a):
#         if i%2 == 1:
#             sum = sum + a[i]
#             i += 1
#         else:
#             i += 1
#     print(sum)

# summa(a)

print(sum(list(filter(lambda x: x % 2 == 1, a))))
