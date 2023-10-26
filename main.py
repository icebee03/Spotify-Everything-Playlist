import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

marvin_profile = "marvbrav_de"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.user_playlists("marvbrav_de")
playlists = results["items"]
while results["next"]:
    results = spotify.next(results)
    playlists.extend(results["items"])

for playlist in playlists:
    print(playlist["name"])

