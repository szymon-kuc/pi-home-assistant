import json
import time
import urllib.request
import requests
from gtts import gTTS 
import os
import datetime

API = "mnoaAGSAAtyozykbpx6Iz0iyf5XOX1qs"
LOCATION_ID = 275789
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

def weather_commands(content):
    if("now" in content):
        current_weather()
    if("tomorrow" in content):
        forecasts(1,"")
    if("days" in content):
        words = content.split()
        day = words[words.index("days") - 1]
        if(day == "three"):
            day = 3
        try:
            forecasts(int(day),"")
        except:
            print("err", day)
    if any(el in content for el in days):
        day = [el for el in days if(el in content)]
        day_index = dow(datetime.date.today(), day[0])
        print(day_index)
        forecasts(day_index, day[0])


def dow(date, day):
    days_2={"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    dayNumber=date.weekday()
    diff = days_2[day] - dayNumber
    if(diff < 0 ):
        diff = diff +7
    return diff

def get_forecast(api, location_id, i):
    url = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/%s?apikey=%s&details=false&metric=true' % (location_id, api)
    print(url)
    try:
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return (data["DailyForecasts"][i]["Day"]["IconPhrase"],
                data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"])
    except urllib.error.HTTPError as err:
        return ([err])

def get_current_weather(api, location_id):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (location_id, api)
    print(url)
    try:
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return (data[0]['Temperature']['Metric']['Value'],
                data[0]['WeatherText'],
                data[0]['Wind']['Speed']['Metric']['Value'])
    except urllib.error.HTTPError as err:
        return ([err] * 3)


timestamp = time.time()


def current_weather():
    temperature, weather_text, wind_speed = get_current_weather(API, LOCATION_ID)

    answer = "It’s" + weather_text + ". The temperature is " + str(temperature)+ " degrees. The wind blows at speed " + str(wind_speed) + " kilometers per hour"
    speech = gTTS(text = answer, lang = 'en', slow = False)
    speech.save("text.mp3")
    os.system("mpg123 text.mp3")

def forecasts(i, day):
    weather_text, temp = get_forecast(API, LOCATION_ID, i)
    answer = ""
    if(i==1):
        answer = "Tomorrow will be " + weather_text + ". The temperature will be " + str(temp) + " degrees"
    if(i > 1):
        if(day!=""):
            answer = "On " + day + " will be " + weather_text + ". The temperature will be " + str(temp) + " degrees"
        else:
            answer = "In " + str(i) + " days will be " + weather_text + ". The temperature will be " + str(temp) + " degrees"
    if(i > 5 or i == 0):
        answer = "Sorry, this is only 5-days forecast"
    speech = gTTS(text = answer, lang = 'en', slow = False)
    print(answer)
    speech.save("text.mp3")
    os.system("mpg123 text.mp3")

