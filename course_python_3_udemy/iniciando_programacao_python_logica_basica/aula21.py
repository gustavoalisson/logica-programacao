# Operadores lógicos
# and or not
# * AND Todas as condições precisam ser verdadeiras
"""
Se qualquer valor for considerado falso, a expressão inteira será avalidada naquele valor
São consideradas falsy 
0 0.0 '' False
Também existe o tipo None que é usado pra representar um não valor
"""

entrada = input('[E]ntrar [S]air: ')
senha_digitada = int(input('Senha: '))

senha_esperada = 123456

if entrada == 'E' and senha_digitada == senha_esperada:
    print('Entrar')
else:
    print('Sair')
    
    