def factorial(num):
    if type(num) != int or num < 0:
        return None
    
    if num == 1:
        return 1
    
    return num * factorial(num - 1)

input = 6
result = factorial(input)

print('Factorial of', input, ':', result)
