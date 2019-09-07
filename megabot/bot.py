from telegram.ext import Updater, CommandHandler
import logging
#Proxy settings
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')

def greet_user(bot, update):
    text = 'Call /start'
    print(text)
    update.message.reply_text(text)
    logging.info('Send email to the customer')

#bot
def main():
    mybot = Updater("812960937:AAEXGUPi7Au90FxLNA0_Y947goTAzbXNS3A", request_kwargs=PROXY)

    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))

    mybot.start_polling()
    mybot.idle()

main()


