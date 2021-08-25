
# * Pilha = O primeiro a entrar, será o último a sair 
stack = []

def empty():
    if len(stack) == 0:
        print('Stack is empty.')
    else:
        print(stack)    

value_1 = 1
value_2 = 2
value_3 = 3
stack.append(value_1)
stack.append(value_2)
stack.append(value_3)
empty()
a = stack.pop()
b = stack.pop()
c = stack.pop()
print('The popped elements are: ' , a, b, c)
empty()
