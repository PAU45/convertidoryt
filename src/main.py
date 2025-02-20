from downloader import download_video
from converter import convert_to_mp3
from utils import create_folders
import os

def main():
    create_folders()
    url = input("Ingresa la URL del video de YouTube: ")
    format_choice = input("¿Quieres descargar el video en formato MP4 o convertirlo a MP3? (mp4/mp3): ").strip().lower()
    
    if format_choice not in ["mp4", "mp3"]:
        print("Opción no válida. Por favor, elige 'mp4' o 'mp3'.")
        return
    
    video_filename = download_video(url)
    if video_filename:
        video_path = f"downloads/videos/{video_filename}"
        print(f"Ruta del archivo de video: {video_path}")
        if not os.path.exists(video_path):
            print(f"El archivo {video_path} no existe.")
            return
        
        if format_choice == "mp3":
            mp3_path = convert_to_mp3(video_path)
            if mp3_path:
                os.remove(video_path)
                print(f"El video se ha convertido a formato MP3 y el archivo MP4 ha sido eliminado: {mp3_path}")
        else:
            print(f"El video se ha descargado en formato MP4: {video_path}")
    else:
        print("No se pudo descargar el video.")

if __name__ == "__main__":
    main()