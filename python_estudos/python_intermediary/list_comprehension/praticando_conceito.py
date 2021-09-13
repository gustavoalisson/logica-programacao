list_empyt = []
new_list = [ list_empyt.append(item) for item in range(1, 5) ]
print(list_empyt)

# --------------------------------------------------------------

lista = []
lista2 = []

for i in [1,2,3]:
    for j in [4,5,6]:
        if i % 2 == 0:
            lista.append((i,j))

print(lista)   

comprehension = [ lista2.append((i,j)) for i in [1,2,3] for j in [4,5,6] if i % 2 == 0] 
print(lista2)

lista3 = [ [ (i,j) for i in [1,2,3] for j in [4,5,6] if i % 2 == 0 ] for v in range(0,3) ] 
print(lista3)       