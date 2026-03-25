from pytubefix import YouTube
from pytubefix.cli import on_progress

print("Digite a URL do vídeo do Youtube")
url = input("URL: ").strip()

if "youtube.com" not in url and "youtu.be" not in url:
    print("Link inválido")
    exit()

try:
    yt = YouTube(url)
except Exception:
    print("Vídeo inválido ou indisponível")
    exit()
    
yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
print(yt.title)
ys.download(output_path=r"D:\Projetos\Baixar MP4 Youtube\Vídeos Baixados")