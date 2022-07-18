a = int(input('Plz enter number1: '))
b = int(input('Plz enter number2: '))

#--------------first method: without function----------------
# for i in range(1, (a * b) + 1):
#     mma = a * i
#     for j in range(1, (a * b) + 1):
#         mmb = b * j
#         if mmb == mma:
#             break
#     if mmb == mma:
#         print('K.m.m(a, b) =', mmb)
#         break

#--------------second method: with function------------------
def k_m_m(a, b):
    if a >= b:
        kmm = a
    else:
        kmm = b
    for i in range(a * b):
        if kmm % a == 0 and kmm % b == 0:
            print('K.m.m(a, b) =', kmm)
            break
        else:
            kmm += 1
            if kmm % a == 0 and kmm % b == 0:
                print('K.m.m(a, b) =', kmm)
                break

k_m_m(a, b)