from datetime import datetime
# Desafio: calcule quantos dias faltam até o seu aniversário
hoje = datetime.now()
aniversario = datetime.strptime(input('Quando é seu próximo aniversário? (dia/mês/ano): '),'%d/%m/%Y')
quantidade_dias = aniversario - hoje
horas = quantidade_dias
print(f'Faltam {quantidade_dias.days} dias')