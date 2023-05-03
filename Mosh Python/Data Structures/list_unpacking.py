numbers = [1, 2, 3, 4 , 4 , 4 , 4]
first, second, *other = numbers

first = numbers[0]
second = numbers[1]
third = numbers[2]

print(first)
print(other)

def multiply(*numbers):
    
    multiply(1, 2, 3, 4)