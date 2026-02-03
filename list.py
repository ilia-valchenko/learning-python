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
