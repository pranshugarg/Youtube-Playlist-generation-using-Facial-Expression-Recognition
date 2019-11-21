import face as emotionValue
import json
import requests

emotion = get_emotion()

valence = 0
arousal = 0

if emotion == 'Happy':
    valence = 900000
    arousal = 900000
elif emotion == 'Sad':
    valence = 20000
    arousal = 20000
elif emotion == 'Angry':
    valence = 100000
    arousal = 700000
elif emotion == 'Neutral':
    valence = 700000
    arousal = 200000

api_url = "http://musicovery.com/api/V6/playlist.php?&fct=getfrommood&popularitymax=100&popularitymin=10&starttrackid=&date10=true&trackvalence="+str(valence)+"&trackarousal="+str(arousal)+"&resultsnumber=50&listenercountry=us"
print(api_url)

def get_songs_list():
    res = requests.get(api_url)
    if res.status_code == 200:
        data = res.json()
        print(data['tracks']['track'])
    else:
        print('Error')

get_songs_list()