# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
nul = 0
if n > 0:
    M = [randint(-100, 100)
         for x in range(0, n)]
    M1 = []
    print(M)
    for i in range(0, n):
        if M[i] > 0:
            M1.append(M[i])
        if M[i] == 0:
            nul += 1
    for i in range(0, n):
        if M[i] < 0:
            M1.append(M[i])
    for x in range(0, nul):
        M1.append(0)
    print(M1)
else:
    print('Error: n > 0')