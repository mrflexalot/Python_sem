from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def log(update: Update, context: CallbackContext, text):
    file = open('C:\Users\PCIgor\Desktop\geekbrains\python\pythonsem\9_homework\hw_2\db.csv', 'a')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {text}\n')
    file.close()
