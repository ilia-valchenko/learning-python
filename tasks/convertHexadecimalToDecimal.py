# Python code​​​​​​‌‌‌‌​​​‌​​​​‌​​​‌​‌​​‌​​‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    if len(hexNum) == 0:
        return None

    power = len(hexNum) - 1
    result = 0

    for item in hexNum:
        if item not in hexNumbers:
            return None

        result = result + (hexNumbers[item] * (16 ** power))
        power = power - 1

    return result

# hex = 'A2'
hex = 'spam spam spam'
result = hexToDec(hex)
print(hex, ' in decimal is ', result)
