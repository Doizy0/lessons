a = input()
b = input()

sign_a = '+' if a[0].isdigit() else '-'
sign_b = '+' if b[0].isdigit() else '-'

num_a = list(map(int, (' '.join(a if sign_a == '+' else a[1:])).split()))
num_b = list(map(int, (' '.join(b if sign_b == '+' else b[1:])).split()))


def sort_digits_in_num(num, reverse=False):
    num = sorted(num, reverse=reverse)
    if not reverse:
        # 1000123456
        cnt = 0
        for n in num:
            if n == 0:
                cnt += 1
            else:
                break

        num = [num[cnt]] + num[0:cnt] + (num[cnt + 1:] if len(num) > cnt + 1 else [])

    return [str(n) for n in num]


transformed_a = int(''.join(sort_digits_in_num(num_a, sign_a == '+'))) * (-1 if sign_a == '-' else 1)
transformed_b = int(''.join(sort_digits_in_num(num_b, sign_b == '-'))) * (-1 if sign_b == '-' else 1)
print(transformed_a - transformed_b)

