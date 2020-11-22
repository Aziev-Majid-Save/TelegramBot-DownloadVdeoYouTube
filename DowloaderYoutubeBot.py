# - *- coding: utf- 8 - *-
import telebot
import random
import os
from telebot import types

bot = telebot.TeleBot('***')

@bot.message_handler(commands=['start'])
def welcome(message):

    bot.send_message(message.chat.id, "Добро пожаловать! Скинь ссылку на видео из YouTube мне и я тебе скину ссылку на скачивание этого видео! Приятного пользование этим ботом :)".format(message.from_user, bot.get_me()))
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    url = message.text;
    if url[:12] == "https://yout":
        urlSS = url[17:]
        bot.send_message(message.chat.id, "Вот ссылка на скачивание: " + "https://www.ssyoutube.com/watch?v=" + urlSS)  
    		
    if url[:12] == "https://www.":
        urlSS = url[23:]
        bot.send_message(message.chat.id, "Вот ссылка на скачивание: " + "https://www.ssyoutube.com" + urlSS)

    if url[:12] == "https://m.yo":
        urlSS = url[22:]
        bot.send_message(message.chat.id, "Вот ссылка на скачивание: " + "https://www.ssyoutube.com/" + urlSS)

# RUN
def botCikle():
	try:
		bot.polling(none_stop=True)
	except:
		time.sleep(5)
		VizovCikle()

def VizovCikle():
	botCikle()
	
botCikle()
