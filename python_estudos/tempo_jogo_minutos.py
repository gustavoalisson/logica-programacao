line = []

line = input().split(' ')

hora_inicial = int(line[0])
minuto_inicial = int(line[1])
hora_final = int(line[2])
minuto_final = int(line[3])


print(hora_final - hora_inicial)

# rh = hora_final - hora_inicial

# if rh < 0:
#     rh = 24 + rh

# rm = minuto_final - minuto_inicial

# if rm < 0:
#     rm = 60 + rm
#     rh -=1
    
# if hora_inicial==hora_final and minuto_inicial==minuto_final:
#     print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
# else:
#     print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(rh,rm))       