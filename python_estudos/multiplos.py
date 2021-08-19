line = []

line = input().split()

a = int(line[0])
b = int(line[1])

line[0] = a
line[1] = b

print(a % b )
print(b % a )

if (a % b == 0) or (b % a == 0):
    print('multiplo')