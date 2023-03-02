
# * Exercício do curso de Guanabara
# * Exercício de fixação apenas para reforçar a base

algum_valor = input('Digite algum valor: ')
print(f'{type(algum_valor)}')
print(f'Os dados estão TODOS em minusculo ? >>> {algum_valor.islower()}')
print(f'O dado é um número ? >>> {algum_valor.isnumeric()}')
print(f'O dado é um alfa numético ? >>> {algum_valor.isalnum()}')
print(f'TODOS os dados estão em MAÍSCULO ? >>> {algum_valor.isupper()}' )