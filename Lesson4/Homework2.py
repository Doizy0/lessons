#Произведение матриц
#Заданы две целочисленные матрицы A и B. Матрица A состоит из N строк и M столбцов, Матрица B состоит из M строк и P столбцов. Требуется вычислить произведение данных матриц A*B.




n, m, p = map(int, input().split())


a = []
for i in range(n):
    row1 = list(map(int, input().split()))
    for j in range(m):
        a[i][j] = row1[j]


b = []
for i in range(m):
    row2 = list(map(int, input().split()))
    for j in range(p):
        b[i][j] =row2[j]

c = []
for i in range(n):
    row3 = []
    for j in range(p):

        sum = 0
        for k in range(m):
            sum += a[i][k] * b[k][j]
        row3.append(sum)
    c.append(row3)

