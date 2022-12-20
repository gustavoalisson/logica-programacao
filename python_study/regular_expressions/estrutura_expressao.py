import re

texto = '''
Arara 1992
Arara 1997

'''
# [] - grupo de caracters 

p = re.compile(r'[a-zA-Z0-9]')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

print()

# Outra siatuação

p = re.compile(r'[a-zA-Z]+ [0-9]+')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)

