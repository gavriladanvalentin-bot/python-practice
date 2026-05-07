
numbers = [1, 3, 2, 3, 4, 1, 3, 2, 1, 1]

count_max = 0
most_frequen = None

for x in numbers:
    count = 0

    for y in range(0, len(numbers)):
        if x == numbers[y]:
            count += 1

        if count > count_max:
            count_max = count
            most_frequen = x

print(most_frequen)
