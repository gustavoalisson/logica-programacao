with open('text.txt', 'r') as t:
    text = t.read()

def func1(text):
    '''Retornar dict
    dict[char] = quantidade que char aparece em text''' 
    chars = []
    quantity = []
    for c in text:
        if not c in chars:
            chars.append(c)
            quantity.append(1)
        else:
            index = chars.index(c)
            quantity[index] += 1   
    d = {}         
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d    

print(func1(text))

    