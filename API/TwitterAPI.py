from twitter import *  #To install twitter go cmd install twitter

consumer_secret = "RovByO651oMYjW2FZBNIoqln5KCzGenHUZhQp1sI2sQ1C40PF0"
consumer_key = "qrAPyHP7ZYMZSd7Kn8nVbf7i6"

access_token = "1101179444536913921-PRqmL9I3IxOeFEIdQa8RlKPnU1af6n"
access_token_secret = "K5AzZZv6KPin09mhTlJDpo6LHVawBze2ENZX8Ti4NqAW5"

t = Twitter(auth = OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

t.statuses.update(status="Posting to twitter from Python. #python")





