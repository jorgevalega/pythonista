preco_1 = 10
preco_2 = 20
preco_3 = 30

# Listas
precos = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(precos[2]) # Acessar por índice
print(precos[precos.index(60)])

# Listas no Python são dinámicas (aceitam qualquer tipo de dado)
itens = [1,3,6,'Olá','Café',True,10.6]
print(itens[4])

# Maneiras diferentes de gerar uma lista
# Multiplicação de valores
lista_de_noves = [9] * 10
lista_de_testes = ['Teste'] * 10
print(lista_de_noves)
print(lista_de_testes)

# Usando gerador Range (Sequência)
# 1 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))

# Lista de lista (matriz)
matriz_de_nomes = [['Emily',4],['Raquel',38],['Jorge',48]]
print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(matriz_de_nomes[0][1])
print(matriz_de_nomes[1][1])
