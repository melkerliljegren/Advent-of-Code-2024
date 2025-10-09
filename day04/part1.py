with open("day04/input.txt", "r", encoding="utf-8") as f:
    grid = [list(line.strip()) for line in f]

word = "XMAS"
dirs = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
R, C = len(grid), len(grid[0])

count = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] != "X":
            continue
        for dy, dx in dirs:
            rr = r + dy * 3
            cc = c + dx * 3
            if not (0 <= rr < R and 0 <= cc < C):
                continue
            ok = True
            for k in range(4):
                if grid[r + dy * k][c + dx * k] != word[k]:
                    ok = False
                    break
            if ok:
                count += 1

print(count)
