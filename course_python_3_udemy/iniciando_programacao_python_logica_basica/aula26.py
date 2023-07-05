"""
Interpolação básica de strings

s - string
d - int
f - float
.<número de dígitos>f
x e X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda 
< - Direita
^ - Centro
Sinal de + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s !a

"""

variavel = "ABC"
print(f'.{variavel:>20}.')
print(f'.{variavel:<20}.')
print(f'.{variavel:q^20}.')
print(f'{10000.564941261321:+,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}') #maisculo
print(f'O hexadecimal de 1500 é {1500:08x}') #minusculo


