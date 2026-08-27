with open("day02/input.txt", "r") as f:
    lists = [list(map(int, line.split())) for line in f]

safe = 0

# Looping trough each list and implementing starting values
for line in lists:
    length = len(line)
    count1 = 0
    count2 = 0

    #   Checking each number with its neighbours
    for x in range(1, length):
        if line[x] > line[x - 1] and abs(line[x] - line[x - 1]) < 4:
            count1 += 1
            if count1 == (length - 1):
                safe += 1
            continue

        elif line[x] < line[x - 1] and abs(line[x] - line[x - 1]) < 4:
            count2 += 1
            if count2 == (length - 1):
                safe += 1
            continue

        else:
            break

print(safe)
