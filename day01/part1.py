"""Creating two lists from the inputs"""

list1 = []
list2 = []
with open("day01/input.txt", "r") as f:
    for line in f:
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

""" Sorting the lists"""
list1.sort()
list2.sort()

""" Counting the difference """
sum = 0
for n1, n2 in zip(list1, list2):
    sum += abs(n1 - n2)

print(sum)
