"""Creating two lists from the inputs"""

list1 = []
list2 = []
with open("day01/input.txt", "r") as f:
    for line in f:
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

""" Counting the difference """
sum = 0
for n in list1:
    copies = list2.count(n)
    sum += n * copies

print(sum)
