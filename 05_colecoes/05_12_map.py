# Como podemos criar listas?
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)

# Usando Map
nomes = ['Raquel', 'Emily', 'Teresa', 'Alcides']

def aprovar_pessoa(nome):
    # Lógica mais complexa
    # Lógica mais complexa
    # Lógica mais complexa
    return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))