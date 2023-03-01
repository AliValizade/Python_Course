import random
import ast
import telebot
from telebot import types
from gtts import gTTS
import qrcode
import pysynth as ps

MUSIC = ()
NOTE = ''
STRETCH = ''

mybot = telebot.TeleBot('5779783147:AAFq7cTGSciaU9LbYsuWC1ICkezZEUgoFqk')

my_markup = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
start_btn = telebot.types.KeyboardButton('/start')
help_btn = telebot.types.KeyboardButton('/help')
new_game_btn = telebot.types.KeyboardButton('/game')
new_voice_btn = telebot.types.KeyboardButton('/voice')
new_qrcode_btn = telebot.types.KeyboardButton('/qrcode')
new_age_btn = telebot.types.KeyboardButton('/age')
music_btn = telebot.types.KeyboardButton('/music')
my_markup.add(start_btn, help_btn, new_game_btn, new_voice_btn, new_qrcode_btn, new_age_btn, music_btn)

@mybot.message_handler(commands=['start'])
def send_welcome(message):
    mybot.send_message(message.chat.id, "Hello %s! welcome to my bot😘" % message.from_user.first_name, reply_markup=my_markup)

@mybot.message_handler(commands=['help'])
def echo_all(message):
    mybot.reply_to(message, 'To use this bot, send it:\n/start \n/help \n/game \n/age \n/qrcode \n/music.')
  
@mybot.message_handler(commands=['game'])
def send_number(message):
    mybot.reply_to(message, 'Plz enter a number between 1 & 100')
    r = random.randint(1, 100)
    @mybot.message_handler(func=lambda m:True)
    def send_message(message):
        x = int(message.text)
        if x < r :
            mybot.reply_to(message, 'Go up ⏫')
        elif x > r :
            mybot.reply_to(message, 'Go down ⏬')
        elif x == r :
            mybot.send_message(message.chat.id, "Congratiolation %s! you win ✅" % message.from_user.first_name, reply_markup=my_markup)

@mybot.message_handler(commands=['age'])
def send_age(message):
    mybot.reply_to(message, 'Plz enter your Birth Year: ')
    mybot.register_next_step_handler(message, echo_age)
def echo_age(message):
    birth_year = int(message.text)
    your_age = 1401 - birth_year
    mybot.reply_to(message, f'You are {your_age} yaers old!')

@mybot.message_handler(commands=['voice'])
def send_voice(message):
    mybot.reply_to(message, 'Please Enter your message in English to hear it.')
    mybot.register_next_step_handler(message, echo_voice)
def echo_voice(message):
    soundtext = gTTS(message.text)
    soundtext.save('soundtext.mp3')
    voice = open('/content/soundtext.mp3', 'rb')
    mybot.send_voice(message.chat.id, voice)
@mybot.message_handler(commands=['qrcode'])
def send_qrcode(message):
    mybot.reply_to(message, 'please enter the string to get the QRCODE')
    mybot.register_next_step_handler(message, echo_qrcode) 
def echo_qrcode(message):
    qrtext = message.text
    qrpic = qrcode.make(qrtext)
    qrpic.save('qrpic.png')
    photo = open('/content/qrpic.png', 'rb')
    mybot.send_photo(message.chat.id, photo)

# ('c', 4),('c*', 4),('eb', 4),('g#', 4),('g*', 2),('g5', 4),('g5*', 4),
# ('r', 4),('e5', 16),('f5', 16),('e5', 16),('d5', 16),('e5*', 4),('c*', 4)

def add_note():
    global MUSIC
    global NOTE
    global STRETCH
    if NOTE == 'Do':
        NOTE = 'c'
    elif NOTE == 'Re':
        NOTE = 'd'
    elif NOTE == 'Mi':
        NOTE = 'e'
    elif NOTE == 'Fa':
        NOTE = 'f'
    elif NOTE == 'Sol':
        NOTE = 'g'
    elif NOTE == 'La':
        NOTE = 'a'
    else:
        NOTE = 'b'
    if STRETCH == 'Whole':
        STRETCH = 1
    elif STRETCH == 'Half':
        STRETCH = 2
    elif STRETCH == 'Quarter':
        STRETCH = 4
    elif STRETCH == 'Eighth':
        STRETCH = 8
    else:
        STRETCH = 16
    MUSIC += ((NOTE, STRETCH),)
    NOTE = ''
    STRETCH = ''

def set_note(name):
    global NOTE
    NOTE = name

def set_stretch(stroke):
    global STRETCH
    STRETCH = stroke

def empty_music():
    global MUSIC
    MUSIC = ()

@mybot.message_handler(commands=['music'])
def music_func(m):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    btn1 = telebot.types.KeyboardButton('start')
    markup.add(btn1)
    m = mybot.send_message(m.chat.id, 'Make your own music.', reply_markup=markup)
    mybot.register_next_step_handler(m, music01)

def music01(m):
    if not m.text.startswith('/'):
        if m.text != 'start':
            set_stretch(m.text)
        if STRETCH != '' and NOTE != '':
            add_note()
        markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
        btn1 = telebot.types.KeyboardButton('Do')
        btn2 = telebot.types.KeyboardButton('Re')
        btn3 = telebot.types.KeyboardButton('Mi')
        btn4 = telebot.types.KeyboardButton('Fa')
        btn5 = telebot.types.KeyboardButton('Sol')
        btn6 = telebot.types.KeyboardButton('La')
        btn7 = telebot.types.KeyboardButton('Si')
        btn8 = telebot.types.KeyboardButton('END')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        msg = mybot.send_message(m.chat.id, 'note:', reply_markup=markup)
        mybot.register_next_step_handler(msg, music02)
    else:
        mybot.reply_to(m, 'Plz enter your note: ', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))

def music02(m):
    if not m.text.startswith('/'):
        if not m.text == 'END':
            set_note(m.text)
            markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
            btn1 = telebot.types.KeyboardButton('Whole')
            btn2 = telebot.types.KeyboardButton('Half')
            btn3 = telebot.types.KeyboardButton('Quarter')
            btn4 = telebot.types.KeyboardButton('Eighth')
            btn5 = telebot.types.KeyboardButton('Sixteenth')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            msg = mybot.send_message(m.chat.id, 'stretch:', reply_markup=markup)
            mybot.register_next_step_handler(msg, music01)
        else:
            try:
                if len(MUSIC) >= 1:
                    mybot.send_message(m.chat.id, 'Your Music', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
                    ps.make_wav(MUSIC, fn="music.wav")
                    empty_music()
                    music = open('/content/music.wav', 'rb')
                    mybot.send_voice(m.chat.id, music)
            except:
                mybot.send_message(m.chat.id, 'Error!! try again.', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))
    else:
        mybot.reply_to(m, 'Plz enter your note: ', reply_markup=telebot.types.ReplyKeyboardRemove(selective=True))

mybot.polling()