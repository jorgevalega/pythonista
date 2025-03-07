from itertools import zip_longest

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for produto,preco in zip_longest(produtos,precos):
    print(f'Produto: {produto} encontrado no valor de {preco}')