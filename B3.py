#Checking Senors Readings

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

count = 0
highest = readings[0]
lowest = readings[0]
total = 0

for voltage in readings:
    if voltage > 3.2:
        count = count + 1

    if voltage > highest:
        highest = voltage

    if voltage < lowest:
        lowest = voltage

    total = total + voltage

average = total / len(readings)

print("Readings above 3.2 V:", count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(average, 2), "V")
