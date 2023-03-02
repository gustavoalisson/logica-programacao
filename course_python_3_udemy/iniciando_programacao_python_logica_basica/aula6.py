# conversao de tipos, coercao 
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutaveis e primitivos
# str, int, float, bool
print(int('1') + 1)
print(float('1.9') + 1)
print(bool(' '))

"""
O código bool(' ') retorna True porque a string ' ' contém um espaço em branco.
Em Python, uma string com qualquer caractere, mesmo que seja apenas um espaço em branco,
é considerada verdadeira quando convertida em um valor booleano usando a função bool(). 
Se a string estiver vazia, ou seja, sem caracteres, bool() retornará False

"""

print(str(11) + 'b')