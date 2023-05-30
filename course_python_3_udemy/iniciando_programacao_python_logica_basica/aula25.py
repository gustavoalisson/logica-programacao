"""
Interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal

"""
# Neste exercício pratiquei um pouco para pegar a posição das strings

nome = 'Alisson Gustavo'
preço = 1000.9000
variavel = " Olá %s %s, tudo bem ? O preço é %f" % (nome[0:7], nome[8:], preço)

print(variavel)
print('O valor de %i é %08x e em maisculo é %08X' % (22500, 22500, 22500))