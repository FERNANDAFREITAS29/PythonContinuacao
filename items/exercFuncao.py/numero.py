def numero():
    x = 2


def dobro(x):
    y = x * 2
    return y

num = 2
result = dobro(num)
print("O resultado de ", num, " ao dobro é ", result)


def quadrado(x):
    y = x ** x
    return y

num = 2
result = quadrado(num)
print("O resultado de ", num, " ao quadrado é ", result)

def dobro_do_quadrado_do_dobro_do_numero(x):
    z = x ** 2
    return z

result = dobro_do_quadrado_do_dobro_do_numero(num)
print("O resultado de ", num, " ao  é dobro_do_quadrado_do_dobro_do_numero ", result)