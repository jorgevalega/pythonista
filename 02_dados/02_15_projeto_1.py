from datetime import datetime

# ​PROJETO 1 

## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1


# 1. Obtenha o nome do usuário
nome_usuario = input('Digite seu nome: ')

# 2. Obtenha a idade do usuário
data_nascimento_str = input('Insira sua data de nascimento (dd/mm/AAAA): ')

try:
    data_nascimento = datetime.strptime(data_nascimento_str, '%d/%m/%Y')
    data_cadastro = datetime.now()
    idade_usuario = data_cadastro.year - data_nascimento.year
    if (data_cadastro.month, data_cadastro.day) < (data_nascimento.month, data_nascimento.day):
        idade_usuario -= 1
    
    print(f'{nome_usuario} sua idade é: {idade_usuario} anos')
except ValueError:
    print('Formato de data inválido. Por favor, use o formato dd/mm/AAAA')


    




# 3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

# 4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:

# cartoes = ['R$50,00','R$250,00','R$120,00']

# 5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)




## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!
'''
Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).

Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''