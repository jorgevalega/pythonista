'''

1- Definir o objetivo da API:
ex: Iremos montar uma api de blog, onde eu poderei consultar, editar, criar e excluir postagens em um blog usando a API

2- Qual será o URL base do api?
ex: Quando você cria uma aplicação local ela terá um url tipo http://localhost:5000 , porém quando você for subir isso para nuvem, você terá que comprar ou usar um domínio como url base, vamos imaginar um exemplo de devaprender.com/api

3- Quais são os endpoints?
ex: Se seu requisito é de poder consultar, editar, criar e excluir, você terá que disponibilizar os endpoints para essas questões
> /postagens

4- Quais recursos será disponibilizado pelo api: informações sobre as postagens

5- Quais verbos http serão disponibilizados?
* GET
* POST
* PUT
* DELETE 

6- Quais são os URL completos para cada um?
http://localhost:5000/postagens

* GET http://localhost:5000/postagens
* GET id http://localhost:5000/postagens/1
* POST id http://localhost:5000/postagens
* PUT id http://localhost:5000/postagens/1
* DELETE id http://localhost:5000/postagens/1

'''

from flask import Flask, jsonify, request

app = Flask(__name__)
postagens = [
    {
        'título': 'Minha História',
        'autor': 'Amanda Dias'
    },
    {
        'título': 'Novo dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'título': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }    
]
# Rota padrão - GET http://localhost:7777
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem com id - GET http://localhost:7777/postagem/1
@app.route('/postagem/<int:indice>',methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Criar uma nova postagem - POST http://localhost:7777/postagem
@app.route('/postagem',methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem,200)

# Alterar uma postagem existente - PUT 
@app.route('/postagem/<int:indice>',methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice],200)

# Excluir uma postagem - DELETE http://localhost:7777/postagem/0
@app.route('/postagem/<int:indice>',methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi exclído a postagem {postagens[indice]}',200)
    except:
        return jsonify('Não foi possível encontrar a postagem para excluxão',404)



app.run(port=7777,host='localhost',debug=True)