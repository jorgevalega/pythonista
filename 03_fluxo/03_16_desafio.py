import turtle

# Configuração inicial
screen = turtle.Screen()
screen.title('Movendo a tartaruga')
t = turtle.Turtle()
t.speed(3)
t.shape('turtle')
t.color('green')

# Função para mover a tartaruga
def mover_tartaruga(direcao, pixeis, rotacao, angulo):
    if rotacao == 'e':
        t.left(angulo)
    elif rotacao == 'd':
        t.right(angulo)
    if direcao == 'f':
        t.forward(pixeis)
    elif direcao == 't':
        t.backward(pixeis)

# Laço principal do programa
while True:
    # Solicitar direção
    direcao = input('\nPara qual direção devemos ir (f:frente / t:trás / s:sair): ').lower()
    if direcao == 's':
        print('Saindo do programa...')
        break
    if direcao not in ['f', 't']:
        print('Direção não válida. Tente novamente.')
        continue

    # Solicitar os pixels
    try:
        pixeis = int(input('Quantos pixels devemos movimentar: '))
    except ValueError:
        print('Por favor, insira um número inteiro válido.')
        continue

    # Solicitar a rotação
    rotacao = input('Rotacionar para e:esquerda, d:direita ou n:não rotacionar: ').lower()
    if rotacao not in ['e', 'd', 'n']:
        print('Rotação não válida. Tente novamente.')
        continue

    # Solicitar o ângulo de rotação se necessário
    angulo = 0  # Valor padrão para caso não haja rotação
    if rotacao in ['e', 'd']:
        try:
            angulo = int(input('Quantos graus deseja rotacionar? (ex.: 90, 45): '))
        except ValueError:
            print('Por favor, insira um número inteiro válido para o ângulo.')
            continue

    # Mover a tartaruga
    mover_tartaruga(direcao, pixeis, rotacao, angulo)
    print('Movimento realizado.')

# Finalizar o programa
print('Programa finalizado. Feche a janela de Turtle para sair.')
screen.mainloop()