# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
from random import randint
print('Enter length of massive:', end=' ')
n = int(input())
if n > 0:
    A = [randint(0, 1000) for x in range(n)]
    b = False

    print(n)
    print(A[-1])
    print(A[::-1])
    for i in range(0, n):
        if A[i]%10 == (A[i]%100)//10 == (A[i]%1000)//100:
            print('YES')
            b = True
    if not(b):
        print('NO')
    if n > 1:
        A.pop(n - 1)
        A.pop(0)
        print(A)
    else:
        A.pop(0)
        print(A)
else:
    print('Error: n > 0')