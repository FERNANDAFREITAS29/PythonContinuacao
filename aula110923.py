
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
            
             