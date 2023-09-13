import moeda
from moeda import diminuir

p = float(input('digite o Preço: R$'))
print(f' a metade de {p} e {moeda.metade(p)}')
print(f' a dobro de {p} e {moeda.dobro(p)}')
print(f' aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f' reduzindo 15%, temos {moeda.diminuir(p, 15)}')