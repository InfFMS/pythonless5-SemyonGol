# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
#777 => a=7
def rep(n):
    n = abs(n)
    a = n%10
    if n//10 > 0:
        if a == (n//10)%10:
            return rep(n//10)
        else:
            return False
    else:
        return True
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
if n > 0:
    M = [randint(10, 100000)
         for x in range(0, n)]
    M1 = []
    for i in range(0, n):
        if rep(M[i]):
            M1.append(M[i])
    print(M1)
else:
    print('Error, n > 0')