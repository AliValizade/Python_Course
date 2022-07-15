import random
words = ['python', 'java', 'php', 'html', 'javascript', 'kotlin', 'swift']
computer_choice = random.choice(words)
guess_letters = ""
life_count = 5
while life_count > 0:
    user_letter = input("\n Plz enter your guess_letter: ").lower()
    if user_letter in computer_choice:
        print("Ok, your guess is one or more letter in the computer_choice.")
        guess_letters += user_letter
    else:
        life_count -= 1
        print("Sorry, your guess is not in the computer_choice. You have ", life_count, "guesses left.")
    winner_check = 0
    for letter in computer_choice:
        if letter in guess_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
            winner_check += 1
    if winner_check == 0:
        print("\nCongratulations, You win!")
        break
else:
    print("Game over! Try again.")