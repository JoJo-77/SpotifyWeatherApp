import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError
from get_weather import data

def main()
	#client ID = 249fc495e1e34f8e81e25b2b0920f79b
	username = "581hxrshcy0yznmfveoc4cwl4"   #prob. a string

	token = util.prompt_for_user_token(username,'playlist-read-private')
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
	
	x = 1
	result = sp.user_playlist(username,list[x])
	tracks = result['tracks']
	i = 0
	for i, item in enumerate(tracks['items']):
        track = item['track']
        return track['external_urls']




















