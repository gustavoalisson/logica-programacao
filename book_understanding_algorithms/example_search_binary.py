# Encontrar a posição de um item

def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1 
    while baixo <= alto: 
        meio = (baixo + alto) // 2 
        chute = lista[meio]
        if chute == item: 
            return meio
        if chute > item: 
            alto = meio - 1
        else: 
           baixo = meio + 1
    
    return None

lista = [1, 3, 5, 7, 9, 80] 
print(pesquisa_binaria(lista,80))

"""
1 Suponha que você tenha uma lista com 128 nomes e esteja fazendo uma
pesquisa binária. Qual seria o número máximo de etapas que você levaria
para encontrar o nome desejado?

"""

# ! minha resposta: 7 etapas

""" 
 Suponha que você duplique o tamanho da lista. Qual seria o número
máximo de etapas agora?

"""

# ! minha resposta: 9 etapas