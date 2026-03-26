from pytubefix import YouTube

def _validate_youtube(url):
    if not url or ("youtube.com" not in url and "youtu.be" not in url):
        raise ValueError("Link inválido: não é um link do YouTube")
    try:
        yt = YouTube(url)
    except Exception:
        raise ValueError("Vídeo inválido ou indisponível")
    return yt

def baixar_audio(url, output_path="Áudios Baixados"):
    yt = _validate_youtube(url)
    ys = yt.streams.filter(only_audio=True).first()
    if not ys:
        raise ValueError("Nenhuma stream de áudio disponível para este vídeo")
    if output_path:
        ys.download(output_path="Áudios Baixados")
    else:
        ys.download()
    print("Áudio baixado")