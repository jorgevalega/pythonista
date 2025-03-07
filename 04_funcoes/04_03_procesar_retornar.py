# Procesar VS Retornar

# Função que apenas procesa dados
print('Olá!')

# Funções que retornam dados
cidade = input('Qual é a sua cidade? ')
# Como escolher entre funções que processam VS retornam dados?
'''
Eu vou procesar de usar essa informação na lógica do meu programa ainda?
Ou só preciso processar eese dado, mas não irei utilizar mais ele depois?
'''
# Na seguinte função só está para informar a cotação do dolar
def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.85)

exibir_cotacao_do_dia('usd')

def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.85

cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('Investir em ações americanas')
else:
    print('Cotação não favorável')