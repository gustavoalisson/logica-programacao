line = []

line = input().split(' ')

a = int(line[0])
b = int(line[1])
c = int(line[2])

line[0] = a
line[1] = b
line[2] = c

new_list = [a, b, c]

line.sort()

for i in line:
    print(i)

print()

for i in new_list:
    print(i)




    