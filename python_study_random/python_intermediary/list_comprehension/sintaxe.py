numbers = [1,2,3,4,5]
new_numbers = [number for number in numbers]

# ! The same as: 
# new_numbers = []

# for number in numbers:
#     new_numbers.append(number)

numbers[0] = 30

print(new_numbers)