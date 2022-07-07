import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram.update import Update

BOT_TOKEN = '5515977752:AAG5diYY1jno26YmFu7jnmRs0gSLznGXM-Y'


# updater = Updater(token, use_context=True)


# bot = telegram.Bot(token=token)
# updater.start_polling()


def send_order_approval(chat_id, product):
    yes = InlineKeyboardButton(text="Да", callback_data=1)
    no = InlineKeyboardButton(text="Нет", callback_data=0)
    custom_keyboard = [[yes, no]]
    reply_markup = InlineKeyboardMarkup(custom_keyboard)
    updater.bot.send_message(chat_id=chat_id,
                             text='У вас хотят купить товар '
                                  f'{product}',
                             reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    # This will define which button the user tapped on (from what you assigned to "callback_data". As I assigned them "1" and "2"):
    choice = query.data

    # Now u can define what choice ("callback_data") do what like this:
    if choice == '1':
        print('YES')

    if choice == '0':
        print('NO')


# updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot))
# updater.dispatcher.add_handler(CallbackQueryHandler(button))
# updater.start_polling()

# def main():
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# start_handler = CommandHandler("start", start)
# help_handler = CommandHandler("help", help)
dispatcher.add_handler(CallbackQueryHandler(button))
# dispatcher.add_handler(send_order_approval)
# dispatcher.add_handler(help_handler)
updater.start_polling()


# if __name__ == '__main__':
#     main()
