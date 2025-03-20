from operator import itemgetter

# Desafio 1:
produtos = [
    {
        'nome': 'Celular',
        'preco': 1500
    },
    {
        'nome': 'Monitor',
        'preco': 500
    },
    {
        'nome': 'Microfone',
        'preco': 300
    }
]

produtos.sort(key=itemgetter('preco'))
print(produtos)

# Desafio 2:
equipamento_filmagem = [
    ('Tripé', 300),
    ('Camera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

# Desafio 3:
cotacao_moeda = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]

cotacao_moeda.sort(key=itemgetter(1))
print(cotacao_moeda)