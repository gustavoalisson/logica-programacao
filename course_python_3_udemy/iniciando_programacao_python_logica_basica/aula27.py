
"""
Fatiamento de Strings
012345678
Olá Mundo
-987654321
Fatiamento [i:f:p] [::]

Obs.: a função len retorna a qtd de caracter da str

"""

variavel = 'Ola mundo'

print(variavel)
print(len(variavel[4:]))
print(variavel[4:])
print(variavel[:len(variavel):1]) # contando de um em um
print(variavel[:len(variavel):2]) # contando de dois em dois
print(variavel[::-1]) # inverter string 
