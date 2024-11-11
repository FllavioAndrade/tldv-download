# tldv Video Downloader

Este script Python permite baixar gravações de reuniões do serviço [tldv.io](https://tldv.io/). Ao fornecer a URL de uma reunião e o token de autenticação, o script faz uma solicitação à API do tldv.io, obtém o link direto para o vídeo e o baixa usando `ffmpeg`.

## Requisitos

- Python 3.8+
- `ffmpeg` instalado e configurado no PATH
- Biblioteca `requests` para Python

## Instalação

1. Instale o `ffmpeg` (certifique-se de que está no PATH):
    ```bash
    # Para MacOS com Homebrew
    brew install ffmpeg
    ```

2. Instale o pacote `requests`:
    ```bash
    pip3 install requests
    ```
## Atenção

- **Segurança do Token:** O token de autenticação é sensível e deve ser mantido seguro. Não compartilhe o token nem o arquivo JSON salvo.
- **Armazenamento Local:** Certifique-se de que o arquivo JSON e o vídeo baixado estão protegidos, especialmente em um ambiente multiusuário.

## Como Usar

1. Acesse [tldv.io](https://tldv.io/) e faça login.
2. Vá até a reunião que deseja baixar e copie a URL da reunião.
3. Abra as ferramentas de desenvolvedor no navegador (pressione F12).
4. Vá até a aba de **Network** e recarregue a página.
5. Pesquise por `auth`.
6. Copie o **token de autenticação** dos cabeçalhos da requisição.
   ![Imagem](https://private-user-images.githubusercontent.com/124023264/331073198-cdca4fda-e126-460d-bc3d-05cc3a4eeb92.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzEzMzExMzcsIm5iZiI6MTczMTMzMDgzNywicGF0aCI6Ii8xMjQwMjMyNjQvMzMxMDczMTk4LWNkY2E0ZmRhLWUxMjYtNDYwZC1iYzNkLTA1Y2MzYTRlZWI5Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTExJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTExMVQxMzEzNTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kYzY4NTZhNjM0NTk3YTA0ZmE3MDhhYmM1ZWU0YzFlMDRkNWU5MmUxOTYxZDVjNjU0MGFkZmNjODNmMjVkYWY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.IdNIFjF6YgyrWk1m25evO2l5_D7UPQRf7h0OvSEHnRk)
8. Execute o script e insira a URL e o token quando solicitado:
    ```bash
    python3 tldv.py
    ```


## Exemplo

```plaintext
Please paste the URL of the meeting you want to download: https://gw.tldv.io/v1/meetings/64145828ced74b0013d496ce/watch-page?noTranscript=true
Found meeting ID: 64145828ced74b0013d496ce
Auth token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
FFmpeg command: ffmpeg -i https://video-source-url -c copy "2023-10-31-14-00-00_Meeting Title.mp4"
Downloading video...
```

## Erros Comuns
- "No video source found in the response": Certifique-se de que a URL e o token estão corretos. Se o token expirou, obtenha um novo.
- "Error encountered": Isso indica que houve algum problema na requisição ou no processamento da resposta. Verifique o token, a URL, e se o ffmpeg está configurado corretamente.
