import json
# criar ou ler JSON existente
computador_json = """{
    "marca": "Dell",
    "preço": 15000
}"""

# Lendo m string JSON
data = json.loads(computador_json)
print(data["preço"])

# Salvar um string JSON -> Arquivo JSON
with open('computador.json','w', encoding='utf8') as arquivo_json:
    json.dump(computador_json,arquivo_json)

# Para ler um arquivo JSON
with open('computador.json',encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # convertendo JSON -> String
    dicionario_computador_json = json.loads(string_computador_json)
    print(dicionario_computador_json["marca"])