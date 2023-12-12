from telegram import ChatAction, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from text_to_speech import tts

TOKEN = 'YOUR TOKEN HERE'


def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def send_voice(update, context):
    chat_id = update.message.chat_id
    text = update.message.text
    context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.UPLOAD_AUDIO)

    voice_file_path = tts(text, str(chat_id)

    context.bot.send_voice(chat_id=update.message.chat_id, voice=InputFile(open(voice_file_path, 'rb')))


def start(update, context):
    chat_id = update.message.chat_id
    create_folder(str(chat_id))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="""This bot converts the text you write in English into an audio recording and sends it to you.""")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_voice))

    updater.start_polling()
    updater.idle()
