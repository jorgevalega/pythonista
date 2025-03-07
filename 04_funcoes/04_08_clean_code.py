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

def solicitar_input(mensagem, opcoes_validas=None, tipo=int):
    while True:
        entrada = input(mensagem).lower()
        if opcoes_validas and entrada not in opcoes_validas:
            print('Opção inválida. Tente novamente.')
            continue
        if tipo == int:
            try:
                return int(entrada)
            except ValueError:
                print('Por favor, insira um número válido.')
                continue
        return entrada

def main():
    screen = configurar_tela()
    t = configurar_tartaruga()
    
    while True:
        direcao = solicitar_input('\nPara qual direção devemos ir (f:frente / t:trás / s:sair): ', ['f', 't', 's'], str)
        if direcao == 's':
            print('Saindo do programa...')
            break
        
        pixeis = solicitar_input('Quantos pixels devemos movimentar: ')
        rotacao = solicitar_input('Rotacionar para e:esquerda, d:direita ou n:não rotacionar: ', ['e', 'd', 'n'], str)
        
        angulo = 0  # Valor padrão
        if rotacao in ['e', 'd']:
            angulo = solicitar_input('Quantos graus deseja rotacionar? (ex.: 90, 45): ')
        
        mover_tartaruga(t, direcao, pixeis, rotacao, angulo)
        print('Movimento realizado.')
    
    print('Programa finalizado. Feche a janela de Turtle para sair.')
    screen.mainloop()

if __name__ == "__main__":
    main()
