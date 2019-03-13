import telepot

def tele(msg):
    bot = telepot.Bot('738453187:AAGuHaNH7Vx406WC8qCTwqyvPAPX--g_9ao')
    bot.sendMessage(chat_id='@CrisisNews',text=msg)

""" The function takes in a string and sends it to the telegram channel"""
