import yt_dlp
import os

#Descargador de Audio de Youtube, sirve para Playlist y para Videos sueltos.
def download_youtube_audio(url, output_path='./downloads'):
    # Crea el directorio si no existe
    os.makedirs(output_path, exist_ok=True)

    #Configuración de opciones de la libreria yt_ldp, es necesario instalar FFMPEG también.
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Change to preferred audio format if needed
            'preferredquality': '192',
        }],
    }
    try:
        #Descarga el audio de la URL.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error: {e}")

download_url = input("Copie la URL a descargar | Copy here the URL to download: \n")
download_youtube_audio(download_url)

