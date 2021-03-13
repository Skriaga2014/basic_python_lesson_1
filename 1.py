duration_test = 0
while duration_test == 0:
    durations_right = []
    durations_list = input('Enter duration (one or list):')
    durations_list = durations_list.replace(' ', '')
    durations_list = durations_list.split(',')
    error_count = 0
    for dur in durations_list:
        if dur.isdigit() == False:
            print('Durations may be digits only. Try again.')
            error_count += 1
            break
        durations_right.append(int(dur))
    if error_count == 0:
        duration_test = 1

for duration in durations_right:
    secs_in_day = 24 * 60 * 60
    secs_in_hour = 60 * 60
    secs_in_minute = 60

    days = duration // secs_in_day
    hours = (duration - days * secs_in_day) // secs_in_hour
    minutes = (duration - days * secs_in_day - hours * secs_in_hour) // secs_in_minute
    seconds = (duration - days * secs_in_day - hours * secs_in_hour - minutes * secs_in_minute)

    result_txt = f'In {duration} secs: '
    result_list = [days, hours, minutes, seconds]
    result_list_items = ['days', 'hours', 'minutes', 'seconds']

    for i in range(len(result_list)):
        if result_list[i] != 0:
            result_txt += f'{result_list[i]} {result_list_items[i]}, '

    if result_txt[-1] == ' ':
        result_txt = result_txt[:-2]

    print(result_txt)

