import random
game_item = ['rock', 'paper', 'scissors']
print(game_item)
score_board = {'user': 0, 'computer': 0}
for i in range(10):
    computer_choice = game_item[random.randint(0, 2)]
    user_choice = input('Plz enter your choice: ').lower()
    if computer_choice == 'rock':
        if user_choice == 'paper':
            score_board['user'] += 1
        elif user_choice == 'scissors':
            score_board['computer'] += 1
    elif computer_choice == 'paper':
        if user_choice == 'rock':
            score_board['computer'] += 1
        elif user_choice == 'scissors':
            score_board['user'] += 1
    elif computer_choice == 'scissors':
        if user_choice == 'rock':
            score_board['user'] += 1
        elif user_choice == 'paper':
            score_board['computer'] += 1
    elif computer_choice == user_choice:
        print('Draw! Try again.')
    print(score_board)

if score_board['computer'] > score_board['user']:
    print('Computer Wins.')
elif score_board['computer'] < score_board['user']:
    print('Congratulations, You Win. ✅')
else:
    print('Draw! ⏸')

