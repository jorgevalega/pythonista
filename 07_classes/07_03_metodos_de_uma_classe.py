# Métodos de uma classe -> ligar, desligar, exibir dados do computador
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.palca_de_video = placa_de_video 
    def ligar(self):
        print('Estou ligando o computador')     

    def desligar(self):
        print('Estou desligando')   

    def exibir_dados_do_computador(self):
        print(f'Computador de marca {self.marca}, com {self.memoria_ram} de memoria ram e que usa a placa de vídeo {self.palca_de_video}')

computador1 = Computador('Asus', '64GB', 'NVIDIA')  
         
computador1.ligar()         
computador1.desligar()
computador1.exibir_dados_do_computador()

computador2 = Computador('Dell', '8GB', 'NVIDIA')
computador2.ligar()         
computador2.desligar()
computador2.exibir_dados_do_computador()