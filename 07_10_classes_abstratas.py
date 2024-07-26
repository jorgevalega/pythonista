# Classes abstratas
# Criar um contrato (esqueleto) -> que deve ser implementado na classe que a herda

from abc import ABC, abstractmethod

class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self,tamanho):
        pass

class CameraProfissional(Camera):
    def definir_tamanho_lente(self,tamanho):
        print(f'Alterando a lente para {tamanho}')


camera_profissional = CameraProfissional()
camera_profissional.definir_tamanho_lente(5)

# DESAFIOS

# Crie uma classe abstrata chamada Monitor, que irá ter 2 métodos abstratos:
# aumentar_claridade e reduzir_claridade.

# Os métodos iram receber um número que representam o quanto de claridade deve ser aumentado ou diminuído ao chamar eles.

# Após ter criado a classe abstrata, crie uma nova classe chamada de MonitorFullHD e coloque a implementação dos métodos aumentar_claridade e reduzir_claridade dentro deles.

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self,claridade):
        pass

    @abstractmethod
    def diminuir_claridade(self,claridade):
        pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, claridade):
        print(f'Aumentando a claridade: {claridade}')
        # return super().aumentar_claridade(claridade)
    
    
    
    def diminuir_claridade(self, claridade):
        print(f'Diminuindo a claridade: {claridade}')
        # return super().diminuir_claridade(claridade)
    
monitor_full_hd = MonitorFullHD()
monitor_full_hd.aumentar_claridade(5)
monitor_full_hd.diminuir_claridade(3)
