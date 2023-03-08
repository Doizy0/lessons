#Произведение матриц
#Заданы две целочисленные матрицы A и B. Матрица A состоит из N строк и M столбцов, Матрица B состоит из M строк и P столбцов. Требуется вычислить произведение данных матриц A*B.
n, m, p = map(int, input().split())
for i in range(n):
    a = list(map(int, input().split()))
input()
for i in range(m):
    b = list(map(int, input().split()))


c = [[0 for j in range(p)] for i in range(n)]
for i in range(n):
    for j in range(p):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]


print(c)