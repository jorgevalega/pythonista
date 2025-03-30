import os

frutas = ['Banana', 'Melancia', 'Maçã', 'Laranja', 'Limão']
cores = ['Amarelo', 'Verde', 'Marrão', 'Azul', 'Vermelho']
linguagens = ['Python', 'Java', 'Javascript', 'Cobol', 'Delphi']


# Desafio 1:
with open('frutas.txt', 'w', encoding='utf8', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

# Desafio 2:
with open('frutas.txt', 'r', encoding='utf8') as arquivo:
    for linha in arquivo:
        print(linha)

# Desafio 3:
with open('frutas.txt', 'a', encoding='utf8', newline='') as arquivo:
    for cor in cores:
        arquivo.write(cor + os.linesep)

# Desafio 4:
with open('Top 5 Linguagens.txt', 'w', encoding='utf8', newline='') as arquivo:
    for linguagem in linguagens:
        arquivo.write(linguagem + os.linesep) 

# Bonus:
numeros = range(5)
for numero in numeros:
    with open(f'arquivo_{numero}.txt', 'w') as arquivo:
        arquivo.write('')