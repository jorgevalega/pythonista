def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')

# Argumentos posicionais
exibir_preco('Iphone', 5000)
exibir_preco(5000, 'Iphone')

# Argumentos nomeados
exibir_preco(nome_produto='Iphone', preco=5000)
exibir_preco(preco=5000, nome_produto='Iphone')