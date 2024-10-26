# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
#[9, 9, 9]
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
if n > 0:
    M = [randint(1, 10)
         for x in range(0, n)]
    B = []
    print(M)
    for i in range(0, n - 1):
        for o in range(i + 1, n):
            if M[i] == M[o]:
                B = B + [M[o]]
    print(B)
    for i in range(0, len(B)):
        M.remove(B[i])
    print(M)