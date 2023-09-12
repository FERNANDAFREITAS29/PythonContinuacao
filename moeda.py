#crie um modulo chamado moeda.py que tenha as funçoes 
#incorparadas aumentar(), dobro() e metade().
#faça tambem programa que importa esse modulo e use algumas
#dessas funções crie modulo teste.py

def aumentar(preço, taxa):
    res = preço + (preço*taxa/100)
    return res

def diminuir(preço, taxa):
    res = preço - (preço*taxa/100)
    return res

def dobro (preço):
    res = preço * 2
    return res

def metade(preço):
    res = preço / 2
    return res