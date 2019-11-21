import vlc
import pafy
import urllib.request
import time

url = "https://www.youtube.com/watch?v=0197axfuVwM"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
ins = vlc.Instance()
player = ins.media_player_new()

code = urllib.request.urlopen(url).getcode()

Media = ins.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()

good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
while str(player.get_state()) in good_states:
    print('Stream is working. Current state = {}'.format(player.get_state()))
print('Stream is not working. Current state = {}'.format(player.get_state()))

timeout = time.time() + 20   # 20 seconds from now
while True:
    if time.time() > timeout:
        player.stop()

player.stop()