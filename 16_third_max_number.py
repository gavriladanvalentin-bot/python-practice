
numbers = [7, 2, 9, 4, 1, 5, 9, 2, 8]
max1 = float("-inf")
max2 = float("-inf")
max3 = float("-inf")

for x in numbers:
    if x > max1:
        max3 = max2
        max2 = max1
        max1 = x

    elif x > max2 and x != max1:
        max3 = max2
        max2 = x

    elif x > max3 and x != max1 and x != max2:
        max3 = x

print(max3)
