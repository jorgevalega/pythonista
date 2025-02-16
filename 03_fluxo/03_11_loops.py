# Loops aninhados
# Pais + Estação

paises = ['Brasil', 'Chile', 'Argentina']
estacoes = ['Primavera', 'Verão', 'Outono', 'Inverno']

for pais in paises:
    for estacao in estacoes:
        print(f'{pais} {estacao}')

for x in range(1, 11):
    for y in range(1, 6):
        print(f'Valor externo {x} e interno {y}')