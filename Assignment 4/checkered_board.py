def checkered_board(n, m):
    for i in range(n):
        for j in range(m):
            print('#*', end='')
        print()

checkered_board(12, 15)
