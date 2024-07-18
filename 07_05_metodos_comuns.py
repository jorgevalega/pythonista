# Métodos comuns
# Métodos de Classes (Class Methods)
# Métodos estáticos (Static Methods)

class Computador:
    sistema_operacional = 'Windows 10'

    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    # Método comum
    def exibir_dados_do_computador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video, self.sistema_operacional)

    @classmethod
    def computador_escrtorio(cls,memoria_ram):
        return cls('Dell',memoria_ram,'Placa de Vídeo - Baixo Custo')
    
    @classmethod
    def computador_configuracao_pesado(cls,memoria_ram):
        return cls('Dell',memoria_ram,'Placa de Vídeo - Alto Nível')
    
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False

print(Computador.roda_programas_pesados(10))

# Configuração para clientes de escritório
computador1 = Computador.computador_escrtorio('8GB')        

# Configuração para clientes de trabalho pesado
computador2 = Computador.computador_configuracao_pesado('16GB')

computador1.exibir_dados_do_computador()
print('###########')
computador2.exibir_dados_do_computador()