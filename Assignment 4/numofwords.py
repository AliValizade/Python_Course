def num_of_words():
    sentence = input('Plz enter a sentece: ')
    c = 0
    for i in sentence:
        if i == " ":
            c += 1
    print('Number of words in sentence is: ', c+1)

num_of_words()