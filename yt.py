import json
import requests
import subprocess
def play(querry):
    params = {
    'key': 'AIzaSyBsuc9kjdYHMOw82gKOu5rVrBq1o1Rf8pc',
    'q': querry,
    'part': 'snippet'
    }
    url ='https://www.googleapis.com/youtube/v3/search?'
    response = requests.get(url,params)
    result = json.loads(response.text)
    i = 0
    while result["items"][i]["id"]["kind"] != "youtube#video":
        i = i +1
    video_id = result["items"][i]["id"]["videoId"]
    subprocess.Popen(["node", "player.js", video_id])