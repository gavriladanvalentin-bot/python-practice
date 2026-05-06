
numbers = [1, 2, 3, 1, 2, 8, 9]

count_int = 1
count_final = 1

for x in range(1, len(numbers)):
    if numbers[x] > numbers[x-1]:
        count_int += 1
    else:
        count_int = 1

    if count_int > count_final:
        count_final = count_int

print(count_final)
