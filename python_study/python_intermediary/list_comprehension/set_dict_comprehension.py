from collections import Counter

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

print()
# set = adiciona valores distintos

def func2(text):
    chars = set()
    for c in text:
        chars.add(c)
    
    chars = list(chars)
    quantity = [ text.count(c) for c in chars ]
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d

print(func2(text))
print()

def func3(text):
    chars = list({ c for c in text })
    quantity = [ text.count(c) for c in chars ]
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d

print(func3(text))
print()

def func4(text):
    chars = list({ c for c in text })
    quantity = [ (c,text.count(c)) for c in chars ]
    return dict(quantity)

print(func4(text))
print()

def func5(text):
    return dict([ (c,text.count(c)) for c in set(text) ])

print(func5(text))
print()

def func6(text):
    return { c: text.count(c) for c in set(text) }

print(func6(text))
print()

def func7(text):
    return Counter(text)

print(func7(text))




        