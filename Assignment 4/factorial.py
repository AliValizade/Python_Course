def check_factorial():
    n = int(input('Plz enter a number:'))
    j = 1
    while j <= n:
        fact = 1
        for i in range(1, j+1):
            fact *= i
        if fact == n:
            print('Yes', j,'! =', n)
            break
        j += 1

    else:
        print('No')

check_factorial()
        

