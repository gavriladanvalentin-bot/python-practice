
numbers = [1, 3, 2, 5, 8, 6]

count = 0
for x in range(1, len(numbers)):
    if numbers[x] > numbers[x-1]:
        count += 1

print(count)
