# O que são os arquivos JSON (Javascript Object Notation)
# É parecido com o dicionario de python
import json

with open('usuarios1.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter JSON -> String
    print(data["nome"])

with open('usuarios2.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["permissões"][1])

with open('usuarios3.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuarios"][0]["telefone"])
    print(data["usuarios"][1]["admin"])

with open('usuarios4.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuarios"][0]["plano"]["preco"])

with open('usuarios5.json',encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data[0]["admin"])