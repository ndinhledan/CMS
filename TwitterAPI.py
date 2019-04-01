from twitter import *  #To install twitter go cmd install twitter

def tweets(postal,msg):
    North = frozenset(["No","28","29","30","31","32","33","34","35","36","37","53","54","55","56","57","72","73","75","76","77","78","79","80","82"])
    West = frozenset(["We","60","61","62","63","64","65","66","67","68","69","70","71"])
    East = frozenset(["Ea","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","81"])
    Central = frozenset(["Ce","01","02","03","04","05","06","07","08","18","19","20","21","22","23","24","25","26","27","58","59"])
    South = frozenset(["So","09","10","11","12","13","14","15","16","17"])
    if postal[:2] in Central:
        consumer_secret = "RovByO651oMYjW2FZBNIoqln5KCzGenHUZhQp1sI2sQ1C40PF0"
        consumer_key = "qrAPyHP7ZYMZSd7Kn8nVbf7i6"
        access_token = "1101179444536913921-PRqmL9I3IxOeFEIdQa8RlKPnU1af6n"
        access_token_secret = "K5AzZZv6KPin09mhTlJDpo6LHVawBze2ENZX8Ti4NqAW5"
        t = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
        t.statuses.update(status=msg)
    if postal[:2] in West:
        consumer_secret = "6Mlxoupjsb85L5IycvB4zDMp5uTKUpwXxs11vn7p6KdNIhpo9L"
        consumer_key = "Kjpx08fQIjN2KgB7J3hcNO1DW"
        access_token = "1101179444536913921-LYKUYDLY7XrJsRIxFZa4UP9zwDlQvr"
        access_token_secret = "psDvc1Q8wvXBS9g3gzQ0eLeBgIggWe3a7emsXkxoaYjVy"
        t = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
        t.statuses.update(status=msg)
    if postal[:2] in North:
        consumer_secret = "8bA26bqUSaYHZ2dVJxlopHACTfZFdvouoJZrrB9mfq7pFdNqnE"
        consumer_key = "PVtcH1a45wCzhkwJPebmDwTFo"
        access_token = "1101179444536913921-JtGIhwZECfSY5Qo6DV2DKYSmJEMFGf"
        access_token_secret = "8ogRUKImZK9HKYH6QjGFeglx1iCQY750nuRZ3kaXTa6V1"
        t = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
        t.statuses.update(status=msg)



def main():
    consumer_secret = "8bA26bqUSaYHZ2dVJxlopHACTfZFdvouoJZrrB9mfq7pFdNqnE"
    consumer_key = "PVtcH1a45wCzhkwJPebmDwTFo"
    access_token = "1101179444536913921-JtGIhwZECfSY5Qo6DV2DKYSmJEMFGf"
    access_token_secret = "8ogRUKImZK9HKYH6QjGFeglx1iCQY750nuRZ3kaXTa6V1"
    t = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
    t.statuses.update(status='hi guy have a good day =)')

if __name__ == '__main__':
    main()
