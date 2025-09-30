with open("day02/input.txt", "r") as f:
    lists = [list(map(int, line.split())) for line in f]

safe = 0

for line in lists:
    length = len(line)
    check1 = None
    check2 = None

    for x in range(1, length):
        if line[x] > line[x - 1] and abs(line[x] - line[x - 1]) < 4:
            check1 = True
            continue
        else:
            check1 = False
            break

    if check1 is True:
        safe += 1
        continue

    for x in range(1, length):
        if line[x] < line[x - 1] and abs(line[x] - line[x - 1]) < 4:
            check2 = True
            continue
        else:
            check2 = False
            break

    if check2 is True:
        safe += 1
        continue

print(safe)
