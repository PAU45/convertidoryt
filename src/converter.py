from moviepy.editor import VideoFileClip
import os

def convert_to_mp3(video_path, output_path="downloads/audios"):
    """
    Convierte un video a MP3.
    """
    try:
        print(f"Intentando abrir el archivo de video: {video_path}")
        if not os.path.exists(video_path):
            print(f"El archivo {video_path} no existe.")
            return None
        video = VideoFileClip(video_path)
        audio_path = video_path.replace(" video.mp4", ".mp3").replace("videos", "audios")
        video.audio.write_audiofile(audio_path)
        video.close()  # Cerrar el archivo de video después de la conversión
        print(f"Audio guardado como: {audio_path}")
        return audio_path
    except IOError as e:
        print(f"Error al abrir el archivo de video: {e}")