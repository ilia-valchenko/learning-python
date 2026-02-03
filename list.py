# Slicing
listOfIntegers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
print('1 example:', listOfIntegers[:2]) # 1, 2
print('2 example:', listOfIntegers[2:])


# The 3rd parameter is a step size
# 1
# 1 + 2 = 3
# 3 + 2 = 5
print('3 example:', listOfIntegers[0:6:2]) # 1, 3, 5

# Equivalent
print('4 example:', listOfIntegers[::2]) # 1, 3, 5, 8, 10

# Range function
print('5 example: Print range function values')

for i in range(14):
    print(i)
    
# Converting range in a list
listOfIntegers = list(range(100))

print('6 example: Print range values which we put in the list')
print(listOfIntegers)

# Use negative numbers as parameters
print('7 example:', listOfIntegers[-2:]) # 98, 99
print('8 example:', listOfIntegers[:-2]) # 0, 1, 2, ... 96, 97

# Modifying lists
listOfIntegers = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
listOfIntegers.append(777) # Adds a new value to the end of the list
print('9 example:', listOfIntegers)

# Insert a new item in a specific position
myList = [1, 2, 3, 4]
myList.insert(2, 'new value')
print('10 example:', myList) # 1, 2, 'new value', 3, 4

# Remove by value
myList.remove('new value')
print('11 example:', myList) # 1, 2, 3, 4

myList.remove(2)
print('12 example:', myList) # 1, 3, 4
