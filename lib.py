# You don't have to use these classes, but we recommend them as a good place to start!



#from dotenv import load_dotenv
#import os
#load_dotenv()
import requests

class WeatherGetter():
    def __init__(self, date = None):
        self.date = date + "T12:00:00"  #set default time to 12nn
        self.lat = 52.52 #Berlin
        self.long = 13.405 #Berlin
        self.key = "dc40686a80b16d006b8747f0706e7215" #add key here
        self.link = f"https://api.darksky.net/forecast/{self.key}/{self.lat},{self.long},{self.date}?exclude=currently,hourly,flags"
        self.weather = self.getweathersummary()
        
    def getweathersummary(self):
        r = requests.get(self.link)
        response = r.json()
        try:
            response['daily']['data'][0]['icon'] 
        except:
            return response['daily']['data'][0]['summary']  #if there is no icon then get summary
        else:
            return response['daily']['data'][0]['icon']


        
#         self.BASE_URL = 'https://api.darksky.net'
#         self.token = os.getenv('DARKSKY')
#         if len(self.token) == 0:
#             raise ValueError('Missing API key!')


class MongoHandler():
    pass