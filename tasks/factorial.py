# Python code​​​​​​‌‌‌‌​​​​​​‌‌​‌‌​​​‌​‌​‌​​ below

def factorial(num):
    if type(num) is not int or num < 0:
        return None

    if num == 0 or num == 1:
        return 1

    result = num
    num = num - 1
    
    while num > 1:
        result *= num
        num = num - 1

    return result

input = 5
result = factorial(input)

print('Type of input:', type(input))
print('Factorial of', input, ':', result)
