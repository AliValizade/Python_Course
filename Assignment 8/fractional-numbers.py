def sum(x, y):
    result = {}
    result['s'] = x['s'] * y['m'] + y['s'] * x['m']
    result['m'] = x['m'] * y['m']
    return result
def sub(x, y):
    result = {}
    result['s'] = x['s'] * y['m'] - y['s'] * x['m']
    result['m'] = x['m'] * y['m']
    return result
def multiply(x, y):
    result = {}
    result['s'] = x['s'] * y['s']
    result['m'] = x['m'] * y['m']
    return result
def division(x, y):
    result = {}
    result['s'] = x['s'] * y['m']
    result['m'] = x['m'] * y['s']
    return result
def show_result(x):
    print(x['s'],'/',x['m'])
    
f1 = {'s': 5, 'm': 7}
f2 = {'s': 3, 'm': 5}
sum = sum(f1, f2)
print('Sum => ', end=' ')
show_result(sum)
sub = sub(f1, f2)
print('Subtraction => ', end=' ')
show_result(sub)
multiply = multiply(f1, f2)
print('Multiply => ', end=' ')
show_result(multiply)
division = division(f1, f2)
print('Division => ', end=' ')
show_result(division)

    
    
    