frase = 'Olá, bem-vindo a este treinamento!'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))

nomes = 'Raquel, Emily, Jorge, Bela'
print(nomes.split())
print(nomes.split(','))

hastags = 'music #guitar #gamer #coder #python'
print(hastags.split())
print(hastags.split('#'))
print(hastags.split('#',3))

# Como concatenar (combinar) strings
hastags_separados_por_espaco = hastags.split(' ')
print(hastags_separados_por_espaco)
print(','.join(hastags_separados_por_espaco))
print('.'.join(hastags_separados_por_espaco))
print(' '.join(hastags_separados_por_espaco))

""" DESAFIOS
Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: 'Desafio, manipulação,de,strings'. Imprima o resultado no console.
Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = 'jhonatan & rafael & carol & camilla'. Imprima o resultado no console. """

frase1 = 'Desafio manipulação de strings'
frase2 = 'emily,raquel,jorge,bela'

# Desafio 1:
palavras1 = frase1.split()
print(palavras1)

# Desafio 2:
palavras2 = frase2.split(',')
print(palavras2)

# Desafio 3:
print(','.join(palavras1))

# Desafio 4:
palavras2 = frase2.split(',')
print(' & '.join(palavras2))
