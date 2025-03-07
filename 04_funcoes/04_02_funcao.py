# Funções
# input()
# len()
# split()

# O que elas tem em comum?
'''
def nome_da_funcao(parametros):
    comandos
'''

def dar_boas_vindas():
    print('\n\nBem-vindo!')

dar_boas_vindas()

# Usar poucos parámetos para deixar as funções mais legiveis

def dar_boas_vindas_personalizada(nome):
    print(f'Bem-vindo(a) {nome}')

dar_boas_vindas_personalizada('Raquel')

# Valor padrão
def apresentar_lugar(horario_de_funcionamento,lugar='Nossa loja'): # O parámetro padrão sempre no final dos parámetros ou vai dar erro
    print(f'Conheça {lugar}, horário de funcionamento das {horario_de_funcionamento}')

apresentar_lugar('08:00 as 18:00', 'Disney')


#############################################################################
def gerar_nome_completo(nome, sobrenome):
    print(f'Welcome, {nome} {sobrenome}!')
gerar_nome_completo('Thiago', 'Henrique')
#############################################################################

def gerar_nome_completo2(nome2, sobrenome2):
    return f'Welcome, {nome2} {sobrenome2}!'

primeiro = input('Digite o primeiro nome: ')
segundo = input('Digite o segundo nome: ')
completo = gerar_nome_completo2(primeiro, segundo)
print(completo)

##############################################################################

def calcular_valores (preco, quantidade=1):
    print(preco * quantidade)
calcular_valores(2.25, 10)

##############################################################################
def calcular_valor2 (preco2, quantidade2=1):
    return preco2 * quantidade2

valor = float(input('Digite o valor do produto: '))
unidades = int(input('Digite a quantidade do produto: '))
multi = calcular_valor2(valor, unidades)
print(multi)