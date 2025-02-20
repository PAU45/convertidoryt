import os

def create_folders():
    """
    Crea las carpetas necesarias si no existen.
    """
    folders = ["downloads/videos", "downloads/audios"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)