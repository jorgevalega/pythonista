""" teclado = 'Teclado Teclado Teclado Teclado Teclado'
print(teclado[2])
print(teclado[4])
print(teclado[-1])
print(teclado.index('l'))
print(teclado[teclado.index('l')])

# Acessando partes de um string
link = 'facebook.com/jorgevalega'
print(link[0])
print(link[-1])
print(link[0:5])
print(link[0:])
print(link[-5:])
print(link[5:])
print(link[:-5])

frase = 'Clean Code'
print(frase.rindex('C')) """

# DESAFIO 1
# Encontre o índice de 'o' dentro da variable biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))


# DESAFIO 2
# Usando a frase seguinte imprima apenas 'De Aplicações'
frase2 = 'Dessenvolvimento De Aplicações'
indice_1 = frase2.rindex('D')
indice_2 = frase2.rindex('s') + 1

print(frase2[indice_1:indice_2]) 
