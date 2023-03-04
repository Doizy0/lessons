n = int(input())
a = list(map(int,input().split()))


min_idx = 0

for i in range(n):
    if a[i] < a[min_idx]:
        min_idx = i

for i in range(min_idx, n):
    print(a[i], end=' ')
for i in range(min_idx):
    print(a[i], end=' ')