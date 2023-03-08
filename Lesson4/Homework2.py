#Произведение матриц
#Заданы две целочисленные матрицы A и B. Матрица A состоит из N строк и M столбцов, Матрица B состоит из M строк и P столбцов. Требуется вычислить произведение данных матриц A*B.




n, m, p = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

input()

b = []
for i in range(m):
    b.append(list(map(int, input().split())))

#  2  3    2 -3  4
# -1  4    3  1  0    13 -3 8


c = []
for i in range(n):
    row3 = []
    for j in range(p):
        summ = 0
        for k in range(m):
            summ += a[i][k] * b[k][j]
        row3.append(summ)
    c.append(row3)

for i in range(n):
    for j in range(p):
        print(c[i][j], end=' ')
    print()