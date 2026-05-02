
numbers = [7, 2, 9, 4, 1, 5, 1, 2]
min1 = float("+inf")
min2 = float("+inf")
for x in numbers:
    if x < min1:
        min1 = min2
        min1 = x

    elif x < min2 and x != min1:
        min2 = x

print(min1, min2)
