class Table:
    def __init__(self, t):
        self.t = t
        self.tables = []

    def read_table(self):
        for i in range(self.t):
            n, m = map(int, input().split())
            table = []
            for j in range(n):
                row = list(map(int, input().split()))
                table.append(row)
            self.tables.append(table)

    def is_table_sympathetic(self, table):
        n, m = len(table), len(table[0])
        for i in range(n - 1):
            for j in range(m - 1):
                if table[i][j] == table[i + 1][j] == table[i][j + 1] == table[i + 1][j + 1]:
                    return False
        return True


t = int(input())
table = Table(t)
table.read_table()
for i in range(t):
    if table.is_table_sympathetic(table.tables[i]):
        print("YES")
    else:
        print("NO")
