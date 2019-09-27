from datetime import datetime
from random import choice
from glob import glob


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton
import ephem
from emoji import emojize


import logging, passwd


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO, filename='bot.log')




def greet_planet(bot, update, user_data):
    receive_text = update.message.text
    arrt_planet_name = receive_text.split(' ')
    print(arrt_planet_name)
    planet = getattr(ephem, arrt_planet_name[1])(datetime.now())
    cons = ephem.constellation(planet)
    print(cons)
    update.message.reply_text(cons, reply_markup=get_keyboard())


def send_minion_picture(bot, update, user_data):
    minion_list = glob('pictures/minion*')
    minion_pictures = choice(minion_list)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(minion_pictures, 'rb'), reply_markup=get_keyboard())


def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = f"Hello! {emo}"
    print(text)
    contact_button = KeyboardButton('Send contacts', request_contact=True)
    location_button = KeyboardButton('Request location', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
        ['Geve me a minion pictures', 'Change avatar'],
        [contact_button, location_button]
    ])
    update.message.reply_text(text, reply_markup=get_keyboard())



def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    reply_text_for_user = f"Hello {update.message.chat.first_name}, you wrote next message: {update.message.text}, {emo}"
    logging.info(f"User: {update.message.chat.first_name}, Chat id: {update.message.chat.id}, Message: {update.message.text} ")
    print(f"User: {update.message.chat.first_name}, Chat id: {update.message.chat.id}, Message: {update.message.text} ")
    update.message.reply_text(reply_text_for_user, reply_markup=get_keyboard())


def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text(f"Change your avatar is done to: {emo}", reply_markup=get_keyboard())


def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text(f"Thanks! {get_user_emo(user_data)}", reply_markup=get_keyboard())


def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text(f"Thanks! {get_user_emo(user_data)}", reply_markup=get_keyboard())


def get_keyboard():
    contact_button = KeyboardButton('Send contacts', request_contact=True)
    location_button = KeyboardButton('Request location', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
        ['Geve me a minion pictures', 'Change avatar'],
        [contact_button, location_button]
    ], resize_keyboard=True)
    return my_keyboard


def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(passwd.USER_EMOJI), use_aliases=True)
        return user_data['emo']

#bot
def main():
    mybot = Updater(passwd.token_API, request_kwargs=passwd.PROXY)

    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler('planet', greet_planet, pass_user_data=True))
    dp.add_handler(CommandHandler('minion', send_minion_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Geve me a minion pictures)$', send_minion_picture, pass_user_data=True))
    dp.add_handler(RegexHandler('^(Change avatar)$', change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))




    mybot.start_polling()
    mybot.idle()

main()


