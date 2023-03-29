def sort(array, reverse=True):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array



def to_grams(weight):
    grams = 0
    i = 0
    while i < len(weight) and weight[i].isdigit():
        i += 1
    number = float(weight[:i])
    unit = weight[i:].strip()
    if unit == 'mg':
        grams = number * 0.001
    elif unit == 'g':
        grams = number
    elif unit == 'kg':
        grams = number * 1000
    elif unit == 't':
        grams = number * 1000000
    elif unit == 'mp':
        grams = number * 16.38
    elif unit == 'p':
        grams = number * 16380
    elif unit == 'M':
        grams = number * 16380000
    elif unit == 'G':
        grams = number * 16380000000
    return grams


n = int(input())
weights = []
for i in range(n):
    weight = input().strip()
    grams = to_grams(weight)
    weights.append((grams, weight))

sort(weights)

for weight_tuple in weights:
    print(weight_tuple[1])
