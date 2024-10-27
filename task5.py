# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
s = 0
if n > 0:
    M = [randint(1, 100)
         for x in range(0, n)]
    m = max(M)
    for i in range(0, n):
        if m == M[i]:
            s += 1
    print(M, m, s)
else:
    print('Error: n > 0')