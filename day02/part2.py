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
                break
            continue

        elif line[x] < line[x - 1] and abs(line[x] - line[x - 1]) < 4:
            count2 += 1
            if count2 == (length - 1):
                safe += 1
                break
            continue

        #       If a code is not safe one of the numbers gets removed and we do the process again
        #       (we try it with both numbers that could be the root to the problem)
        else:
            line2 = line.copy()
            line2.pop(x - 1)
            count3 = 0
            count4 = 0
            for z in range(1, length - 1):
                if line2[z] > line2[z - 1] and abs(line2[z] - line2[z - 1]) < 4:
                    count3 += 1
                    if count3 == (length - 2):
                        safe += 1
                        break
                    continue

                elif line2[z] < line2[z - 1] and abs(line2[z] - line2[z - 1]) < 4:
                    count4 += 1
                    if count4 == (length - 2):
                        safe += 1
                        break
                    continue
                else:
                    break

            line3 = line.copy()
            line3.pop(x)
            count5 = 0
            count6 = 0
            for y in range(1, length - 1):
                if line3[y] > line3[y - 1] and abs(line3[y] - line3[y - 1]) < 4:
                    count5 += 1
                    if count5 == (length - 2):
                        safe += 1
                        break
                    continue

                elif line3[y] < line3[y - 1] and abs(line3[y] - line3[y - 1]) < 4:
                    count6 += 1
                    if count6 == (length - 2):
                        safe += 1
                        break
                    continue
                else:
                    break
            break

print(safe)
