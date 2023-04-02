
k = int(input())
leaflets = []
for i in range(k):
    line = input()
    if not line:
        continue
    day_month_parts, time_parts = line.split()
    if not day_month_parts:
        continue
    day, month = map(int, day_month_parts.split('.'))
    hour, minute = map(int, time_parts.split(':'))
    leaflets.append((day, month, hour, minute))

leaflets.sort()

total_work_time = 0
current_case_start_time = None
for day, month, hour, minute, leaflet_type in leaflets:
    dt = (day, month, hour, minute)
    if leaflet_type == 0:

        current_case_start_time = dt
    else:

        case_duration = ((day - current_case_start_time[0]) * 1440 +
                         (month - current_case_start_time[1]) * 43200 +
                         (hour - current_case_start_time[2]) * 60 +
                         (minute - current_case_start_time[3]))
        if current_case_start_time[2] < 10:
            current_case_start_time = (current_case_start_time[0], current_case_start_time[1], 10, 0)
        if hour > 18 or (hour == 18 and minute > 0):
            dt = (day, month, 18, 0)
        if current_case_start_time[0] % 4 == 0:

            work_time = case_duration / 527040
        else:

            work_time = case_duration / 525600
        total_work_time += work_time

hours = int(total_work_time * 24)
minutes = int((total_work_time * 24 * 60) % 60)
print(hours+':'+minutes)
