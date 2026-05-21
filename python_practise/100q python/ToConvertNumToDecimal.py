def convertBinaryToDecimal(binary):
    decimal = 0
    base = 1
    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * base
        base *= 2
        binary //= 10
    return decimal

def convertdecimalToBinary(decimal):
    binary = 0
    base = 1
    while decimal > 0:
        last_digit = decimal % 2
        binary += last_digit * base
        base *= 10
        decimal //= 2
    return binary

def convertBinary(n):
    if n>1:
        convertBinary(n // 2)
    print(n % 2, end='')

convertBinary(10)
print(convertBinaryToDecimal(10))