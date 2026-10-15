#Parallel Resistance

def parallel_resistance(resistors):
    reciprocal_sum = 0

    for resistance in resistors:
        reciprocal_sum = reciprocal_sum + 1 / resistance

    equivalent = 1 / reciprocal_sum
    return round(equivalent, 2)


print(parallel_resistance([10, 10]))
print(parallel_resistance([100, 200, 300]))
