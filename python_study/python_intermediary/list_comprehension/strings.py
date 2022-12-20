name = 'Alisson Gustavo'
number_letters = 2
new_string = '_'.join([name[index:index + number_letters] for index in range(0, len(name), number_letters)])
print(new_string)