
# * Exemplo 01 
list1 = [1,2,3,4, 'Estrutura de Dados']

# append(), extend() and insert()
list1.append((2,'teste_tuple'))
list1.extend((2,0))
list1.insert(4, 5)

#del, pop(), remove()
del list1[6]
list1.pop(4)
list1.remove(2)

# ! print(list1) 

# * Exemplo 02
list2 = [200, 0, 2, 1, 10, 9, 21, 7, 12]

# sorted() and sort()
print(sorted(list2))
print('O sorted() não altera a estrutura da lista >>>' , list2 ) 

list2.sort()
print('O sort() altera a estrutura definitivamente >>>' , list2)
# Ao contrário - reverse = True

# Busca a posição do elemento
print(list2.index(21))
# Retorna o número de ocorrência do elemento dentro de uma lista
print(list2.count(10))
