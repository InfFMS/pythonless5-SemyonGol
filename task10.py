# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90
from math import acos, pi
A = B = []
s = l1 = l2 = 0
print('Enter dimension of vectors:', end=' ')
d = int(input())
print('Enter coordinates of first vector:')
for i in range(0, d):
    A = A + [int(input())]
print('Enter coordinates of second vector:')
for i in range(0, d):
    B = B + [int(input())]
    s += A[i] * B[i]
for i in range(0, d):
    l1 += A[i]**2
    l2 += B[i]**2
print('Angle between two vectors:', acos(s/((l1**0.5)*(l2**0.5)))/(pi)*180)
                                    #сразу считает скалярное произведение, находит
                                    #косинус угла, переводит его в рад. и переводит
                                    #рад в градусы