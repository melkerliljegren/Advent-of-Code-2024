import re

# Importing the input and using encoding to make sure that it gets read correct
with open("day03/input.txt", "r", encoding="utf-8") as f:
    s = f.read()

# Defining the valid pattern
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

# Finding all valid combinations in the input and counts the total sum
total = 0
for a, b in pattern.findall(s):
    total += int(a) * int(b)

print(total)
