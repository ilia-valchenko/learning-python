# Disclaimer: Tuples very much like lists. They haven't order except they declared with parentheses.

simpleTuple = (100, 'Apple') # Trick: We can't modify them.

firstItem = simpleTuple[0] # 100
secondItem = simpleTuple[1] # 'Apple'

# TypeError: 'tuple' object does not support item assignment
# simpleTuple[0] = 'd'

# Why use Tuples:
# - More efficient than lists
# - They don't  grow or change
# - Store compactly in memory
# - They often used by default

def returnMultipleValues():
    return 1, 2, 3, 'Banana' # BTW We can return tuple explicitly: return (1, 2, 3)

print(type(returnMultipleValues())) # <class 'tuple'>

# Short syntax
simpleTuple = 1, 2, 3, 'Apple' # BUT We usually ask developers to use parentheses (1, 2, 3, 'Apple') to avoid confusion

# Assign tuple result to multiple variable
firstNumber, secondNumber, thirdNumber, fruit = returnMultipleValues()

print(f'FirstNumber: {firstNumber}; SecondNumber: {secondNumber}; ThirdNumber: {thirdNumber}; Fruit: {fruit}')
