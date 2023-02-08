from random import choice
user_score = com_1_score = com_2_score = draw = 0
for i in range(3):
    user_choise = input('Please show the palm or top of your hand: ')
    computer_1 = choice(['✋', '🤚'])
    computer_2 = choice(['✋', '🤚'])
    print('user:',user_choise, 'com_1:', computer_1, 'com_2:', computer_2)
    if computer_1 == computer_2 == user_choise:
        draw += 1
    elif computer_1 == computer_2:
        user_choise += 1
    elif computer_1 == user_choise:
        com_2_score += 1
    elif computer_2 == user_choise:
        com_1_score += 1
print('user:',user_score, '\ncom_1:', com_1_score, '\ncom_2:', com_2_score, '\ndraw: ', draw)
if user_score > com_1_score and user_score > com_2_score:
    print('User wins.✅')
if com_1_score > user_score and com_1_score > com_2_score:
    print('Computer_1 wins.✅')
if com_2_score > user_score and com_2_score > com_1_score:
    print('Computer_2 wins.✅')