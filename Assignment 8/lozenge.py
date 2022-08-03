n = int(input('Plz enter a number: '))
star = 1
space = n 
for i in range(n):
    print(space * ' ',star * '*')
    star += 2
    space -= 1
for i in range(n+1):
    print(space * ' ',star * '*')
    star -= 2
    space += 1