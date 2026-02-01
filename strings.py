import math

# Slicing
name = 'My name is Ryan Mitchell'
print(name[0])
print(name[11:24]) # Ryan Mitchell

print(name[:7]) # Short syntax
print(name[11:])

# Formatting
stringValue1 = 'My number is:' + str(5)
stringValue2 = f'My number is: {5}'
stringValue3 = f'My number is: {5} and twice that is {2 * 5}'
stringValue4 = f'Pi is: {math.pi:.2f}' # 'Pi is: 3.14'

# Multi-line Strings
multiLineString = '''
Here is a long block of text.
I can add new lines!
'''
