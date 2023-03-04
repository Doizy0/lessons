
n = int(input())
berries = list(map(int, input().split()))


max_sum = 0
curr_sum = 0


for i in range(n):

    curr_sum = berries[i] + berries[(i+1)%n] + berries[(i+2)%n]

    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)