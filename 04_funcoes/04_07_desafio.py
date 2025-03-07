from datetime import datetime

def meu_decorator(funcao):
    def wrapper():
        print(datetime.now().time())
        funcao()
        print(datetime.now().time())
    return wrapper

@meu_decorator
def parabenizar():
    print('Parabéns!!!!')

parabenizar()