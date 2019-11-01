#from dotenv import load_dotenv
#import os
#load_dotenv()
import requests
import pymongo

class WeatherGetter():
    
    def __init__(self, date = None):
        self.date = date + "T12:00:00"  #set default time to 12nn
        self.lat = 52.52 #Berlin
        self.long = 13.405 #Berlin
        self.key = "" #add key here
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


#sample response from darksky
#get value of icon or summary

#https://api.darksky.net/forecast/[    ]/52.52,13.405,2019-10-21T12:00:00?exclude=currently,hourly,flags
        
#{"latitude":52.52,"longitude":13.405,"timezone":"Europe/Berlin","daily":{"data":[{"time":1571608800,"summary":"Overcast throughout the day.","icon":"cloudy","sunriseTime":1571636580,"sunsetTime":1571673660,"moonPhase":0.76,"precipIntensity":0.0001,"precipIntensityMax":0.0003,"precipIntensityMaxTime":1571617800,"precipProbability":0.15,"precipType":"rain","temperatureHigh":63.5,"temperatureHighTime":1571669040,"temperatureLow":49.03,"temperatureLowTime":1571713200,"apparentTemperatureHigh":63,"apparentTemperatureHighTime":1571669040,"apparentTemperatureLow":48.9,"apparentTemperatureLowTime":1571713200,"dewPoint":54.28,"humidity":0.87,"pressure":1017,"windSpeed":4.44,"windGust":19.79,"windGustTime":1571608800,"windBearing":167,"cloudCover":0.93,"uvIndex":2,"uvIndexTime":1571655240,"visibility":6.216,"ozone":272,"temperatureMin":51.81,"temperatureMinTime":1571637060,"temperatureMax":63.5,"temperatureMaxTime":1571669040,"apparentTemperatureMin":52.3,"apparentTemperatureMinTime":1571637060,"apparentTemperatureMax":63,"apparentTemperatureMaxTime":1571669040}]},"offset":2}


class MongoHandler():
    def __init__(self, row_dict = None, collection = None):
        myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
        db = myclient["Project2"] #create or call Project2 db
        self.table = row_dict
        
        if collection == "team":
            team = db["Team_Names"]
            team.delete_many({})
            team.insert_many(self.table)
        elif collection == "goals":
            goals = db["Team_Goals"]
            goals.delete_many({})
            goals.insert_many(self.table)
        elif collection == "wins":
            wins = db["Team_Wins"]
            wins.delete_many({})
            wins.insert_many(self.table)
        elif collection == "winslosses":
            winslosses = db["Wins_and_Losses"]
            winslosses.delete_many({})
            winslosses.insert_many(self.table)
        elif collection == "rain":
            rain = db["Rain_Stats"]
            rain.delete_many({})
            rain.insert_many(self.table)
        
        
            
        
            
            
        