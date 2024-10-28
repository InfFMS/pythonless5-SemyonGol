# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint
print('Enter even length of massive:', end=' ')
n = int(input())
if n%2 == 1:
    print('Length of massive is need to be even!')
if n > 0 and n%2 == 0:
    M = [randint(1, 100)
         for x in range(0, n)]
    print(M)
    M1 = []
    M2 = []
    for i in range(0, n//2):
        M1.append(M[i])
    M1.reverse()
    for i in range(n//2, n):
        M2.append(M[i])
    M2.reverse()
    M = M1 + M2
    print(M)
else:
    print('Error: n > 0')