# Задача 1: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

n = int(input('Введите длину первого списка чисел: '))
m = int(input('Введите длину второго списка чисел: '))

list_n = []
list_m = []

for i in range(n):
    num_n = int(input('Введите элемент первого списка: '))
    list_n.append(num_n)

for i in range(m):
    num_m = int(input('Введите элемент второго списка: '))
    list_m.append(num_m)

list_nm = []

for i in range(len(list_n)):
    if list_n[i] in list_m:
        list_nm.append(list_n[i])

list_nm.sort()
print(*set(list_nm))
