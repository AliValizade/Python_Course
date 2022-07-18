def multiplication_table(n, m):
    for i in range(1, n+1):
        for j in range(1, m+1):
            print(i * j, end='\t')
        print()

multiplication_table(10, 10)