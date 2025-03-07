from itertools import zip_longest

lista_letras = ['A', 'B', 'C', 'D', 'E']
lista_numeros = [1, 2, 3, 4, 6]

for letra,numero in zip(lista_letras,lista_numeros):
    print(letra)
    print(numero)

produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = [250, 150, 220, 550, 50]

for produto,preco in zip(produtos,precos):
    print(f'Salvando produto {produto} com valor R$ {preco}')

titulos = ['Título 1', 'Título 2', 'Título 3', 'Título 4']
descricoes = ['Descricao 1', 'Descricao 2', 'Descricao 3']

for titulo,descricao in zip_longest(titulos,descricoes):
    print(f'Encontramos o {titulo} descrição: {descricao}')