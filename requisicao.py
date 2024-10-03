import urllib
import json
from naoqi import ALProxy

def onLoad(self):
    # Este método será chamado quando a caixa for carregada
    pass

def onInput_onStart(self):
    # Configuração para a fala
    tts = ALProxy("ALTextToSpeech", "127.0.0.1", 9559)  # Substituir o IP pelo do robô (a porta geralmente é padrão)

    url = "https://jsonplaceholder.typicode.com/todos/1"

    try:
        response = urllib.urlopen(url)
        data = response.read()

        json_data = json.loads(data)

        # Pega o título do JSON e faz o robô falar
        title = json_data['title']
        tts.say("Title: " + title)
    except Exception as e:
        tts.say("Erro ao fazer a requisição.")
        print("Erro ao fazer a requisição:", e)

    self.onStopped()  # Notifica que a ação foi concluída
