

def to_grams(weight):
    ratio = {
        'g': 1,
        'p': 16380,
        't': 10 ** 6

    }
    prefix = {
        'm': 0.001,
        'k': 10 ** 3,
        'M': 10 ** 6,
        'G': 10 ** 9
    }
    num, unit = weight.split()
    total_unit = ' '.join(unit).split()
    sub_unit = None
    if len(total_unit) == 1:
        main_unit = total_unit[0]
    else:
        sub_unit, main_unit = total_unit

    return int(num) * ratio[main_unit] * (prefix[sub_unit] if sub_unit else 1)


n = int(input())
weights = []
for i in range(n):
    weight = input()
    weights.append(weight)

sorted_weights = sorted(weights, key=to_grams)

print(*sorted_weights, sep='\n')

#
# 32 mg
# 234 g
# 4576 mp
# 2 t
# 2 Mg
