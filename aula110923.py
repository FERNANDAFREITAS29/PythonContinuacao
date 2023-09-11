
'''
CLASS CARRO
Velocidade Maxima, Cor, Ligado
'''

class carro:
    def __init__(self, velMax, ligado,cor):
        self.velmax =velMax
        self.ligado = ligado
        self.cor = cor

        def Mostrar(self):
            print('Velocidade maxima: ' + str (self.vel.Max))
            print('cor...............: ' + self.cor)
            estado = 'sim' if self.ligado else 'N'
            print('ligado.............: ' + estado)
            print('.........................')

c1 = Carro(200,False,'Preto')
c2 = Carro(120,False,'Branco')
c3 = Carro(300,False,'Vermelho')
c1.Mostrar()
c2.Mostrar()
c3.Mostrar()