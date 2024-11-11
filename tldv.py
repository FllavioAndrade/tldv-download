
from datetime import datetime
from os import system
import requests
import json



# Solicita ao usuário a URL da reunião
url = input("Please paste the URL of the meeting you want to download: ")

# Extrai o ID da reunião da URL
meeting_id = url.split("/")[-1]  # Extrai apenas o ID da reunião
print("\rFound meeting ID: ", meeting_id)

# Solicita o token de autenticação
auth_token = input("Auth token: ")

# Faz a solicitação HTTP para obter os dados da reunião
data = requests.get(
    f"https://gw.tldv.io/v1/meetings/{meeting_id}/watch-page?noTranscript=true",
    headers={
        "Authorization": f"Bearer {auth_token}",
    },
)

try:
    # Exibe o conteúdo da resposta para debug
    print("Response data:", data.text)
    
    # Analisa o JSON da resposta
    response = json.loads(data.text)
    
    # Extrai informações sobre a reunião
    meeting = response.get("meeting", {})
    name = meeting.get("name", "No name")
    createdAt = meeting.get("createdAt", datetime.now().isoformat())
    source = response.get("video", {}).get("source", None)

    if source is None:
        print("No video source found in the response.")
        exit()

    # Formata a data para o nome do arquivo
    date = datetime.strptime(createdAt, "%Y-%m-%dT%H:%M:%S.%fZ")
    normalised_date = date.strftime("%Y-%m-%d-%H-%M-%S")

    # Nomeia o arquivo de vídeo
    filename = f"{normalised_date}_{name}"
    filename_ext = ".mp4"

    # Comando ffmpeg para baixar o vídeo
    command = f'ffmpeg -i {source} -c copy "{filename}.{filename_ext}"'

    # Salva a resposta em um arquivo JSON para referência
    json_filename = f'{filename}.json'
    with open(json_filename, "w") as f:
        f.write(data.text)

    # Exibe o comando e inicia o download
    print("FFmpeg command:", command)
    print("Downloading video...")
    system(command)

except Exception as e:
    print("Error encountered:")
    print(e)
    print(data.text)
