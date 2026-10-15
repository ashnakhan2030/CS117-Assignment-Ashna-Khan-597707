#Battery Streak

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9,
            12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

current_streak = 1
longest_streak = 1
current_start = voltages[0]
longest_start = voltages[0]
longest_end = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current_streak = current_streak + 1
    else:
        current_streak = 1
        current_start = voltages[i]

    if current_streak > longest_streak:
        longest_streak = current_streak
        longest_start = current_start
        longest_end = voltages[i]

print("Longest continuous drop:", longest_streak, "readings")
print("Started at:", longest_start, "V")
print("Ended at:", longest_end, "V")
