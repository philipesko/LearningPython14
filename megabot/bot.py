from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, passwd, ephem
from datetime import datetime
#Proxy settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')


def greet_planet(bot, update):
    update.message.reply_text('Please write name for planet!')
    update.planets(bot, update)

def planets (bot, update):
    arrt_planet_name = update.message.text
    print(arrt_planet_name)
    planet = getattr(ephem, arrt_planet_name)(datetime.now())
    cons = ephem.constellation(planet)
    print(cons)
    update.message.reply_text(cons)




def greet_user(bot, update):
    text = 'Call /start'
    print(text)
    update.message.reply_text(text)
    logging.info('Send answer to the client')

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
    logging.info('Receive message text from client:  '+ user_text)
#bot
def main():
    mybot = Updater(passwd.token_API, request_kwargs=passwd.PROXY)

    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', greet_planet))
    dp.add_handler(MessageHandler(Filters.text, planets))


    mybot.start_polling()
    mybot.idle()

main()


