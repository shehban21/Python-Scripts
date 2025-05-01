#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Replace with your own Spotify app credentials
CLIENT_ID = 'your_client_id_here'
CLIENT_SECRET = 'your_client_secret_here'
REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'playlist-read-private playlist-read-collaborative'

# Setup authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

# Access token (optional to print)
token_info = sp.auth_manager.get_access_token()
print("Access token:", token_info['access_token'])

# Replace with your desired playlist ID or URI
playlist_id = 'spotify:playlist:37i9dQZF1DXcBWIGoYBM5M'

# Fetch playlist details
playlist = sp.playlist(playlist_id)

# Print playlist name and tracks
print(f"\nPlaylist: {playlist['name']}")
print("Tracks:")
for item in playlist['tracks']['items']:
    track = item['track']
    print(f"- {track['name']} by {', '.join([artist['name'] for artist in track['artists']])}")

