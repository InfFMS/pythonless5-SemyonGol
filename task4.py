# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
s = 0
if n > 0:
    M = [randint(0, 1000)
        for i in range(0, n)]
    print(M)
    for i in range(0, n):
        s += M[i]
    s = s/n
    B = []
    for i in range(0, n):
        if M[i]*0.3 > s or M[i]*1.3 < s:
            B = B + [M[i]]
    for i in range(0, len(B)):
        M.remove(B[i])
    print(M)
else:
    print('Error: n > 0')