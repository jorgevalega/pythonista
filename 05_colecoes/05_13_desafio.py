# Desafio
vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]

def vagas_salario(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(vagas_salario, vagas)))