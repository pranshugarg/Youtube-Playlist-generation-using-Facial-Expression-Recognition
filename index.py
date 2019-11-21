import songList
# import face as emotionValue

# emotion = get_emotion()
emotion = 'Happy'

valence = 0
arousal = 0

if emotion == 'Happy':
	valence = 900000
	arousal = 900000
elif emotion == 'Sad':
	valence = 200000
	arousal = 200000
elif emotion == 'Angry':
	valence = 100000
	arousal = 700000
elif emotion == 'Neutral':
	valence = 700000
	arousal = 200000


songList.play_songs(valence, arousal)