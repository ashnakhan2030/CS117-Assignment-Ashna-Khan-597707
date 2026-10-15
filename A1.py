#Checks if Current Flow is compatible with fuse
voltage = int(input("Enter voltage (V): "))
resistance = int(input("Enter resistance (Ohm): "))

if resistance <= 0:
    print("Invalid resistance")
else:
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
