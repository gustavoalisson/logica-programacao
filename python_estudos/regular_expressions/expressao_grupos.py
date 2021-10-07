import re

# TEXTOS
texto = '''
Arara 1992
arara 1997
'''
p = re.compile(r'(A|a)?[a-z]{4} [0-9]+')
correspondencias = p.finditer(texto)
for correspondencia in correspondencias:
    print(correspondencia)
    print(correspondencia.group(0))
    print(correspondencia.group(1))
    
print()

texto1 = '''
Sites diversos:
https://web.whatsapp.com/
https://realpython.com/regex-python/
https://github.com/gustavoalisson
http://www.nc.ufpr.br
https://www.google.com.br/
http://www.ibam-concursos.org.br
'''

p = re.compile(r'https?')
correspondencias = p.finditer(texto1)
for correspondencia in correspondencias:
    print(correspondencia)