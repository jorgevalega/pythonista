import turtle

def configurar_tela():
    screen = turtle.Screen()
    screen.title('Movendo a tartaruga')
    return screen

def configurar_tartaruga():
    t = turtle.Turtle()
    t.speed(3)
    t.shape('turtle')
    t.color('green')
    return t

def mover_tartaruga(t, direcao, pixeis, rotacao, angulo):
    if rotacao == 'e':
        t.left(angulo)
    elif rotacao == 'd':
        t.right(angulo)
    if direcao == 'f':
        t.forward(pixeis)
    elif direcao == 't':
        t.backward(pixeis)

def obter_entrada(mensagem, opcoes_validas=None, tipo=str):
    while True:
        entrada = input(mensagem).strip().lower()
        if tipo == int:
            try:
                return int(entrada)
            except ValueError:
                print('Por favor, insira um número inteiro válido.')
        elif not opcoes_validas or entrada in opcoes_validas:
            return entrada
        else:
            print('Opção inválida. Tente novamente.')

def main():
    screen = configurar_tela()
    t = configurar_tartaruga()
    
    while True:
        direcao = obter_entrada('\nPara qual direção devemos ir (f:frente / t:trás / s:sair): ', ['f', 't', 's'])
        if direcao == 's':
            print('Saindo do programa...')
            break
        
        pixeis = obter_entrada('Quantos pixels devemos movimentar: ', tipo=int)
        rotacao = obter_entrada('Rotacionar para e:esquerda, d:direita ou n:não rotacionar: ', ['e', 'd', 'n'])
        
        angulo = 0  # Valor padrão
        if rotacao in ['e', 'd']:
            angulo = obter_entrada('Quantos graus deseja rotacionar? (ex.: 90, 45): ', tipo=int)
        
        mover_tartaruga(t, direcao, pixeis, rotacao, angulo)
        print('Movimento realizado.')

    print('Programa finalizado. Feche a janela de Turtle para sair.')
    screen.mainloop()

if __name__ == "__main__":
    main()