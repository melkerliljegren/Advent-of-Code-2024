with open("2025/day02/input.txt", "r", encoding="utf-8") as f:
    ids = [tuple(map(int, r.split("-"))) for r in f.read().strip().split(",")]

total = 0

for lo, hi in ids:
    for h in range(1, 10**6):
        n = int(str(h) + str(h))
        if n > hi:
            break
        if n >= lo:
            total += n

print(total)
