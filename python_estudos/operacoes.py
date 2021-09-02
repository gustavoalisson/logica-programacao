number1 = int(input('1º valor: '))
number2 = int(input('Digite outro valor: '))

s = number1 + number2
m = number1 * number2
d = number1 / number2
di = number1 // number2
e = number1 ** number2

print(f' | Soma:{s}\n | Produto:{m}\n | Divisão:{d:.3f}\n', end=' ')
print(f'Divisão Inteira: {di} | Potência: {e}')