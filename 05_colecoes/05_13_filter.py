# Filter
nomes = ['Raquel', 'Emily', 'Silvanira', 'Jorge']

def pessoa_aprovada(pessoa):
    if pessoa == 'Emily':
        return True
    else:
        return False

print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))


pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

def e_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False
    
print(list(filter(e_antiguidade, pinturas)))