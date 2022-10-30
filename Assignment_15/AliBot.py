import random
import telebot
from telebot import types
from gtts import gTTS
import qrcode

mybot = telebot.TeleBot('5779783147:AAFq7cTGSciaU9LbYsuWC1ICkezZEUgoFqk')

def find_at(msg):
  for text in msg:
    if '@' in text:
      return text

my_markup = types.ReplyKeyboardMarkup(row_width=3)
start_btn = types.KeyboardButton('/start')
help_btn = types.KeyboardButton('/help')
new_game_btn = types.KeyboardButton('/game')
new_voice_btn = types.KeyboardButton('/voice')
new_qrcode_btn = types.KeyboardButton('/qrcode')
new_age_btn = types.KeyboardButton('/age')
my_markup.add(start_btn, help_btn, new_game_btn, new_voice_btn, new_qrcode_btn, new_age_btn)

@mybot.message_handler(commands=['start'])
def send_welcome(message):
    mybot.send_message(message.chat.id, "Hello %s! welcome to my bot😘" % message.from_user.first_name, reply_markup=my_markup)

@mybot.message_handler(commands=['help'])
def echo_all(message):
    mybot.reply_to(message, 'To use this bot, send it a instagram id.')

@mybot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text, reply_markup=my_markup)
def at_answer(message):
  texts = message.text.split()
  at_text = find_at(texts)

  mybot.reply_to(message, 'https://instagram.com/{}'.format(at_text[1:]), reply_markup=my_markup)

@mybot.message_handler(commands=['game'])
def send_number(message):
    mybot.reply_to(message, 'Plz enter a number between 1 & 100')
    r = random.randint(1, 100)
    @mybot.message_handler(func=lambda m:True)
    def send_message(message):
        x = int(message.text)
        if x == r :
            mybot.send_message(message.chat.id, "Congratiolation %s! you win ✅" % message.from_user.first_name, reply_markup=my_markup)
        elif x < r :
            mybot.reply_to(message, 'Go up ⏫')
        elif x > r :
            mybot.reply_to(message, 'Go down ⏬')

@mybot.message_handler(commands=['age'])
def send_age(message):
    mybot.reply_to(message, 'Plz enter your Birth Year: ')
    @mybot.message_handler(func=lambda m: True)
    def echo_age(message):
        birth_year = int(message.text)
        your_age = 1401 - birth_year
        mybot.reply_to(message, f'You are {your_age} yaers old!')

@mybot.message_handler(commands=['voice'])
def send_voice(message):
    mybot.reply_to(message, 'Please Enter your message in English to hear it.')
    @mybot.message_handler(func=lambda m:True)
    def echo_voice(message):
        soundtext = gTTS(message.text)
        soundtext.save('soundtext.mp3')
        voice = open('/content/soundtext.mp3', 'rb')
        mybot.send_voice(message.chat.id, voice)
@mybot.message_handler(commands=['qrcode'])
def send_qrcode(message):
    mybot.reply_to(message, 'please enter the string to get the QRCODE') 
    @mybot.message_handler(func=lambda m:True)   
    def echo(message):
        qrtext = message.text
        qrpic = qrcode.make(qrtext)
        qrpic.save('qrpic.png')
        photo = open('/content/qrpic.png', 'rb')
        mybot.send_photo(message.chat.id, photo)
            

mybot.polling()