from datetime import datetime
import random

print('------------------ Bem-vindo a o sistema ------------------')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
data_cadastro = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
cartao = random.choice(cartoes)
aniversario = datetime.strptime(input('Digite sua data de anivarsário no formato dd/mm/aaaa: '), '%d/%m/%Y')

print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {data_cadastro.day}/{data_cadastro.month}/{data_cadastro.year}.\nParabens, houve um sorteio e você ganhou um cartão de compras no valor de {cartao}')