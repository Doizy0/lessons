n = int(input())
heights = list(map(int, input().split()))
petya = int(input())


pos = n
for i in range(n):
    if heights[i] < petya:
        pos = i
        break


print(pos+1)
