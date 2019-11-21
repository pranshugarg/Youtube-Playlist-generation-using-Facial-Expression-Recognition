import vlc
import pafy

youtubeUrl = url = 'https://www.youtube.com/watch?v='

media = []

def play_song(videoId):
	global media
	url = youtubeUrl + videoId
	video = pafy.new(url)
	best = video.getbest()
	media = vlc.MediaPlayer(best.url)
	media.play()

def stop():
	global media
	media.stop()

def pause():
	global media
	media.pause()

def resume():
	global media
	media.play()