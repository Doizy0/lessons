# Одна предприимчивая и очень симпатичная дамочка с прелестнейшим именем Горгона решила заработать себе денег на роскошную жизнь. N молодых людей так влюблены в нее, что предложили руку и сердце. К несчастью для них, Горгона видит в них только мешок с деньгами. Она планирует выйти замуж и почти сразу же развестись с некоторыми из молодых людей ради денежной выгоды. Все, что ей нужно, это подзаработать как можно больше денег (и уж, конечно, остаться незамужней). По законам этой прекрасной страны при разводе каждый из супругов получает половину всего имущества.

# Вы планируете опубликовать статью, в которой опишете всю подлость и меркантильность этой особы. Для того чтобы статья получилась особенно красочной, нужно указать максимальную сумму денег, которую сможет получить Горгона.
# https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=731
def money(n, array):
    cnt = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    for i in range(len(array)):
        cnt = (array[i] + n) / 2
        n = cnt

    return cnt


n = int(input())
a = list(map(int, input().split()))
g = int(input())
print(money(g, a))
