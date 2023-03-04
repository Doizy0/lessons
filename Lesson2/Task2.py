import sys

sys.setrecursionlimit(10000000)
import functools


@functools.cache
def formula(s):
    if s.isdigit():
        return int(s)
    else:
        expression = s[2:-1].split(',', 1)
        res1 = formula(expression[0])
        res2 = formula(expression[1])

        if s[0] == 'M':
            return max(res1, res2)
        if s[0] == 'm':
            return min(res1, res2)


s = input()
print(formula(s))
