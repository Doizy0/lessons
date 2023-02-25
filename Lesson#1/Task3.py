class MatrixGame:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = []
        for i in range(self.n):
            self.matrix.append([0 for _ in range(self.m)])



    def read_matrix(self):
        for i in range(self.n):
            self.matrix[i] = [int(num) for num in input().split()]

    def lower_value(self):
        d = 0
        lower_values = []
        for i in range(self.n):

            lower_values.append(min(self.matrix[i]))
        return max(lower_values)
    def upper_value(self):
        k = 0
        upper_values = []
        for i in range(self.n):
            for j in range(self.m):
                k = self.matrix[i][j]
                upper_values.append(max(k))
        return min(upper_values)





n, m = map(int, input().split())


game = MatrixGame(n, m)
print(game.lower_value(), game.upper_value())
