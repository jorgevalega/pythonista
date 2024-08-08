""" # Código solto:
marca = input('Digite a marca do seu computador: ')
memoria = input('Digite a quantidade de memória ram: ')
placa = input('Digite o nome da placa de vídeo: ')

print(f'Seu computador é da marca: {marca}')
print(f'Seu computador possui {memoria} de memória')
print(f'Seu computador possui uma placa de vídeo: {placa}')


# Funções:

def exibir_informacoes_do_computador():
    marca = input('Digite a marca do seu computador: ')
    memoria = input('Digite a quantidade de memória ram: ')
    placa = input('Digite o nome da placa de vídeo: ')

    print(f'Seu computador é da marca: {marca}')
    print(f'Seu computador possui {memoria} de memória')
    print(f'Seu computador possui uma placa de cídeo: {placa}')

exibir_informacoes_do_computador() """

# Classes
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memora_ram = memoria_ram
        self.placa_de_video = placa_de_video

computador1 = Computador('Asus', '8GB', 'NVIDIA')
print(computador1.marca)
print(computador1.memora_ram)
print(computador1.placa_de_video)

computador2 = Computador('Dell', '4GB', 'ATI')
print(computador2.marca)
print(computador2.memora_ram)
print(computador2.placa_de_video)