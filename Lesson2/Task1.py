# def fib(n):
# if n == 1:
# return 1
# if n == 2:
# return 2

# return fib(n - 1) + fib(n - 2)


# print(fib(5))

import sys
sys.setrecursionlimit(10000)

n = int(input())
numbers = list(map(int, input().split()))


def recur(n, numbers):
    if n == 0:
        return
    print(numbers[n - 1], end=' ')
    recur(n - 1, numbers)

recur(n, numbers)