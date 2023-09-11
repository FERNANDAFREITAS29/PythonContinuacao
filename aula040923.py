
'''
class Funcionarios:

    nome = 'Elena'
    sobrenome = 'cabral'

usuario1= Funcionarios()
print(usuario1.nome)
print(usuario1.sobrenome)

'''
#modulo
from datetime import datetime
#criar a classe
class Funcionarios:
   def __init__(self, nome, sobrenome, ano_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.ano_nascimento = ano_nascimento

def nome_completo(self):
  return self.nome + '' + self.sobrenome 

def idade_funcionario(self):
  ano_atual = datetime.now().year
  self.ano_nascimento = int (ano_atual - self.ano_nascimento)
  return self.ano_nascimento

#class objeto

usuario1= Funcionarios ('Elena', 'cabral', 2009)
usuario2 = Funcionarios ('Lucia', 'Lima', 2023)
usuario3 = Funcionarios ('Luana', 'Moraes', 2018)

#print(usuario2.nome +''+ usuario2.sobrenome)
#print(usuario2.nome_completo())
print(Funcionarios.idade_funcionario(usuario1))

'''
print(usuario.nome +''+ usuario.sobrenome +''+usuario.data_nascimento)
print(usuario1.nome +''+ usuario1.sobrenome+''+ usuario1.data_nascimento )
print(usuario2.nome+''+ usuario2.sobrenome +''+ usuario2.data_nascimento )
'''
'''
#criar a classe

class Funcionarios:
   def __init__(self, nome, sobrenome, data_nascimento):
    self.nome = nome
    self.sobrenome = sobrenome
    self.data_nascimento = data_nascimento

def nome_completo(self):
  return self.nome + '' + self.sobrenome 

#class objeto

usuario = Funcionarios ('Elena', 'cabral', '12/01/2009')
usuario1 = Funcionarios ('Lucia', 'Lima', '12/01/2023')
usuario2 = Funcionarios ('Luana', 'Moraes', '12/01/2018')

#print(usuario2.nome +''+ usuario2.sobrenome)
#print(usuario2.nome_completo())
#print(Funcionarios.nome_completo (usuario3))

#print(usuario.nome, usuario.sobrenome, usuario.data_nascimento)
#print(usuario1.nome, usuario1.sobrenome, usuario1.data_nascimento )
#print(usuario2.nome, usuario2.sobrenome, usuario2.data_nascimento )

#print(usuario.nome +''+ usuario.sobrenome +''+usuario.data_nascimento)
#print(usuario1.nome +''+ usuario1.sobrenome+''+ usuario1.data_nascimento )
#print(usuario2.nome+''+ usuario2.sobrenome +''+ usuario2.data_nascimento )
'''
'''
#criar parametros

usuario.nome = 'Elena'
usuario.sobrenome = 'Cabral'
usuario.data_nascimento = '12/01/2009'

usuario1.nome = 'Lucia'
usuario1.sobrenome = 'Lima'
usuario1.data_nascimento = '12/01/2023'

#print

print(usuario.nome)
print(usuario1.nome)
'''