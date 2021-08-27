numbers = [1, 5,10,20,25,30,35,40,45,50,55, 60,65, 70,75, 80,85, 90,95, 100, 200, 300, 400, 500, 600]
new_numbers = [number for number in numbers if number >= 50]
odd_numbers = [number for number in numbers if number % 2 != 0]
even_numbers = [number for number in numbers if number % 2 == 0]


print('all numbers > ', numbers)
print()
print('new numbers > ', new_numbers)
print()
print('odd numbers > ', odd_numbers)
print()
print('even numbers > ', even_numbers)

