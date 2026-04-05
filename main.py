from audio import baixar_audio
from video import baixar_video
from video_hd import baixar_video_hd


def main():
    print("\n=== YouTube Downloader ===")
    print("[1] Baixar vídeo (qualidade padrão)")
    print("[2] Baixar áudio")
    print("[3] Baixar vídeo HD (requer FFmpeg)")

    try:
        opcao = int(input("\nEscolha a opção: "))
    except ValueError:
        print("Opção inválida.")
        return

    if opcao == 1:
        url = input("Digite o link do vídeo: ").strip()
        try:
            baixar_video(url)
        except Exception as e:
            print(f"Erro: {e}")

    elif opcao == 2:
        url = input("Digite o link do vídeo: ").strip()
        try:
            baixar_audio(url)
        except Exception as e:
            print(f"Erro: {e}")

    elif opcao == 3:
        url = input("Digite o link do vídeo: ").strip()
        try:
            baixar_video_hd(url)
        except EnvironmentError as e:
            print(f"\n[AVISO] {e}")
        except Exception as e:
            print(f"Erro: {e}")

    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
