from matplotlib.style import use
from pyfiglet import Figlet

def show_menu():
    print('ⓂⓂⓂⓂⓂⓂⓂⓂⓂ  MENU ⓂⓂⓂⓂⓂⓂⓂⓂⓂ')
    print('1- Add new word \n2- Translation English => Persian \n3- Translation Persian => English \n4- Save & Exit')
    print('ⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂⓂ')
def load():
    print('🔠 Welcome to English <=> Persian Translator.🔠')
    words_db = open('words.txt', 'r')
    data = words_db.read()
    words = data.split('\n')
    for i in range(len(words)):
        words_tr = words[i].split(',')
        words_dict = {}
        words_dict['English'] = words_tr[0]
        words_dict['Persian'] = words_tr[1]
        translator_db.append(words_dict)
    words_db.close()
    show_menu()

def add_new_word():
    while True:
        print('1- English🟨 \n2- Persian🟨')
        En_or_Fa = int(input('Plz select the Language of the new_word: '))
        if En_or_Fa == 1:
            translator_db.append({'English': input('Plz enter a new English word: ').lower(), 'Persian': input('Plz enter persian translate of new_word:').lower()})
            print('The new word added to database. ✅')
        elif En_or_Fa == 2:
            translator_db.append({'Persian': input('Plz enter a new Pershian word: ').lower(), 'English': input('Plz enter English translate of new_word:').lower()})
            print('The new word added to database. ✅')
        add_new = input('Do you want to add new word ❔ (Y/N) ').lower()
        if add_new == 'n':
            break
    show_menu()
def english2persian():
    user_word = input('Plz enter your word in English:🔠 ').lower()
    for item in translator_db:
        if item['English'] == user_word:
            print('Translation of (', user_word, ') is:', item['Persian'], '✅')
            break
    else:
        print('The word not found! Please add it. ❎')
    show_menu()
def persian2english():
    user_word = input('Plz enter your word in Persian:🅿 ').lower()
    for item in translator_db:
        if item['Persian'] == user_word:
            print('Translation of (', user_word, ') is:', item['English'], '✅')
            break
    else:
        print('The word not found! Please add it. ❎')
    show_menu()
def save_and_exit():
    update_db = open('words.txt', 'w')
    for item in translator_db:
        update_db.write(item['English'] + ',' + item['Persian'])
        if item != translator_db[-1]:
            update_db.write('\n')
    update_db.close()
    print('Database updated successfully . ✅')
    exit()
f = Figlet(font='slant')
print(f.renderText('Translator'))

translator_db = []
load()
while True:
    menu_item = int(input('Plz select number of the menu: '))
    if menu_item == 1:
        add_new_word()
    elif menu_item == 2:
        english2persian()
    elif menu_item == 3:
        persian2english()
    elif menu_item == 4:
        save_and_exit()