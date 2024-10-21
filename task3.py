# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
b = False
if n > 0:
    M = [randint(0, 100)
         for i in range(n)]
    for i in range(0, n - 1):
        for o in range(i + 1, n):
            if M[i] == M[o]:
                print('Value of equal elements:', M[i], 'Indexes:', i, 'and', o)
                b = True
    if not(b):
        print("Нет")
    print(M)