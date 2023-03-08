#Транспонирование - 3
#Задана целочисленная матрица, состоящая из N строк и M столбцов. Требуется транспонировать ее относительно вертикали.

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(self.n):
            self.matrix.append([0 for _ in range(self.m)])

    def read_matrix(self):
        for i in range(self.n):
            row = list(map(int, input().split()))
            for j in range(self.m):
                self.matrix[i][j] = row[j]
        return self.matrix

    def transpose_vertically(self):
        for i in range(self.n):
            for j in range(self.m // 2):
                self.matrix[i][j], self.matrix[i][self.m - j - 1] = self.matrix[i][self.m - j - 1], self.matrix[i][j]
        return self.matrix

    def print_matrix(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.matrix[i][j], end=' ')
            print()


n, m = map(int, input().split())
matrix = Matrix(n, m)
matrix.read_matrix()
matrix.transpose_vertically()
matrix.print_matrix()

