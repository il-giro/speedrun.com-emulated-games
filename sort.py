# Read the file and create a list of tuples
with open('emu.txt', 'r') as file:
    lines = [line.strip().split(' ') for line in file]

# Convert the first column to integers for proper sorting
lines = [(int(line[0]), line[1], line[2]) for line in lines]

# Sort the list in descending order
lines.sort(reverse=True)

# Write the sorted list back to the existing file
with open('emu.txt', 'w') as file:
    for line in lines:
        file.write(f"{line[0]} {line[1]} {line[2]}\n")


# Read the file and create a list of tuples
with open('no_emu.txt', 'r') as file:
    lines = [line.strip().split(' ') for line in file]

# Convert the first column to integers for proper sorting
lines = [(int(line[0]), line[1], line[2]) for line in lines]

# Sort the list in descending order
lines.sort(reverse=True)

# Write the sorted list back to the existing file
with open('no_emu.txt', 'w') as file:
    for line in lines:
        file.write(f"{line[0]} {line[1]} {line[2]}\n")
