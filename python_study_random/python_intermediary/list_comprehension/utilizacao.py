import math

def divisionFn(value):
    div = value / 2
    return div
    
numbers = [10,20,30,40,50]

division = [divisionFn(number) for number in numbers]
multiplication = [number * 2 for number in numbers]
exponentiation = [math.pow(number, 2) for number in numbers]

print(f'list: {numbers}')
print(division)
print(multiplication)
print(exponentiation)