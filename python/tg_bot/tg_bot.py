"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import os
import logging
from typing import Dict
from telegram import Update, ForceReply,KeyboardButton,ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
import python.tg_bot.ksqldb as ksql
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

markup = ReplyKeyboardMarkup([[KeyboardButton('Send location',request_location=True)]], one_time_keyboard=True)


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f'{key} - {value}' for key, value in user_data.items()]
    return "\n".join(facts).join(['\n', '\n'])


def start(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask user for input."""
    update.message.reply_text(
        "Breathe. Send me your location to find pollution levels in your area.",
        reply_markup=markup,
    )
    return CHOOSING


def regular_choice(update: Update, context: CallbackContext) -> int:
    """Ask the user for info about the selected predefined choice."""
    loc = update.message.location
    loc = [str(loc.longitude), str(loc.latitude)]
    context.user_data['location'] = loc
    airquality_dict = ksql.get_latest_airquality_data_for_location[loc[1],loc[0]]
    update.message.reply_text(f"Looks like you're at {';'.join(loc)} <br> Your nearest measurement is from {airquality_dict['site']}"
                              f"Your readings are as follows:{airquality_dict['readings']}")

    return TYPING_REPLY

def done(update: Update, context: CallbackContext) -> int:
    """Display the gathered info and end the conversation."""
    user_data = context.user_data
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text(
        f"I learned these facts about you: {facts_to_str(user_data)}Until next time!",
        reply_markup=ReplyKeyboardRemove(),
    )

    user_data.clear()
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(os.getenv('TG_TOKEN'))

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(
                    Filters.location, regular_choice
                ),
            ],
            TYPING_CHOICE: [
                MessageHandler(
                    Filters.text & ~(Filters.command | Filters.regex('^Done$')), regular_choice
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

# Define a few command handlers. These usually take the two arguments update and
# context.
# def start(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     update.message.reply_markdown_v2(
#         fr'Hi {user.mention_markdown_v2()}\! <br> Can I use your location?',
#         reply_markup=makeKeyboard(),
#     )
#
# def makeKeyboard():
#     markup =KeyboardButton(request_location=True)
#
#     for key, value in stringList.items():
#         markup.add(types.InlineKeyboardButton(text=value,
#                                               callback_data="['value', '" + value + "', '" + key + "']"),
#         types.InlineKeyboardButton(text=crossIcon,
#                                    callback_data="['key', '" + key + "']"))
#
#     return markup
#
# def location(update:Update, conuext: CallbackContext) -> None:
#     update.message.reply_text(update.message.location)
#
# def help_command(update: Update, context: CallbackContext) -> None:
#     """Send a message when the command /help is issued."""
#     update.message.reply_text('Help!')
#
#
# def echo(update: Update, context: CallbackContext) -> None:
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)
#
#
# def main() -> None:
#     """Start the bot."""
#     # Create the Updater and pass it your bot's token.
#     updater = Updater(os.getenv('TG_TOKEN'))
#
#     # Get the dispatcher to register handlers
#     dispatcher = updater.dispatcher
#
#     # on different commands - answer in Telegram
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CommandHandler("help", help_command))
#
#     # on non command i.e message - echo the message on Telegram
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
#     dispatcher.add_handler(MessageHandler(Filters.location, location))
#
#     # Start the Bot
#     updater.start_polling()
#
#     # Run the bot until you press Ctrl-C or the process receives SIGINT,
#     # SIGTERM or SIGABRT. This should be used most of the time, since
#     # start_polling() is non-blocking and will stop the bot gracefully.
#     updater.idle()
#

if __name__ == '__main__':
    main()