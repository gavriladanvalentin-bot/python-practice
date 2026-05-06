

# numbers = [2, 4, 1, 6, 8, 10, 3, 2, 4]
# numbers = [1, 3, 5]
numbers = [2, 4, 6]

count = 0
count_max = 0

for x in numbers:
    if x % 2 == 0:
        count += 1
    else:
        count = 0

    if count > count_max:
        count_max = count

print(count_max)
