import re

# Entendo um pouco melhor sobre regular expression

# * . Entende qualquer valor exceto uma nova linha 
# * \. Para buscar o caracter "."'
texto = '''
ar\nra
ar1ra
arara
araba
ariba
ararinha
4r4r4
'''
padrao = re.compile('ar.r.')
check = padrao.findall(texto)
print(check)
print()

# * ^ Irá testar o início da string
# * [^] Irá considerar todos os caracteres EXCETO o indicado
texto = 'arara'
p1 = re.compile('^a')
p2 = re.compile('[^a]')
check_1 = p1.findall(texto)
check_2 = p2.findall(texto)
print(check)
print(check_2)
print()

# * \d Qualquer caracter que seja um alrismo de 0 a 9
# * \D Qualquer caracter que NÃO SEJA um algarismo de 0 a 9
# ! Sempre que for usar a \ é importante usar o r 
texto = 'alisson1997'
p1 = re.compile(r'\d')
p2 = re.compile(r'\D')
check_1 = p1.findall(texto)
check_2 = p2.findall(texto)
print(check_1)
print(check_2)
print()

# * \s Qualquer caracter que SEJA vazio
# * \S Qualquer caracter que NÃO SEJA alfanumérico
texto = '''

arara 1992

'''
p1 = re.compile(r'\s')
p2 = re.compile(r'\S')
check_1 = p1.findall(texto)
check_2 = p2.findall(texto)
print(check_1)
print(check_2)
print()

# * \w Qualquer caracter que SEJA alfanumérico
# * \W Qualquer caracter que NÃO SEJA alfanumérico
texto = '''

_arara@ 1992_

'''

p1 = re.compile('\w')
p2 = re.compile('\W')
check_1 = p1.findall(texto)
check_2 = p2.findall(texto)
print(check_1)
print(check_2)



texto_qualquer = 'RUA DON #FREDO ALVES% N°13'
if re.search('#(.*?)%', texto_qualquer):
    # print(re.search('#(.*?)%', texto_qualquer).group(1))
    pass
