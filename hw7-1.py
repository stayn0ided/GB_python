# Задача 1.Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.  
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

line = input().lower()
parts = line.split()
 
lst = [sum(x in 'аеиоуыэюя' for x in part) for part in parts]
if len(set(lst)) == 1:
    output = "Парам пам-пам"  
else: output = "Пам парам"
 
print(output)