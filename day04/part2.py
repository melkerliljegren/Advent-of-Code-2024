with open("day04/input.txt", "r", encoding="utf-8") as f:
    grid = [list(line.strip()) for line in f]

dirs = [(1, 1), (1, -1)]  # Diagonals
R, C = len(grid), len(grid[0])

count = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] != "A":
            continue
        check = 0
        for dy, dx in dirs:
            r1, c1 = r + dy, c + dx
            r2, c2 = r - dy, c - dx

            if not (0 <= r1 < R and 0 <= c1 < C and 0 <= r2 < R and 0 <= c2 < C):
                continue

            ch1 = grid[r1][c1]
            ch2 = grid[r2][c2]

            if ch1 == "M" and ch2 == "S" or ch1 == "S" and ch2 == "M":
                check += 1

        if check == 2:
            count += 1

print(count)
