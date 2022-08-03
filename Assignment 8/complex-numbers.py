def sum(x, y):
    result = {}
    result['real'] = x['real'] + y['real']
    result['unreal'] = x['unreal'] + y['unreal']
    result['i'] = 'i'
    return result
def sub(x, y):
    result = {}
    result['real'] = x['real'] - y['real']
    result['unreal'] = x['unreal'] - y['unreal']
    result['i'] = 'i'
    return result
def multiply(x,y):
    result = {}
    result['real'] = x['real'] * y['real'] - x['unreal'] * y['unreal']
    result['unreal'] = x['unreal'] * y['real'] + x['real'] * y['unreal']
    result['i'] = 'i'
    return result
def show_result(x):
    print(x['real'], ' + ', x['unreal'],x['i'])
z1 = {'real': 3, 'unreal': 2, 'i': 'i' }
z2 = {'real': 1, 'unreal': 7, 'i': 'i' }
sum_result = sum(z1, z2)
print('Sum => ', end=' ')
show_result(sum_result)
sub_result = sub(z1, z2)
print('Subtraction => ', end=' ')
show_result(sub_result)
mul_result = multiply(z1, z2)
print('Multiply => ', end=' ')
show_result(mul_result)

    
    