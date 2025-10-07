import re

# Importing the input and using encoding to make sure that it gets read correct
with open("day03/input.txt", "r", encoding="utf-8") as f:
    s = f.read()

# Defining the patterns to look for
pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")


total = 0
enabled = True  # mul is enabled in the beginning

# iterating trough all valid patterns in the input and enables or disables the mul based on previous instruction
for m in pattern.finditer(s):
    tok = m.group(0)
    if tok == "do()":
        enabled = True
    elif tok == "don't()":
        enabled = False
    else:
        if enabled:
            a = int(m.group(1))  # defining the first number inside mul
            b = int(m.group(2))  # defining the second number inside mul
            total += a * b

print(total)
