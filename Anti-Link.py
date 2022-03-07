from telegram import Update,ParseMode,MessageEntity
from telegram.ext import Updater,CallbackContext,CommandHandler,MessageHandler,Filters

# your bot token 
# yo can get your bot token from botfather in telegram 
TOKEN = 'your bot token'
# create a Updater and pass it your bot token
# use_context is not necessary because by default it's True
BOT=Updater(token=TOKEN,use_context=True)

# start writing bot commands 
def start(update:Update,context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Hello {} ، wellcome to the Anti link bot'.format(update.message.chat.first_name))
    context.bot.send_message(chat_id=update.effective_chat.id,text='✅ You can add this bot to your groups or your channels to get the bot up and running ✅')
        
def antilink(update:Update,context:CallbackContext):
    List_1=[MessageEntity.URL]
    if update.message.parse_entities(types=List_1):
        context.bot.delete_message(chat_id=update.effective_chat.id,message_id=update.message.message_id)    
    
def antilink2(update:Update,context:CallbackContext):
    if update.message.caption_entities[0]['type']=='url':
        context.bot.delete_message(chat_id=update.effective_chat.id,message_id=update.message.message_id)    
# end writing bot commands 
    
# register handlers 
BOT.dispatcher.add_handler(CommandHandler('start',start))
BOT.dispatcher.add_handler(MessageHandler(Filters.text,antilink))
BOT.dispatcher.add_handler(MessageHandler(Filters.all,antilink2))
# Start the Bot
BOT.start_polling()
# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
BOT.idle()
