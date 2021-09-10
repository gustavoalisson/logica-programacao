from collections import deque
# * O primeiro a entrar será o primeiro a sair

q = deque()

q.append('Element 1')
q.append('Element 2')
q.append('Element 3')

print(q)

a = q.popleft()
print('The first popped element is: ', a)

b = q.popleft()
print('The second popped element is: ', b)

c = q.popleft()
print('The third popped element is: ', c)