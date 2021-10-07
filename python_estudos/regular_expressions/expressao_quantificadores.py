import re

# QUANTIFICADORES

texto = '''
Arara
'''
# * * 0 ou mais
p = re.compile(r'[ra]*')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

print()
    
# * + 1 ou mais
p = re.compile(r'[ra]+')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

print()

# * ? 0 ou um
p = re.compile(r'[ra]?')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

print()

# * {3} - número exato de repetições

p = re.compile(r'[ra]{2}')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

print()

# * {3,4} - de 3 A 4 MIN E MAX
p = re.compile(r'[ra]{2,4}')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
