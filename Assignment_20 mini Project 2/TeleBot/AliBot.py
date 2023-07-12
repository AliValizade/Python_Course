import telebot
from telebot import types
import random
import datetime
import pyttsx3
import qrcode
import pysynth as ps

bot = telebot.TeleBot("5779783147:AAFq7cTGSciaU9LbYsuWC1ICkezZEUgoFqk")

# Create a keyboard object
my_markup = types.ReplyKeyboardMarkup(row_width=2)

# Add buttons to the keyboard
my_markup.add('/start', '/help', '/guess', '/age', '/qrcode', '/music')

# Start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello %s! welcome to my bot😘" % message.from_user.first_name, reply_markup=my_markup)

# Help
@bot.message_handler(commands=['help'])
def echo_all(message):
    bot.reply_to(message, 'To use this bot, send it:\n/start \n/help \n/game \n/age \n/voice \n/qrcode \n/music.')

# Number guessing game
@bot.message_handler(commands=['guess'])
def guess_number(message):
    number = random.randint(1, 100)
    bot.send_message(message.chat.id, "I'm thinking of a number between 1 and 100. Try to guess it!", reply_markup=my_markup)
    @bot.message_handler(func=lambda message: True)
    def check_guess(message):
        try:
            guess = int(message.text)
            if guess == number:
                bot.send_message(message.chat.id, "Congratulations, you guessed it!", reply_markup=my_markup)
            elif guess < number:
                bot.send_message(message.chat.id, "Too low, try again!", reply_markup=my_markup)
            elif guess > number:
                bot.send_message(message.chat.id, "Too high, try again!", reply_markup=my_markup)
        except ValueError:
            bot.send_message(message.chat.id, "Please enter a valid number.", reply_markup=my_markup)

# Calculate age
@bot.message_handler(commands=['age'])
def calculate_age(message):
    bot.send_message(message.chat.id, "Please enter your birth year:", reply_markup=my_markup)
    bot.register_next_step_handler(message, calculate_age_step)
def calculate_age_step(message):
    try:
        birth_year = int(message.text)
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        bot.send_message(message.chat.id, f"You are {age} years old.", reply_markup=my_markup)
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid year.", reply_markup=my_markup)

# Convert text to voice
@bot.message_handler(commands=['voice'])
def convert_text_to_voice(message):
    bot.send_message(message.chat.id, "Please enter the text you want me to speak:", reply_markup=my_markup)
    bot.register_next_step_handler(message, convert_text_to_voice_step)
def convert_text_to_voice_step(message):
    text = message.text
    engine = pyttsx3.init()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()
    audio = open('output.mp3', 'rb')
    bot.send_audio(message.chat.id, audio)

# Generate QR code
@bot.message_handler(commands=['qrcode'])
def generate_qr_code(message):
    bot.send_message(message.chat.id, "Please enter the text for the QR code:", reply_markup=my_markup)
    bot.register_next_step_handler(message, generate_qr_code_step)
def generate_qr_code_step(message):
    text = message.text
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
    qr_code = open('qrcode.png', 'rb')
    bot.send_photo(message.chat.id, qr_code)

# Create music
@bot.message_handler(commands=['music'])
def create_music(message):
    notes = [('c', 4), ('d', 4), ('e', 4), ('f', 4), ('g', 4), ('a', 4), ('b', 4)]
    song = random.choices(notes, k=10)
    ps.make_wav(song, fn="output.wav")
    music = open('output.wav', 'rb')
    bot.send_audio(message.chat.id, music)

# Start the bot
bot.polling()
