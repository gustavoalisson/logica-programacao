import re
# Métodos para checagem

texto = 'arara'
p1 = re.compile(r'r')
check_findall = p1.findall(texto)
check_match = p1.match(texto) # * procura no início da string
check_search = p1.search(texto) # * procura em qualquer parte da string
check_finditer = p1.finditer(texto) # * deixa a string iteravel

print(check_findall)
print(check_match)
print(check_search)
print(check_finditer)
print()
correspondencias = check_finditer

for correspondencia in correspondencias:
    print(correspondencia)