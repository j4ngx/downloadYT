from pytube import Playlist
import os

# playlist's URL 
playlist_url = 'https://www.youtube.com/playlist?list=PLW2HgxBnfQmsG12hlRu8N_cHayKK9NsPn'

# Path where files will be downloaded
output_path = '/home/j4ngx/Music'

playlist = Playlist(playlist_url)

# Download each video of the playlist
for video in playlist.videos:
    try:
       # Download video and extract only the audio
        audio = video.streams.filter(only_audio=True).first()
        audio.download(output_path=output_path)

    # Change the name of the file audio for his original name
        default_filename = audio.default_filename
        os.rename(os.path.join(output_path, default_filename),
                 os.path.join(output_path, video.title + ".mp3"))
    except:
       continue
