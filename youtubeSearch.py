from apiclient.discovery import build

# api key for youtube data v3 api from Google Developers Console
apiKey = 'AIzaSyBpLcSDoqug3tRjQHYUN3IOO1Jdhtzdu4c'

# get youtube Resource
youtube = build('youtube', 'v3', developerKey = apiKey)

def get_youtube_videoId(searchQuery):
	print('searching for ', searchQuery)
	request = youtube.search().list(q = searchQuery, part = 'snippet', type = 'video')
	resultVideos = request.execute()
	
	if(len(resultVideos['items']) == 0):
		return ''
	else:
		return resultVideos['items'][0]['id']['videoId']