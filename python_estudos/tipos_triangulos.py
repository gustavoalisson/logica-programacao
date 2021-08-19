import math

line = []

line = input().split(' ')

a = float(line[0])
b = float(line[1])
c = float(line[2]) 

line[0] = a
line[1] = b
line[2] = c

line.sort(reverse= True)

position1 = line[0]
position2 = line[1]
position3 = line[2]

ratangulo = math.pow(b, 2) + math.pow(c, 2)

if position1 >= position2 + position3:
    print('NAO FORMA TRIANGULO')
elif (position1 ** 2) == (position2 ** 2 + position3 ** 2):
    print('TRIANGULO RETANGULO')    
elif math.pow(position1, 2) > (math.pow(position2, 2) + math.pow(position3, 2)):
    print('TRIANGULO OBTUSANGULO')
elif math.pow(position1, 2) < (math.pow(position2, 2) + math.pow(position3, 2)):
    print('TRIANGULO ACUTANGULO')
    
if position1 == position2 and position1 == position3 and position2 == position3:
    print('TRIANGULO EQUILATERO')
elif position1 == position2 or position1 == position3 or position2 == position3:
    print('TRIANGULO ISOSCELES')



    

