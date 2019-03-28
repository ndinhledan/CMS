import telepot

def tele(postal,msg):
    bot = telepot.Bot('738453187:AAGuHaNH7Vx406WC8qCTwqyvPAPX--g_9ao')
    North = frozenset(["No","28","29","30","31","32","33","34","35","36","37","53","54","55","56","57","72","73","75","76","77","78","79","80","82"])
    West = frozenset(["We","60","61","62","63","64","65","66","67","68","69","70","71"])
    East = frozenset(["Ea","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","81"])
    Central = frozenset(["Ce","01","02","03","04","05","06","07","08","18","19","20","21","22","23","24","25","26","27","58","59"])
    South = frozenset(["So","09","10","11","12","13","14","15","16","17"])
    if postal[:2] in North:
        bot.sendMessage(chat_id='@CrisisNewsNorth',text=msg)
    if postal[:2] in South:
        bot.sendMessage(chat_id='@CrisisNewsSouth',text=msg)
    if postal[:2] in West:
        bot.sendMessage(chat_id='@CrisisNewsWest',text=msg)
    if postal[:2] in East:
        bot.sendMessage(chat_id='@CrisisNewsEast',text=msg)
    if postal[:2] in Central:
        bot.sendMessage(chat_id='@CrisisNewsCentral',text=msg)


""" - The function takes in 2 strings, the postal code and message and sends the message to
      the regional telegram channel @CrisisNews (see chat_id)
    - follow the channel to see the output """
