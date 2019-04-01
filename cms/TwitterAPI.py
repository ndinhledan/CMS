from twitter import *  #To install twitter go cmd install twitter

def tweets(postal,msg):
    North = frozenset(["No","28","29","30","31","32","33","34","35","36","37","53","54","55","56","57","72","73","75","76","77","78","79","80","82"])
    West = frozenset(["We","60","61","62","63","64","65","66","67","68","69","70","71"])
    East = frozenset(["Ea","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","81"])
    Central = frozenset(["Ce","01","02","03","04","05","06","07","08","18","19","20","21","22","23","24","25","26","27","58","59"])
    South = frozenset(["So","09","10","11","12","13","14","15","16","17"])

    consumer_secret = "RovByO651oMYjW2FZBNIoqln5KCzGenHUZhQp1sI2sQ1C40PF0"
    consumer_key = "qrAPyHP7ZYMZSd7Kn8nVbf7i6"
    access_token = "1101179444536913921-PRqmL9I3IxOeFEIdQa8RlKPnU1af6n"
    access_token_secret = "K5AzZZv6KPin09mhTlJDpo6LHVawBze2ENZX8Ti4NqAW5"
    t = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
    if postal[:2] in North:
        t.statuses.update(status=msg + '\n#NorthRegion')
    if postal[:2] in West:
        t.statuses.update(status=msg + '\n#WestRegion')
    if postal[:2] in South:
        t.statuses.update(status=msg + '\n#SouthRegion')
    if postal[:2] in Central:
        t.statuses.update(status=msg + '\n#CentralRegion')
    if postal[:2] in East:
        t.statuses.update(status=msg + '\n#EastRegion')
    



