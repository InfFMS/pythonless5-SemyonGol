# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
s = 0
if n > 0:
    M = [randint(0, 100)
        for i in range(0, n)]
    print(M)
    for i in range(1, n):
        if M[i-1] < M[i]:
            m = M[i]
        else:
            m = M[0]
    for i in range(0, n):
        if M[i] == m:
            s +=1
    print(s)