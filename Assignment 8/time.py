def sum_times(x, y):
    result = {}
    result['h'] = x['h'] + y['h']
    result['m'] = x['m'] + y['m']
    result['s'] = x['s'] + y['s']
    if result['s'] > 59:
        result['s'] -= 60
        result['m'] += 1
    if result['m'] > 59:
        result['m'] -= 60
        result['h'] += 1
    return result
def sub_times(x, y):
    result = {}
    result['h'] = x['h'] - y['h']
    result['m'] = x['m'] - y['m']
    result['s'] = x['s'] - y['s']
    if result['m'] < 0:
        result['h'] -= 1
        result['m'] += 60
    if result['s'] < 0:
        result['m'] -= 1
        result['s'] += 60
    return result
def show_time(x):
    print(x['h'],':',x['m'],':',x['s'])
def time_to_second(x):
    seconds = x['h'] * 3600 + x['m'] * 60 + x['s']
    print('Seconds => ', seconds, '\n__________________')
def second_to_time(x):
    result = {}
    result['h'] = int(second / 3600)
    result['m'] = int((second % 3600) / 60)
    result['s'] = second % 60
    return result

second = int(input('Plz enter seconds (for convert to time): '))
result = second_to_time(second)
print('Convert second to time => ', end='')
show_time(result)
t1 = {'h': int(input('Plz enter hours (t1): ')), 'm': int(input('Plz enter minutes (t1): ')), 's': int(input('Plz enter seconds (t1): '))}
print('T1 => ', end='')
show_time(t1)
time_to_second(t1)
t2 = {'h': int(input('Plz enter hours (t2): ')), 'm': int(input('Plz enter minutes (t2): ')), 's': int(input('Plz enter seconds (t2): '))}
print('T2 => ', end='')
show_time(t2)
time_to_second(t2)
sum_result = sum_times(t1, t2)
print('Result of sum times => ✅', end=' ')
show_time(sum_result)
time_to_second(sum_result)
sub_result = sub_times(t1, t2)
print('Result of sub times => ✅', end=' ')
show_time(sub_result)
time_to_second(sub_result)