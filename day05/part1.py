from collections import defaultdict

with open("day05/input.txt", "r", encoding="utf-8") as f:
    rules_text, updates_text = f.read().strip().split("\n\n")

"""Creating two lists with the rules in one and updates in one"""
rules = [tuple(map(int, r.split("|"))) for r in rules_text.splitlines()]
updates = [list(map(int, u.split(","))) for u in updates_text.splitlines()]

"""Creating a dictionary that showcase which updates needs to be after another update"""
after = defaultdict(set)
for x, y in rules:
    after[x].add(y)

"""
Looping trough each update and if the order works 
with the rules, the number in the middle gets added to the total
"""
total = 0
for update in updates:
    pos = {v: i for i, v in enumerate(update)}
    ok = True
    for x in update:
        for y in after.get(x, ()):
            if y in pos and pos[y] < pos[x]:
                ok = False
                break
        if not ok:
            break
    if ok:
        total += update[len(update) // 2]

print(total)
