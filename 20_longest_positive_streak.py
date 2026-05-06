

numbers = [-1, 2, 3, -5, 4, 6, 7, -2, 8]

count = 0
count_max = 0

for x in numbers:
    if x > 0:
        count += 1
    else:
        count = 0

    if count > count_max:
        count_max = count

print(count_max)
