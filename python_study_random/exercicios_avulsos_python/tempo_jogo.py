line = []

line = input().split(' ')

hora_inicial = int(line[0])
hora_final = int(line[1])

if hora_inicial > hora_final:
    calculo = hora_inicial - hora_final
    duracao = 24 - calculo
    print(f'O JOGO DUROU {duracao} HORA(S)')

elif hora_final > hora_inicial:
    duracao = hora_final - hora_inicial
    print(f'O JOGO DUROU {duracao} HORA(S)')

else:
    duracao = 24
    print(f'O JOGO DUROU {duracao} HORA(S)')
            
        



