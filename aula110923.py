
'''
CLASS CARRO
Velocidade Maxima, Cor, Ligado
'''

class carro:
    def __init__(self, velMax, ligado,cor):
        self.velmax = velMax
        self.ligado = ligado
        self.cor = cor

    def Mostrar(self):
        print('Velocidade maxima: ' + str (self.velmax))
        print('cor...............: ' + self.cor)
        estado = 'sim' if self.ligado else 'N'
        print('ligado.............: ' + estado)
        print('.........................')

    def ligar(self):
        self.ligado=True

    def desligar(self):
        self.ligado=True
            

c1 = carro(200,False,'Preto')
c2 = carro(120,False,'Branco')
c3 = carro(300,False,'Vermelho')

c1.ligar()
c2.ligar()
c3.ligar()

c1.Mostrar()
c2.Mostrar()
c3.Mostrar()
