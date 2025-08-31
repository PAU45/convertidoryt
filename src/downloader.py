from pytubefix import YouTube
from pytubefix.exceptions import VideoUnavailable
import urllib.error
import os

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream is None:
            print("No se encontró un stream adecuado para descargar.")
            return None
        # Limpiar el título para que sea válido en Windows
        invalid_chars = '<>:"/\\|?*'
        clean_title = ''.join(c for c in yt.title if c not in invalid_chars)
        video_title = clean_title + " video.mp4"
        video_path = f"downloads/videos/{video_title}"
        stream.download(output_path="downloads/videos", filename=video_title)
        print(f"Video descargado como: {video_path}")
        return video_title
    except VideoUnavailable:
        print("El video no está disponible.")
    except urllib.error.HTTPError as e:
        print(f"Error HTTP: {e.code} - {e.reason}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
