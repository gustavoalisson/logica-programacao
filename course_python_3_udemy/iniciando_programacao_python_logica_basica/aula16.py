# if / elif    /else

entrada = input('Voce quer "entrar" ou "sair" ?').lower()

if entrada == "entrar":
    print('Você entrou no sistema.') 
elif entrada == "sair": 
    print('Você saiu do sistema') 
else:
    print('Opção errada.')