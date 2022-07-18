import math

def Eq_degree_2(a, b, c):
    delta = b**2 - (4 * a * c)
    if delta == 0:
        
        print('X =', -b / (2 * a), "معادله درجه 2 با دلتای صفر دارای یک ریشه ی مضاعف است")
    elif delta > 0:
        print('معادله درجه 2 با دلتای مثبت دارای دو ریشه ی حقیقی است')
        print('X1 =', (-b + math.sqrt(delta)) / (2 * a))
        print('X2 =', (-b - math.sqrt(delta)) / (2 * a))
    else:
        print('No answer!! معادله درجه 2 با دلتای منفی ریشه ی حقیقی ندارد')

Eq_degree_2(4, 8, 2)
