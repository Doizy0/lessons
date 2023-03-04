n = int(input())
a = list(map(int,input().split()))
f = int(input())

for i in range(f):
    k, m = map(int ,input().split())
    for j in range(k-1, m):
        print(a[j], end = ' ')
    print()




