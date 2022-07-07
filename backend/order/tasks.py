from telegram import Update

from backend.celery_helper import app
# from backend.bot import bot
from bot.bot import send_order_approval

# from backend.bot import update
# from telegram.ext import Updater
#
# updater = Updater("5515977752:AAG5diYY1jno26YmFu7jnmRs0gSLznGXM-Y", use_context=True)


@app.task
def do(telegram_id, product):
    pass
    # send_order_approval(chat_id=telegram_id, product=product)
    # bot.send_message(chat_id=telegram_id, text=,
    #                  reply_markup=reply_markup)
    # updater.bot.send_message(telegram_id, text='У вас хотят купить товар '
    #                                            f'{product}',
    #                          reply_markup=custom_keyboard)

    # update.message.reply_text(text='Пожалуйста, поделитесь своим номером '
    #                                'телефона для корректной работы сервиса!',
    #                           reply_markup=reply_markup)
    # updater.start_polling()
