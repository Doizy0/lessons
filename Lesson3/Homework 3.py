n, a, b, c, d = map(int, input().split())

seq = list(range(1, n + 1))

for i in range((b - a + 1) // 2):
    seq[a + i - 1], seq[b - i - 1] = seq[b - i - 1], seq[a + i - 1]

for i in range((d - c + 1) // 2):
    seq[c + i - 1], seq[d - i - 1] = seq[d - i - 1], seq[c + i - 1]

print(*seq)
