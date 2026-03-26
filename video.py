from pytubefix import YouTube

def _validate_youtube(url):
    if not url or ("youtube.com" not in url and "youtu.be" not in url):
        raise ValueError("Link inválido: não é um link do YouTube")
    try:
        yt = YouTube(url)
    except Exception:
        raise ValueError("Vídeo inválido ou indisponível")
    return yt

def baixar_video(url, output_path="Vídeos Baixados"):
    yt = _validate_youtube(url)
    ys = yt.streams.get_highest_resolution()
    if not ys:
        raise ValueError("Nenhuma stream de vídeo disponível para este vídeo")
    ys.download(output_path="Vídeos Baixados")
    print("Vídeo baixado")