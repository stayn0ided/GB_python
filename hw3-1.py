# Задача 1: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

n = int(input('Введите размер массива: '))
lst = []
for i in range(n):
    A = int(input('Введите число: '))
    lst.append(A)
print(lst.count(int(input('Введите число, встречаемость которого хотите узнать: '))))