# Dicionários

'''
Pessoa
    nome
    idade
    altura
'''

pessoa = ['Raquel', 38, 1.74, 'Jorge', 48, 1.75]

# Dicionário (chave,valor)
dicionario_pessoa = {'nome':'Raquel', 'idade':38, 'altura':1.74}
pessoa_2 = dict(nome='Raquel', idade=38, altura=1.74)
print(pessoa)
print(dicionario_pessoa)
print(pessoa_2)
print(pessoa_2['idade'])
print(dicionario_pessoa.keys())
print(dicionario_pessoa.values())
print(dicionario_pessoa.items())

# Iterar sobre um dicionário
for item in dicionario_pessoa.items():
     print(item)
    #print(item[0])
    #print(item[1])

