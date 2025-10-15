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
