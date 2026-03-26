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
streams = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc()

print("\nQualidades disponíveis:")
for i, stream in enumerate(streams):
    tamanho = round(stream.filesize / 1024 / 1024, 2) if stream.filesize else "?"
    print(f"[{i}] {stream.resolution} - {tamanho} MB")

escolha = int(input("\nEscolha o índice: "))
ys = streams[escolha]
print(yt.title)
ys.download(output_path=r"Vídeos Baixados")