# Valores aleatórios com random
import random
print(' ')
print(random.random()) # Gera um valor de 0.0 a 1.0

# Gera um valor decimal de Valor Mínimo ao Valor Máximo
print(random.uniform(4,10))

# Gera un valor inteiro de Valor Mínimo ao Valor Máximo
print(random.randint(4, 10))

cores = ['verde','vermelho','azul'] # Escolher opção aleatória
print(random.choice(cores))
print(random.choices(cores, k=2))

cartas_baralho = ['carta1','carta2','carta3','carta4'] # Embaralhar uma lista
random.shuffle(cartas_baralho) # Não mostra aqui o resultado se quero imprimir
print(cartas_baralho)
