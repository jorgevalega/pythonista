'''

1- Definir o objetivo da API:
ex: Iremos montar uma api de músicas, onde deverá ser possível, consultar todas canções disponíveis, consultar uma canção individual, editar canções existentes e também excluir músicas existentes.

2- Qual será o URL base da API?
Iremos utilizar o URL base http://localhost:5000 

3- Quais são os endpoints?
Disponibilize endpoints para consulrar, editar, criar e excluir

4- Quais recursos serão disponibilizados pela API?
Informações sobre canções

5- Quais verbos http serão disponibilizados?
* GET
* POST
* PUT
* DELETE 

6- Quais são os URLs completos para cada um?
http://localhost:5000/postagens

* GET http://localhost:5000/cancoes
* GET http://localhost:5000/cancoes/1
* POST http://localhost:5000/cancoes
* PUT http://localhost:5000/cancoes/1
* DELETE http://localhost:5000/cancoes/1

7- Qual deve ser a estrutura de cada canção
* Lista de dicionários, que contem canção e estilo


'''

from flask import Flask, jsonify, request

app = Flask(__name__)
cancoes = [
    {
        'cancao': 'Fricote',
        'estilo': 'Axé'
    },
    {
        'cancao': 'O Som do Tambor',
        'estilo': 'Pagode'
    },
    {
        'cancao': 'Patricinha de Olho Azul',
        'estilo': 'Samba'
    }    
]
# Rota padrão http://localhost:5000
@app.route('/')
def obter_cancoes():
    return jsonify(cancoes)

# Obter canções - GET http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>',methods=['GET'])
def obter_cancoes_por_indice(indice):
    return jsonify(cancoes[indice])

# Criar uma nova canção - POST http://localhost:5000/cancoes
@app.route('/cancoes',methods=['POST'])
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(cancao,200)

# Alterar uma canção existente - PUT 
@app.route('/cancoes/<int:indice>',methods=['PUT'])
def alterar_cancao(indice):
    cancao_alterada = request.get_json()
    cancoes[indice].update(cancao_alterada)
    return jsonify(cancoes[indice],200)

# Excluir uma canção - DELETE http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>',methods=['DELETE'])
def excluir_cancao(indice):
    try:
        if cancoes[indice] is not None:
            del cancoes[indice]
            return jsonify(f'Foi exclída a canção {cancoes[indice]}',200)
    except:
        return jsonify('Não foi possível encontrar a cancão para excluxão',404)



app.run(port=5000,host='localhost',debug=True)