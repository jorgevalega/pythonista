from datetime import datetime
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().fold)

# Criar uma data
lancamento_app = datetime(2025,1,3)
print(lancamento_app)

# Quero receber a data lançamento do meu aplicativo
data_lancamento = datetime.strptime(input('Quando devemos lançar o aplicativo?: '),'%d/%m/%Y')
print(data_lancamento)
print(type(data_lancamento))

# Calcular o intervalo entre datas
data_atual = datetime.now()
prazo = data_lancamento - data_atual
print(prazo.days)

# Desafio: calcule quantos dias faltam até o seu aniversário
hoje = datetime.now()
aniversario = datetime.strptime('14/01/2025','%d/%m/%Y')

quantidade_dias = aniversario - hoje
print(quantidade_dias)