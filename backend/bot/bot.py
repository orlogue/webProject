import json
import os
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, ChosenInlineResult
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CallbackQueryHandler, CommandHandler
from telegram.update import Update

BOT_TOKEN = '5515977752:AAES0iPisL0jtbX4vaV3nOskfcBhJZ5-pno'
BACKEND_BASE = 'http://127.0.0.1:8000'
updater = Updater(BOT_TOKEN, use_context=True)

bot = updater.bot
dispatcher = updater.dispatcher


# updater.start_polling()
# def send_back(update: Update, context: CallbackContext):
#     update.message.reply_text('ads')


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Приветствуем Вас! '
                              '\nДля начала нажмите на\n/send_phone_number')


def send_phone_number(update: Update, context: CallbackContext):
    con_keyboard = KeyboardButton(text="Поделиться номером телефона", request_contact=True)
    # loc_keyboard = KeyboardButton(text="send_location", request_location=True)
    custom_keyboard = [[con_keyboard]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True)
    update.message.reply_text(text='Пожалуйста, поделитесь своим номером '
                                   'телефона для корректной работы сервиса!',
                              reply_markup=reply_markup)


def contact_callback(update, context):
    contact = update.message.contact
    phone = contact.phone_number
    r = requests.get(f'%s/api/user/{phone}' % BACKEND_BASE)
    phone_number = r.json()
    data = {'user': phone_number['id'],
            'telegram_id': update.effective_user.id}
    r = requests.post('%s/api/telegram_id/create/' % BACKEND_BASE, data)
    if (r.status_code != 201):
        update.message.reply_text(text='Что-то пошло не так!'
                                       '\nУбедитесь, что вы сначала зарегистрировались на сайте.')
    else:
        update.message.reply_text(text='Номер успешно получен!', reply_markup=ReplyKeyboardRemove())


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    data = json.loads(query.data)

    product_id = data['prdct_id']
    quantity = data['q']

    if data['status'] == 1:
        response = requests.get(f'%s/api/products/{product_id}' % BACKEND_BASE)
        product = json.loads(response.text)
        requests.patch(f'%s/api/products/{product_id}' % BACKEND_BASE,
                       {'quantity': product["quantity"] - quantity})
        response = requests.get(f'%s/api/users/{product["seller_id"]}' % BACKEND_BASE)
        seller = json.loads(response.text)

        approved = InlineKeyboardButton(text="Подтверждено ✅", callback_data='approved')
        custom_keyboard = [[approved]]
        reply_markup = InlineKeyboardMarkup(custom_keyboard)
        bot = context.bot
        bot.edit_message_reply_markup(chat_id=query.message.chat_id,
                                      message_id=query.message.message_id,
                                      reply_markup=reply_markup)
        bot.send_message(chat_id=data['buyer_id'],
                         text=f'{product["name"]} ждёт тебя в корпусе {seller["building"]} '
                              f'в комнате {seller["room"]}!'
                              f'\nК оплате: {quantity * product["price"]} руб.'
                              f'\nПеревод по номеру: +{seller["phone_number"]}')

    if data['status'] == 0:
        approved = InlineKeyboardButton(text="Отменено ❌", callback_data='declined')
        custom_keyboard = [[approved]]
        reply_markup = InlineKeyboardMarkup(custom_keyboard)
        context.bot.edit_message_reply_markup(chat_id=query.message.chat_id,
                                              message_id=query.message.message_id,
                                              reply_markup=reply_markup)

        response = requests.get(f'%s/api/products/{product_id}' % BACKEND_BASE)
        product = json.loads(response.text)
        context.bot.send_message(chat_id=data['buyer_id'],
                                 text=f'Продавец отменил продажу {product["name"]} :(')


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('send_phone_number', send_phone_number))
dispatcher.add_handler(MessageHandler(Filters.contact, contact_callback))
dispatcher.add_handler(CallbackQueryHandler(button))

PORT = int(os.environ.get('PORT', '8443'))


def main():
    updater.start_webhook(
        listen='0.0.0.0',
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url='https://98a9-82-162-0-40.eu.ngrok.io/' + BOT_TOKEN
    )
    updater.idle()


if __name__ == '__main__':
    main()
# def send_order_approval(chat_id, product):
#     yes = InlineKeyboardButton(text="Да", callback_data=1)
#     no = InlineKeyboardButton(text="Нет", callback_data=0)
#     custom_keyboard = [[yes, no]]
#     reply_markup = InlineKeyboardMarkup(custom_keyboard)
#     updater.bot.send_message(chat_id=chat_id,
#                              text='У вас хотят купить товар '
#                                   f'{product}',
#                              reply_markup=reply_markup)


# updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot))
# updater.dispatcher.add_handler(CallbackQueryHandler(button))
# updater.start_polling()

# def main():
#     updater = Updater(token=BOT_TOKEN, use_context=True)
#     dispatcher = updater.dispatcher
#
#     # start_handler = CommandHandler("start", start)
#     # help_handler = CommandHandler("help", help)
#     dispatcher.add_handler(CallbackQueryHandler(button))
#     dispatcher.add_handler(send_order_approval)
#     # dispatcher.add_handler(help_handler)
#     updater.start_polling()
#
#
# if __name__ == '__main__':
#     main()
