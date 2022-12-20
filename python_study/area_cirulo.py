import math

n = 3.14159
def circulo(raio):
    area = n * math.pow(raio, 2)
    return '%.4f' % area

print(circulo(2))