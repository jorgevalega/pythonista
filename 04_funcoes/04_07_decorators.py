from datetime import datetime

def depositar_dinheiro():
    print('depositando dinheiro')

    def depositando_dolar():
        print('Depositando dolares')

    def depositando_reais():
        print('Depositnado reais')
    
    depositando_dolar()
    depositando_reais()

depositar_dinheiro()


def pai(numero):
    def filho_1():
        print('Sou filho 1')
    def filho_2():
        print('Sou filho 2')
    if numero == 1:
        return filho_1

resultado = pai(1)
resultado()


# Decorators

def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

@meu_decorator
def parabenizar():
    print('Parabéns!!!!')

parabenizar()