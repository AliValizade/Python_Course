a = int(input('Plz enter number1: '))
b = int(input('Plz enter number2: '))

#--------------first method: without function----------------
# for i in range(1, a + 1):
#     if a % i == 0:
#         mma = a / i
#     for j in range(1, b + 1):
#         if b % j == 0:
#             mmb = b / j
#         if mmb == mma:
#             break
#     if mmb == mma:
#         print('B.m.m(a, b) =', mmb)
#         break

#--------------second method: with function------------------

def b_m_m(a, b):
    if a >= b:
        bmm = b
    else:
        bmm = a
    for i in range(bmm):
        if a % bmm == 0 and b % bmm == 0:
            print('B.m.m(a, b) =', bmm)
            break
        else:
            bmm -= 1
            if a % bmm == 0 and b % bmm == 0:
                print('B.m.m(a, b) =', bmm)
                break

b_m_m(a, b)


