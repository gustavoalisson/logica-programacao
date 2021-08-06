line = []
line = input().split(' ')

a = float(line[0])
b = float(line[1])
c = float(line[2])

module_1 = b - c
module_2 = a - c
module_3 = a - b    
     
if (module_1) < a + b + c or (module_2) < b < a + c or (module_3) < c < a + b:
    perimeter = a + b + c
    print(perimeter)
else:
    pass
    
        