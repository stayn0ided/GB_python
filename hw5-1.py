# Задача 1. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(base, exp):
    if exp == 1:
        return base
    else:
        return (base * power(base, exp - 1))
    
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

print(power(A, B))