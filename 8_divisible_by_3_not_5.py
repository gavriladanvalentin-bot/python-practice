count = 0
for x in range(1, 101):
    if x % 3 == 0 and x % 5 != 0:
        print(x)
        count += 1

print("Count: ", count)
