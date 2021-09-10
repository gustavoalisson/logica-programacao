dictionary = {1: 'valor1', 2: 'valor2', 3: 'valor3'}
print(dictionary[1])

# alterando o valor de um dicionário
dictionary[1] = 'Python'
dictionary[2] = 'JavaScript'
dictionary[3] = 'Java'
# adicionando uma nova chave
dictionary[4] = 'Ruby'
# deletando uma chave
del dictionary[3]
# ! dictionary.popitem()

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
