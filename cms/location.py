import requests

"""This class requires the requests library. Run 'pip install requests' """


#APIKEY = 'test'

"""Returns a tuple (lat, long)"""
def getCoordinates(zipcode):

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    
    
    params = {'address':zipcode, 'components':'country:SG', 'key':APIKEY}

    result = requests.get(url, params)
    try:
        data = result.json()
        lat = data['results'][0]['geometry']['location']['lat']
        long = data['results'][0]['geometry']['location']['lng']

    except:
        print("API Key Invalid, giving sample lat/long")
        lat = 1.355027
        long = 103.891234
    return (lat, long)

print(getCoordinates(680351))



