# Ordenar por propriedades
from operator import itemgetter
nomes = ['Emily', 'Raquel', 'Jorge', 'Alcides']
valores = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]
nomes.sort()
valores.sort()
print(nomes)
print(valores)

# Ordenar um dicionário ou algúm tipo de coleção 
# que possui uma chave podemos ordenar com itemgetter
pessoas = [
    {'nome': 'Emily',
     'idade': 4,
     'nivel_acesso': 2},
     {'nome': 'Raquel',
      'idade': 38,
      'nivel_acesso': 3},
      {'nome': 'Jorge',
     'idade': 48,
     'nivel_acesso': 5},
     {'nome': 'Alcides',
      'idade': 79,
      'nivel_acesso': 1},
]

pessoas.sort(key=itemgetter('nome'))
print(pessoas)

# Lista de tuplas 
# (nesse caso como não tem uma chave podemos ordenar pelo índice)
produtos = [
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550),
]

produtos.sort(key=itemgetter(1), reverse=True)
print(produtos)

# Ordenar matriz de dados
matriz = [[5, 10], [15, 21], [1, 5],]

matriz.sort(key=itemgetter(0), reverse=True)
print(matriz)