a = 'A'
b = 'B'
c = 1.1
string = '{nome4} a = {0} b = {1} c = {2:.2f} {nome4}'

formato = string.format(
    a, b, c, nome4=...)

print(formato)

