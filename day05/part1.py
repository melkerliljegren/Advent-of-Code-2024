with open("day05/input.txt", "r", encoding="utf-8") as f:
    rules_text, updates_text = f.read().strip().split("\n\n")


rules = [tuple(map(int, r.split("|"))) for r in rules_text.splitlines()]
updates = [list(map(int, u.split(","))) for u in updates_text.splitlines()]
