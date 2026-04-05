# YouTube Downloader

Projeto Python para baixar vídeos e áudios do YouTube utilizando a biblioteca **pytubefix**. Suporta download de vídeo padrão, somente áudio e vídeo em HD com escolha de qualidade (requer FFmpeg).

---

## Funcionalidades

- **[1] Baixar vídeo** — Baixa o vídeo na maior resolução disponível via stream progressiva
- **[2] Baixar áudio** — Extrai somente o áudio do vídeo
- **[3] Baixar vídeo HD** — Lista todas as resoluções disponíveis (ex: 4K, 1440p, 1080p, 720p...) e permite escolher a qualidade antes de baixar. Requer FFmpeg instalado.

---

## Pré-requisitos

- Python 3.8 ou superior
- pip
- FFmpeg *(obrigatório apenas para a opção HD — veja instruções abaixo)*

---

## Instalação do projeto

**1. Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

**2. Instale as dependências Python:**

```bash
pip install -r requirements.txt
```

**3. Execute o programa:**

```bash
python main.py
```

---

## Instalação do FFmpeg (obrigatório para vídeo HD)

O FFmpeg é necessário para mesclar streams de vídeo e áudio separadas, que é como o YouTube disponibiliza vídeos em alta definição (1080p, 1440p, 4K).

### Windows

**Opção 1 — Via Winget (recomendado, Windows 10/11):**

```powershell
winget install --id=Gyan.FFmpeg -e
```

**Opção 2 — Manualmente:**

1. Acesse [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Em *Windows*, clique em **Windows builds from gyan.dev**
3. Baixe o arquivo `ffmpeg-release-essentials.zip`
4. Extraia o conteúdo para uma pasta, por exemplo: `C:\ffmpeg`
5. Adicione o FFmpeg ao PATH do sistema:
   - Abra **Painel de Controle → Sistema → Configurações avançadas do sistema → Variáveis de Ambiente**
   - Em *Variáveis do sistema*, selecione `Path` e clique em **Editar**
   - Clique em **Novo** e adicione: `C:\ffmpeg\bin`
   - Clique em **OK** em todas as janelas

6. Verifique a instalação abrindo o **Prompt de Comando** ou **PowerShell**:

```powershell
ffmpeg -version
```

---

### macOS

**Via Homebrew (recomendado):**

```bash
brew install ffmpeg
```

Se não tiver o Homebrew instalado, instale primeiro:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Verifique a instalação:

```bash
ffmpeg -version
```

---

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg
```

**Fedora / RHEL / CentOS:**

```bash
sudo dnf install ffmpeg
```

**Arch Linux:**

```bash
sudo pacman -S ffmpeg
```

Verifique a instalação:

```bash
ffmpeg -version
```

---

## Verificando se o FFmpeg está configurado corretamente

Após a instalação, execute o seguinte comando no terminal:

```bash
ffmpeg -version
```

A saída esperada começa com algo como:

```
ffmpeg version 7.x.x Copyright (c) 2000-2024 the FFmpeg developers
```

Se o comando não for reconhecido no Windows, revise o passo de configuração do PATH e reinicie o terminal.

---

## Problemas com PATH no Windows (VSCode)

Se você instalou o FFmpeg mas o programa ainda exibe *"FFmpeg não encontrado"*, o problema mais comum é que o terminal do VSCode não reconheceu o PATH atualizado.

**Solução 1 — Fechar e reabrir o VSCode** *(resolve na maioria dos casos)*

Feche o VSCode completamente e abra novamente. Abra o terminal integrado e teste:

```powershell
ffmpeg -version
```

**Solução 2 — Verificar se o PATH foi configurado**

No terminal do VSCode, execute:

```powershell
echo $env:PATH
```

Procure na lista um caminho como `C:\ffmpeg\bin`. Se não aparecer, o PATH não foi salvo. Execute o comando abaixo no PowerShell **como administrador** para adicioná-lo permanentemente:

```powershell
[System.Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\ffmpeg\bin", "Machine")
```

Ajuste `C:\ffmpeg\bin` para o caminho real onde está o `ffmpeg.exe` na sua máquina. Depois feche e reabra o VSCode.

**Solução 3 — Informar o caminho diretamente no código** *(ignora o PATH completamente)*

Se preferir não mexer nas variáveis de ambiente, edite o arquivo `video_hd.py` e substitua a constante no topo do arquivo:

```python
# Linha a editar em video_hd.py
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"  # ajuste para o seu caminho real
```

> Esse problema é mais comum quando o projeto está em um disco diferente do Windows (ex: projeto no disco `D:` e FFmpeg instalado no `C:`). O disco do projeto não afeta o PATH — o que importa é reiniciar o VSCode após a instalação.

---

## Estrutura do projeto

```
├── main.py           # Ponto de entrada — menu interativo
├── video.py          # Lógica de download de vídeo padrão
├── video_hd.py       # Lógica de download HD com escolha de qualidade + FFmpeg
├── audio.py          # Lógica de download de áudio
├── requirements.txt  # Dependências Python
├── Vídeos Baixados/  # Pasta criada automaticamente para vídeos
├── Áudios Baixados/  # Pasta criada automaticamente para áudios
└── README.md
```

---

## Dependências principais

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| pytubefix | 10.3.8 | Fork atualizado do pytube para download do YouTube |
| aiohttp | 3.13.3 | Cliente HTTP assíncrono |

Todas as dependências estão listadas em `requirements.txt`.

---

## Observações

- Os vídeos e áudios são salvos nas pastas **`Vídeos Baixados`** e **`Áudios Baixados`**, criadas automaticamente no diretório onde o script for executado.
- O arquivo final do vídeo HD é salvo com o nome do título + resolução escolhida, ex: `Meu Video [1080p].mp4`.
- O vídeo HD é processado em uma pasta temporária e mesclado automaticamente — nenhum arquivo intermediário fica salvo.
- Este projeto é destinado a uso pessoal. Respeite os Termos de Serviço do YouTube ao utilizá-lo.
