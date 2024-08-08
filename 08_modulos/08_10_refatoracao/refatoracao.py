# Refatoração
# Renomear todas ocorrências - F2 - depois Ctrl+Enter 

class Calculadora:
    pass

calc1 = Calculadora()
calc2 = Calculadora()
calc3 = Calculadora()

print(calc1)

# Ctrl+Shift+p - Refactor - Extract Method

def resultados():
    resultado = 20 + 50

resultados()


# Ctrl+Shift+p - Refactor - Extract Variable
altura = 60
largura = 2
tamanho = (altura/largura) + 50