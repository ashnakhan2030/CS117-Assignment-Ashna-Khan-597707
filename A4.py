#Logic Gates

a = int(input("Enter A: "))
b = int(input("Enter B: "))

if (a != 0 and a != 1) or (b != 0 and b != 1):
    print("Bits must be 0 or 1")
else:
    if a == 1 and b == 1:
        and_answer = 1
    else:
        and_answer = 0

    if a == 1 or b == 1:
        or_answer = 1
    else:
        or_answer = 0

    if a != b:
        xor_answer = 1
    else:
        xor_answer = 0

    print("AND =", and_answer)
    print("OR =", or_answer)
    print("XOR =", xor_answer)
