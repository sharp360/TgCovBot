from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
import json
import os


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Здарова ебать')

def cases(update: Update, context: CallbackContext) -> None:
    response = requests.api.get('https://api.apify.com/v2/key-value-stores/3Po6TV7wTht4vIEid/records/LATEST?disableRedirect=true').content
    response = json.loads(response)
    daily_infected = response['dailyInfected']
    daily_deceased = response['dailyDeceased']
    txtdate = response['txtDate']
    update.message.reply_text(f'New cases from {txtdate}: 🎉{daily_infected}🎉')

def deaths(update: Update, context: CallbackContext) -> None:
    response = requests.api.get('https://api.apify.com/v2/key-value-stores/3Po6TV7wTht4vIEid/records/LATEST?disableRedirect=true').content
    response = json.loads(response)
    daily_deceased = response['dailyDeceased']
    txtdate = response['txtDate']
    update.message.reply_text(f'New deaths from {txtdate}: {daily_deceased}')


updater = Updater(os.environ['TOKEN'])

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('cases', cases))
updater.dispatcher.add_handler(CommandHandler('deaths', deaths))

updater.start_polling()
updater.idle()
