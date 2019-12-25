import json
import time
import urllib.request
from gtts import gTTS 
import os

API = "mnoaAGSAAtyozykbpx6Iz0iyf5XOX1qs"
LOCATION_ID = 275789

def get_weather(api, location_id):
    url = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (location_id, api)
    print(url)
    try:
        with urllib.request.urlopen(url) as url:
            data = json.loads(url.read().decode())
        return (data[0]['Temperature']['Metric']['Value'],
                data[0]['RelativeHumidity'],
                data[0]['Wind']['Direction']['Degrees'],
                data[0]['Wind']['Speed']['Metric']['Value'],
                data[0]['UVIndex'],
                data[0]['CloudCover'],
                data[0]['Pressure']['Metric']['Value'],
                data[0]['Precip1hr']['Metric']['Value'],
                data)
    except urllib.error.HTTPError as err:
        return ([err] * 9)


timestamp = time.time()


def weather():
    temperature, humidity, wind_bearing, wind_speed, uv_index, cloud_cover, pressure, precipitation, raw \
    = get_weather(API, LOCATION_ID)

    answer = "It’s" + str(temperature) + "cold and windy outside. It's around 2.5 degrees"
    speech = gTTS(text = answer, lang = 'en', slow = False)
    speech.save("text.mp3")
    os.system("mpg123 text.mp3")