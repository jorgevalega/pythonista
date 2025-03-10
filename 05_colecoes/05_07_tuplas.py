# Tuplas
site1 = 'youtube.com'
site1 = 'facebook.com'
site1 = 'instagram.com'

valor1 = 23
valor1 = 43
valor1 = 65

# Criação de tuplas, pode conter como as listas: strings, números, valores booleanos
# Não pode adicionar valores nas tuplas
sites = ('youtube.com', 'facebook.com', 'instagram.com')
valores = (23, 43, 65)

print(sites[1])
print(valores[2])

# União de tuplas
dados_do_sistema = sites + valores
print(dados_do_sistema)
print(dados_do_sistema[2])