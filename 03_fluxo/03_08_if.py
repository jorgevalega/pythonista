# trabalho_terminado = True

# if trabalho_terminado == True:
#     print('Bora dar uma saida!')
# else:
#     print('Não posso sair agora.')


# numero_atrasos = 2
# if numero_atrasos >= 3:
#     print('Vá para a diretoria')
# elif numero_atrasos == 2:
#     print('Essa é sua segunda falta')
# elif numero_atrasos == 1:
#     print('Essa é sua primeira falta')
# else:
#     print('Pode entrar')


# A velocidade máxima para essa rua é 50km/h
# Cruzou entre 50km a 60km, levou multa de 2 pontos
# Cruzou entre 61km a 75km, levou multa de 3 pontos
# Cruzou acima de 75km, levou multa de 7 pontos

velocidade = 10

if 50 < velocidade < 61:
    print(f'Sua velocidade é {velocidade}km/h, leva multa de 2 pontos.')
elif 61 <= velocidade <= 75:
    print(f'Sua velocidade é {velocidade}km/h, leva multa de 3 pontos.')
elif velocidade > 75:
    print(f'Sua velocidade é {velocidade}km/h, leva multa de 5 pontos.')
else:
    print(f'Sua velocidade é {velocidade}km/h, não leva multa.')
