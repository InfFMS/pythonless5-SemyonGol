# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
b = False
if n > 0:
    A = [randint(0, 5)
         for x in range(n)]
    for i in range(1, n):
        if A[i - 1] == A[i]:
            print('Value of equal elements:', A[i],'Indexes:',i - 1, 'and', i)
            b = True
    if not(b):
        print('Нет')
    print(A)
else:
    print('Error: n > 0')