import telegram.ext

## Initializing with the both token

Token = "6033441861:AAFo8X6hE7mc4LCDerU9IF8EeDUDfZtc3Fk"

updater = telegram.ext._updater (Token, use_context = True)
dispatcher  = updater.dispatcher

# starting the bot

def start (update, context):
    update.message.reply_text ("Going through your inbox at the end of the day may feel like a Herculean task. Make life easier by having your mails sent to you on Telegram")

# help command

def help (update, context):
    update.message.reply_text (
        """
        /start --> Going through your inbox at the end of the day may feel like a Herculean task. Make life easier by having your mails sent to you on Telegram
        /help --> This particular message
        /fetch --> Starts fetching the mails

        """
    )

# Fetching mails

def fetch (update, context):
    update.message.reply_text ("Fetching e-mails from the last call")
    

