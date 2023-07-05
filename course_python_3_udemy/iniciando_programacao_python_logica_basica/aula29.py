"""
Introdução ao try/except

try - > Irá tentar executar o código
except - > Ocorreu algum erro ao tentar executar

"""

numero = input(
    'Vou dobrar o número que você digitar: '
    )

try:
    numero_float = float(numero)
    print(f'FLOAT: {numero_float}')
      
    print(f'O dobro de {numero} é {numero_float}')
except:
    print('Isso não é um número')
