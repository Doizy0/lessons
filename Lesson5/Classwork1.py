#Kак-то раз Шрек решил посетить казино. Не будучи заядлым любителем азартных игр, Шрек обнаружил, что он не знает правил ни одной из игр, доступных в казино. Недолго думая, Шрек решил все-таки поиграть. Его взор привлекла игра с довольно незамысловатыми правилами.

#На игровом столе лежат N карточек. На каждой карточке написано целое положительное число. Игра проходит между игроком и крупье. Карточки лежат на столе числами вниз. Игра заключается в том, что игрок открывает ровно N/2 карточек. Сумма всех чисел, написанных на карточках открытых игроком, называется “суммой игрока”. Следующим ходом крупье открывает оставшиеся N/2 карточек. Сумма всех чисел, написанных на карточках открытых крупье, называется “суммой крупье”. Выигрыш игрока определяется разностью чисел между “суммой игрока” и “суммой крупье”. Очевидно, что полученная разность может быть отрицательным числом. Это свидетельствует о том, что игрок проиграл и должен казино соответствующую сумму.

#Все бы ничего, но Шрек обладает способностью видеть надписи сквозь бумагу любой плотности. Ваша задача определить максимальную сумму выигрыша, которую может получить Шрек с учетом того, что он видит все числа, написанные на карточках.
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