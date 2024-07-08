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