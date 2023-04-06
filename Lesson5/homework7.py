from datetime import datetime
from calendar import monthrange


def dt_diff(start_dt: datetime, end_dt: datetime):
    total_minutes = (end_dt - start_dt).total_seconds() / 60
    number_of_days = 0
    if end_dt.month != start_dt.month:
        number_of_days = (monthrange(2023, start_dt.month)[1] - start_dt.day) + end_dt.day
    elif end_dt.day != start_dt.day:
        number_of_days = end_dt.day - start_dt.day

    to_subtract = number_of_days * 960

    return total_minutes - to_subtract + 1


days = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31}
months = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

k = int(input())
leaflets = []
for i in range(k):
    line = input()
    day_month_parts, time_parts = line.split()
    day, month = map(int, day_month_parts.split('.')[:-1])
    hour, minute = map(int, time_parts.split(':'))
    #if month in months and day in days:
        #continue
    leaflets.append(datetime(2023, month, day, hour, minute))

leaflets.sort()

total_minutes = 0

for i in range(1, len(leaflets), 2):
    end = leaflets[i]
    start = leaflets[i - 1]
    total_minutes += dt_diff(start, end)

hours = int(total_minutes // 60)
minutes = str(int(total_minutes % 60))
displayed_minutes = '0' + minutes if len(minutes) == 1 else minutes
print(hours, ':', displayed_minutes, sep='')
