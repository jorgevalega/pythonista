# Polimorfismo
print(10 + 20)
print('Olá' + ' dev')

print(len('Livro'))
print(len([25, 20, 30]))
print(len({'Título': 'Livro1', 'Lançamento': '2010', 'Cateroria': 'Lifestyle'}))

class Carro:
    def ligar(self):
        print('Ligando o carro')

class Moto:
    def ligar(self):
        print('Ligando a moto')

def iniciar(veiculo):
    veiculo.ligar()

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)

class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(nome)

pessoa = Pessoa()
pessoa.apresentar('Jorge')
pessoa.apresentar('Jorge', 47)
pessoa.apresentar('Jorge', 47, 'Programador')