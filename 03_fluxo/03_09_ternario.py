# Caso a idade seja maior ou igual a 18 anos, essa pessoa
# é maior de idade, caso contrário ela é menor de idade.

idade = 15

if idade >= 18:
    print('maior de idade')
else:
    print('menor de idade')


# Expressão Condicional ou Operador Ternário
print('Maior de idade') if idade >= 18 else print('Menor de idade')
# expressão if condição else expressão


possui_passaporte = True
print('Favor embarcar') if possui_passaporte == True else print('Favor tirar passaporte')

# Desafio: 
velocidade = 80

print('Você foi multado') if velocidade > 100 else print('Siga em frente')