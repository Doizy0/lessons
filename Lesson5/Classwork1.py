
#https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=730
def bubble_sort(array):
    cnt = 0
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                cnt += 1
    return cnt


def selection_sort(array):
    for i in range(len(array) - 1, -1, -1):
        sub_array = array[:i + 1]
        max_elem = min(sub_array)
        idx = sub_array.index(max_elem)

        array[i], array[idx] = array[idx], array[i]

    n = sum(array[len(array)//2:])
    n1 = sum(array[:len(array//2)])

    max_win = n-n1
    return max_win

n = int(input())
a = list(map(int, input().split()))
print(selection_sort(a))