def printTypeInfo(value):
    print('Type of the result:', type(value))

# Ints and Floats

# Example 1
firstIntegerNumber = 20
secondIntegerNumber = 4

result1 = firstIntegerNumber / secondIntegerNumber

printTypeInfo(result1) # float

# Example 2
integerNumber = 4
floatNumber = 4.0
result2 = integerNumber + floatNumber

printTypeInfo(result2)

# Example 3 (casting)
result3 = 4 ** 4.0 # float
result3Integer = int(result3) # It's a class not a method

printTypeInfo(result3Integer)
