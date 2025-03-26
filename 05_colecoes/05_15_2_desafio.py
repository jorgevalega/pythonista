import json

# Criar ou ler JSON existente
usuario_json = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true,
    "gpa": 3.5
}"""

# Salvar un string JSON -> Arquivo json
with open('desafio3.json','w',encoding='utf8') as arquivo_json:
    json.dump(usuario_json,arquivo_json)
    
# Para ler um arquivo JSON
with open('desafio3.json',encoding='utf-8') as arquivo_json:
    string_usuario_json = json.load(arquivo_json) # convertendo JSON -> String
    dicionario_usuario_json = json.loads(string_usuario_json)
    print(dicionario_usuario_json["name"])