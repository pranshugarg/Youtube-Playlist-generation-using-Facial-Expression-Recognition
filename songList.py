import json
import requests

def get_songs_list(valence, arousal):

	api_url = "http://musicovery.com/api/V6/playlist.php?&fct=getfrommood&popularitymax=100&popularitymin=10&starttrackid=&date10=true&trackvalence="+str(valence)+"&trackarousal="+str(arousal)+"&resultsnumber=50&listenercountry=91"
	# print(api_url)

	res = requests.get(api_url)

	songs = []

	if(res.status_code == 200):
		data = res.json()
		tracks = data['tracks']['track']

		# print(tracks)
		# print()

		for i in tracks:
			if(i['title'] == '' or i['artist_display_name'] == ''):
				continue
			
			song = i['artist_display_name'] + ' ' + i['title']

			songs.append(song)
	else:
		print('Error')

	return songs