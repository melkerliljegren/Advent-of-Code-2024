with open("2025/day01/input.txt", "r", encoding="utf-8") as f:
    document = [(s[0], int(s[1:])) for s in (line.strip() for line in f)]

counter = 0
pos = 50

for d, c in document:
    steps = c if d == "R" else -c
    pos = (pos + steps) % 100
    if pos == 0:
        counter += 1

print(counter)
