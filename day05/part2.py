from functools import cmp_to_key

with open("day05/input.txt", "r", encoding="utf-8") as f:
    rules_text, updates_text = f.read().strip().split("\n\n")

"""Creating two lists with the rules in one and updates in one"""
rules = [tuple(map(int, r.split("|"))) for r in rules_text.splitlines()]
updates = [list(map(int, u.split(","))) for u in updates_text.splitlines()]

"""Creating a dictionary with all rules"""
after = set(rules)

"""Defining the key for the sorted function"""


def cmp(x, y):
    if (x, y) in after:
        return -1
    elif (y, x) in after:
        return 1
    return 0


"""
Looping through the updates and sorting the incorrectly-ordered update
cmp_to_key makes it possible for sorted to sort after our rules
"""
total = 0
for upd in updates:
    fixed = sorted(upd, key=cmp_to_key(cmp))
    if fixed != upd:
        total += fixed[len(fixed) // 2]

print(total)
