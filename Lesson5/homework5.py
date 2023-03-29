def sort(array, reverse=True):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def max_profit(a, b):
    a_digits = list(str(a))
    b_digits = list(str(b))

    sort(a_digits, reverse=True)
    sort(b_digits, reverse=True)

    i = 0
    while i < len(a_digits) and a_digits[i] == 0:
        i += 1
    if i == len(a_digits):
        return -b

    j = 0
    while j < len(b_digits) and b_digits[j] >= a_digits[i]:
        j += 1
    a_digits[i], b_digits[j - 1] = b_digits[j - 1], a_digits[i]

    a_sorted = int(''.join(str(d) for d in a_digits))
    b_sorted = int(''.join(str(d) for d in b_digits))


    max_diff = a_sorted - b_sorted

    return max_diff


a = int(input())
b = int(input())
max_diff = max_profit(a, b)
print(max_diff)
