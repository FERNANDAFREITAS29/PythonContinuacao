# exercicio
# criem uma class chamada automoveis com paramentros = marca, ano
# objetos locadora1, locadora2, locadora3, e imprima valores marca , ano.


# criar a classe
class Computador:
   
 def __init__(self, marca, memoria_ram, placa_de_video):
   self.marca = marca
   self.memoria_ram = memoria_ram
   self.placa_de_video = placa_de_video

def ExibirInformacoes(self):
    print(self.marca,self.memoria_ram,self.placa_de_video)


def Desligar(self):
    print('estou desligando')

    #criar objeto 

    computador1 = Computador('asus', '16gb','Samsung')
    computador1.ExibirInformacoes()
    computador1.Desligar()