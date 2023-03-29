
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=731
def money(capital, array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    for partner_capital in array:
        if capital >= partner_capital:
            continue
        capital = (partner_capital + capital) / 2
    return capital


n = int(input())
a = list(map(int, input().split()))
g = int(input())
print(f'{money(g, a):.6f}')