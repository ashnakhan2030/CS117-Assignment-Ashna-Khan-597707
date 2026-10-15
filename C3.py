#Binary Code

def decimal_to_binary(n):
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary


print(decimal_to_binary(10))
print(decimal_to_binary(25))
