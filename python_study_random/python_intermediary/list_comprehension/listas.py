# minha solução
nomes = ['alisson', 'carlos', 'juninho', 'giulan', 'amós']
novos_nomes = [f'{nome[:-1]}{nome[-1].upper()}' for nome in nomes]

print(novos_nomes)


# print()
# print('--------SEM O LIST COMPREHENSION ---------')
# for i in nomes:
#     print(f'{i[:-1]}{i[-1].upper()}')