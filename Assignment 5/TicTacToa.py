import random
from colorama import Fore
import time
start = time.time()
G_Board =  [['-','-','-'],
            ['-','-','-'],
            ['-','-','-']]
def show_G_Board():
    for i in range(3):
        for j in range(3):
            if G_Board[i][j] == '-':
                print(Fore.WHITE + G_Board[i][j], end=' ')
            elif G_Board[i][j] == 'X':
                print(Fore.YELLOW + G_Board[i][j], end=' ')
            elif G_Board[i][j] == 'O':
                print(Fore.GREEN + G_Board[i][j], end=' ')
        print()
def check_game():
    def print_winner(): #----------print result function
        if count_x == 3:
            print('Congatulations, Player 1 Wins✅')
            print('Run time of the game: ' + str(time.time() - start))
            exit()
        elif count_o == 3:         
            print('Congatulations, Player 2 Wins✅')
            print('Run time of the game: ' + str(time.time() - start))
            exit()
        elif count_dash == 0:
            print('The game equalised!⛔')
            print('Run time of the game: ' + str(time.time() - start))
            exit()
    count_dash = 9
    for i in range(3): #---------- Check winner for sort columns & rows OR Draw! 
        count_x = 0
        count_o = 0
        for j in range(3):
            if G_Board[i][j] == 'X':
                count_x += 1
                count_dash -= 1
            elif G_Board[i][j] == 'O':
                count_o += 1
                count_dash -= 1             
        print_winner()
    print_winner()
    count_x = 0 #----------------- Check winner for sort diagonal 
    count_o = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                if G_Board[i][j] == 'X':
                    count_x += 1
                elif G_Board[i][j] == 'O':
                    count_o += 1
        print_winner()
    if G_Board[0][2] == 'X' and G_Board[1][1] == 'X' and G_Board[2][0] == 'X':
        count_x = 3
    elif G_Board[0][2] == 'O' and G_Board[1][1] == 'O' and G_Board[2][0] == 'O':
        count_o = 3
    print_winner()
#--------------------------------- Start Game
while True:
    game_type = int(input('Plz select game with single player (1) or two player (2): '))
    if game_type in range(1, 3):
        break
    else:
        print('The value is out of range, Try again!')
while True: 
    while True: #----------------- Player 1
        row = int(input('Player 1 enter number of row: '))
        col = int(input('Player 1 enter number of column: '))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if G_Board[row][col] == '-':
                G_Board[row][col] = 'X'
                break
            else:
                print('Sorry! The cell is not empty.')
        else:
            print('The value is out of range, Try again!')
    show_G_Board()
    check_game()
    print('Player 2: ') #----------------- Player 2
    while True: 
        if game_type == 2:
            row = int(input('Player 2 enter number of row: '))
            col = int(input('Player 2 enter number of column: '))
            if 0 <= row <= 2 and 0 <= col <= 2:
                if G_Board[row][col] == '-':
                    G_Board[row][col] = 'O'
                    break
                else:
                    print('Sorry! The cell is not empty.')
            else:
                print('The value is out of range, Try again!')
        elif game_type == 1:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if 0 <= row <= 2 and 0 <= col <= 2:
                if G_Board[row][col] == '-':
                    G_Board[row][col] = 'O'
                    break
    show_G_Board()
    check_game()