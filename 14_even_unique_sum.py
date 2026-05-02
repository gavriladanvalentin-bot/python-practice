even = []
total = 0
numbers = [4, 7, 2, 7, 8, 2, 3, 4, 4, 8]
for x in numbers:
    if x % 2 == 0 and x not in even:
        even.append(x)
        total += x

print(total)
