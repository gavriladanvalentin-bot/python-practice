
nr = [12, 45, 7, 23, 89, 34, 10]
rez = 0
for x in nr:
    rez += x

medie = rez/len(nr)
count = 0
for x in nr:
    if x > medie:
        count += 1

print(medie)
print(count)
