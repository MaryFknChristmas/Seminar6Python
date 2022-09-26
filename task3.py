#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

a = int(input('Введите число: '))
# sum = 0
# list = [2]
# for i in range(a-1):
#     list.append((1 + (1/(i+2)))**(i+2))
# print(list)

# for i in list:
#     sum = sum+i
# print(round((sum), 3))

spis = [2]

new = [spis.append((1 + (1/(i+2)))**(i+2)) for i in range(a-1)]

print(round(sum(spis), 3))