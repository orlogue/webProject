import json

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from backend.celery_helper import app
from bot.bot import bot


@app.task
def send_order_item_approval(seller_id, product_name, product_id, buyer_id, quantity, price):
    yes = InlineKeyboardButton(text="Подтвердить ✅",
                               callback_data=json.dumps({'prdct_id': product_id,
                                                         'buyer_id': buyer_id,
                                                         'q': quantity,
                                                         'status': 1}))
    no = InlineKeyboardButton(text="Отменить ❌",
                              callback_data=json.dumps({'prdct_id': product_id,
                                                        'buyer_id': buyer_id,
                                                        'q': quantity,
                                                        'status': 0}))
    custom_keyboard = [[no, yes]]
    reply_markup = InlineKeyboardMarkup(custom_keyboard)
    bot.send_message(chat_id=seller_id,
                     text='У вас хотят купить товар '
                          f'{product_name} в количестве {quantity} шт. на сумму '
                          f'{price * quantity} руб.',
                     reply_markup=reply_markup)