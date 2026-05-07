

numbers = [2, 7, 11, 15]
target = 9


for x in range(0, len(numbers)):
    for y in range(x+1, len(numbers)):
        if numbers[x] + numbers[y] == target and x != y:
            print(x, y)
