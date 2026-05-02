
numbers = [12, 45, 7, 23, 89, 34, 89]
maxim1 = float("-inf")
maxim2 = float("-inf")
for x in numbers:
    if x > maxim1:
        maxim2 = maxim1
        maxim1 = x
    elif x > maxim2 and x != maxim1:
        maxim2 = x

print(maxim2)
