#Resistors within Tolerence Range

one_percent = 0
five_percent = 0
reject = 0

resistance = float(input("Enter measured resistance (0 to stop): "))

while resistance != 0:
    if 99.0 <= resistance <= 101.0:
        one_percent = one_percent + 1
    elif 95.0 <= resistance <= 105.0:
        five_percent = five_percent + 1
    else:
        reject = reject + 1

    resistance = float(input("Enter measured resistance (0 to stop): "))

print("1% tolerance:", one_percent)
print("5% tolerance:", five_percent)
print("Reject:", reject)
