import os
import sys
import json
import spotipy
import webbrowser
import yaml
import spotipy.util as util
from json.decoder import JSONDecodeError
from .get_weather import *
from .config import *

def get_tracks(input):
	#client ID = 249fc495e1e34f8e81e25b2b0920f79b
	#data = get_data(input)
	data = input
	username = "581hxrshcy0yznmfveoc4cwl4"   #prob. a string

	token = util.prompt_for_user_token(username,'playlist-read-private', client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)
	sp = spotipy.Spotify(auth=token)

	user = sp.current_user()

	windyPlaylist = '1mQvg5NX8hwvETI3Ud6pws?si=QF1obWvpSRCzV_JixWEuRw'
	sunnyPlaylist = '4kIXGUdLiKqDnyPKHjtGy4?si=Xx_OT0qsQoejiLDhPnUi_w'
	cloudyPlaylist = '2I7TZYJy5qLtfowMCTLIkP?si=m22x99xNS_KiMS6oLDB9BQ'
	rainyPlaylist = '6N3EWQRQCMtrTeO6KSK0wR?si=BnofNgGNRfiFNYlWqPNkQQ'
	snowyPlaylist = '0DqgjK67u13ZQp7qNFdPKt?si=jjPm2I6zRTm-CI-3Sx1lUw'
	list = [sunnyPlaylist, rainyPlaylist, snowyPlaylist, cloudyPlaylist, windyPlaylist]

	if data["mood"] == "sunny":
		x = 0
	if data["mood"] == "rainy":
		x = 1
	if data["mood"] == "snowy":
		x = 2
	if data["mood"] == "cloudy":
		x =3
	if data["mood"] == "windy":
		x =4 
	
	result = sp.user_playlist(username,list[x])
	tracks = result['tracks']
	i = 0
	for i, item in enumerate(tracks['items']):
		track = item['track']
		#print(track['external_urls'])
		return track['external_urls']

#testing stuff don't mind it
"""data1 = get_data("20147")
data1 = get_mood(data1) 
data2 = get_tracks(data1)
track = json.dumps(data2["spotify"])
track2 = {}
track2['current'] = track.replace("https://open.spotify.com/track/", '')
print(track2)"""














