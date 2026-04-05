import os
import shutil
import subprocess
import tempfile
from pytubefix import YouTube


def _validate_youtube(url):
    if not url or ("youtube.com" not in url and "youtu.be" not in url):
        raise ValueError("Link inválido: não é um link do YouTube")
    try:
        yt = YouTube(url)
    except Exception:
        raise ValueError("Vídeo inválido ou indisponível")
    return yt


def _check_ffmpeg():
    if not shutil.which("ffmpeg"):
        raise EnvironmentError(
            "FFmpeg não encontrado. Instale o FFmpeg e adicione ao PATH. "
            "Consulte o README para instruções de instalação."
        )


def _listar_qualidades(yt):
    """Retorna lista de streams de vídeo adaptativas (sem áudio), sem duplicatas de resolução."""
    streams = (
        yt.streams
        .filter(adaptive=True, only_video=True)
        .order_by("resolution")
        .desc()
    )

    vistas = set()
    unicas = []
    for s in streams:
        if s.resolution not in vistas:
            vistas.add(s.resolution)
            unicas.append(s)
    return unicas


def baixar_video_hd(url, output_path="Vídeos Baixados HD"):
    _check_ffmpeg()
    yt = _validate_youtube(url)

    qualidades = _listar_qualidades(yt)
    if not qualidades:
        raise ValueError("Nenhuma stream HD disponível para este vídeo.")

    # Exibe as qualidades disponíveis
    print("\nQualidades disponíveis:")
    for i, stream in enumerate(qualidades, start=1):
        fps_info = f" | {stream.fps}fps" if stream.fps else ""
        codec_info = f" | {stream.video_codec}" if stream.video_codec else ""
        print(f"  [{i}] {stream.resolution}{fps_info}{codec_info}")

    # Escolha do usuário
    while True:
        try:
            escolha = int(input("\nEscolha a qualidade (número): "))
            if 1 <= escolha <= len(qualidades):
                break
            print(f"Digite um número entre 1 e {len(qualidades)}.")
        except ValueError:
            print("Entrada inválida. Digite apenas o número.")

    stream_video = qualidades[escolha - 1]

    # Busca a melhor stream de áudio disponível
    stream_audio = (
        yt.streams
        .filter(only_audio=True)
        .order_by("abr")
        .last()
    )
    if not stream_audio:
        raise ValueError("Nenhuma stream de áudio disponível para este vídeo.")

    os.makedirs(output_path, exist_ok=True)

    # Nome base seguro para os arquivos temporários e final
    titulo = yt.title
    nome_seguro = "".join(c for c in titulo if c.isalnum() or c in " _-()[]").strip()
    resolucao = stream_video.resolution

    with tempfile.TemporaryDirectory() as tmp_dir:
        print(f"\nBaixando vídeo ({resolucao})...")
        caminho_video = stream_video.download(
            output_path=tmp_dir,
            filename="video_temp"
        )

        print("Baixando áudio...")
        caminho_audio = stream_audio.download(
            output_path=tmp_dir,
            filename="audio_temp"
        )

        nome_final = f"{nome_seguro} [{resolucao}].mp4"
        caminho_final = os.path.join(output_path, nome_final)

        print("Mesclando vídeo e áudio com FFmpeg...")
        comando = [
            "ffmpeg",
            "-i", caminho_video,
            "-i", caminho_audio,
            "-c:v", "copy",       # Copia o vídeo sem re-encodar (mais rápido)
            "-c:a", "aac",        # Converte áudio para AAC (compatível com MP4)
            "-b:a", "192k",
            "-movflags", "+faststart",  # Otimiza para streaming/reprodução rápida
            "-y",                 # Sobrescreve se já existir
            caminho_final
        ]

        resultado = subprocess.run(
            comando,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE
        )

        if resultado.returncode != 0:
            erro = resultado.stderr.decode("utf-8", errors="replace")
            raise RuntimeError(f"Erro ao mesclar com FFmpeg:\n{erro}")

    print(f'\nVídeo HD salvo em: "{caminho_final}"')
