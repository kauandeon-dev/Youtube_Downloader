from audio import baixar_audio
from video import baixar_video

def main():
    print("[1] Baixar vídeo")
    print("[2] Baixar áudio")

    try:
        opcao = int(input("Escolha a opção: "))
    except ValueError:
        print("Opção inválida")
        return

    if opcao == 1:
        url = input("Digite o link do vídeo: ").strip()
        try:
            baixar_video(url)
        except Exception as e:
            print(e)
    elif opcao == 2:
        url = input("Digite o link do áudio: ").strip()
        try:
            baixar_audio(url)
        except Exception as e:
            print(e)
    else:
        print("Opção inválida")


if __name__ == "__main__":
    main()