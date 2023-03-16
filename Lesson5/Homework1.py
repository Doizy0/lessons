#Требуется выполнить сортировку временных моментов, заданных в часах, минутах и секундах.
#https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=728
n = int(input())
times = []
for i in range(n):
    h, m, s = map(int, input().split())
    times.append((h, m, s))

for i in range(n):
    key = times[i]
    j = i - 1
    while j >= 0 and times[j] > key:
        times[j + 1] = times[j]
        j -= 1
    times[j + 1] = key

for time in times:
    print(times)

