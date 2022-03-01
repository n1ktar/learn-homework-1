"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}

current_datetime = datetime.now()

planet_dict = {'Mars': ephem.Mars(current_datetime), 'Venus': ephem.Venus(current_datetime), 'Saturn': ephem.Saturn(current_datetime), 'Jupiter': ephem.Jupiter(current_datetime),
               'Neptune': ephem.Neptune(current_datetime), 'Uranus': ephem.Uranus(current_datetime), 'Mercury': ephem.Mercury(current_datetime), 'Moon': ephem.Moon(current_datetime), 'Pluto': ephem.Pluto(current_datetime)}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def constellations(update, context):
    user_planet = update.message.text.split()[1]
    print(user_planet)
    ephem_planet = planet_dict.get(user_planet, None)
    if ephem_planet != None:   
        ephem_coordinates = ephem_planet
        const = ephem.constellation(ephem_coordinates)
        print(const)
        update.message.reply_text(const)
    else:
        update.message.reply_text("I dont know this planet")

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def main():
    mybot = Updater("5235982340:AAHh0sahvpHDbgoGCaUWFQuVB1a-3EzWjKY", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constellations))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
