# Задача 2: Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

N = int(input('Количество кустов черники: '))
blueberries = []
max_sum = 0

for i in range(N):
    bb = int(input(f'Количество ягод черники на кусте {i + 1}: '))
    blueberries.append(bb)

sum_1 = blueberries[N - 2] + blueberries[N - 1] + blueberries[0]  #Сначала найду сумму ягод с кустов, которые не войдут в цикл при проверке по длине цикла (так как кусты расположены по кругу)
sum_2 = blueberries[N - 1] + blueberries[0] + blueberries[1]

if sum_1 > sum_2:
    max_sum = sum_1
else:
    max_sum = sum_2

for i in range(N - 2):
    sum_bb = blueberries[i] + blueberries[i + 1] + blueberries[i + 2]
    if sum_bb > max_sum:
        max_sum = sum_bb

print(f'Максимальное число ягод: {max_sum}')
