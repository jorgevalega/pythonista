# *args
def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)

# Obrigatoriamente o último argumento tem que ser nomeado
somar(5,6,7,b=8)