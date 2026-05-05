

numbers = [3, -2, 5, -1, 6, -3]
current_sum = float("-inf")
max_sum = float("-inf")

for x in numbers:
    if current_sum + x > x:
        current_sum = current_sum + x
    else:
        current_sum = x

    if current_sum > max_sum:
        max_sum = current_sum

print(current_sum)
print(max_sum)
