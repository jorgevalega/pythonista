# **kwargs (Keyword arguments)
def concatenar(**palavras):
    frase = ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nos', b='somos', c='Pythonistas', d='Profissionais')


def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)

fazer_calculo('Raquel',4,5,6,7,a=1,b=2,c=3,d=4)



def exemplo(nome, *args, **kwargs):
    print("Nome:", nome)
    print("Args:", args)      # args é uma tupla
    print("Kwargs:", kwargs)   # kwargs é um dicionário

exemplo("João", "a", "b", "c", idade=30, cidade="São Paulo")