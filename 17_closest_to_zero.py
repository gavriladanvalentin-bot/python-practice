
# numbers = [7, -3, 2, -8, 4, -1, 1]
# poz = float("inf")
# neg = float("-inf")

# for x in numbers:
#     if x < poz and x > 0:
#         poz = x
#     elif x > neg and x < 0:
#         neg = x

# if poz + neg > 0:
#     print(neg)
# elif poz + neg <= 0:
#     print(poz)


numbers = [7, -3, 2, -8, 4, -1, 1]

closest = float("inf")

for x in numbers:
    # distanța manuală față de 0
    if x < 0:
        dist_x = -x
    else:
        dist_x = x

    if closest < 0:
        dist_closest = -closest
    else:
        dist_closest = closest

    if dist_x < dist_closest:
        closest = x
    elif dist_x == dist_closest and x > closest:
        closest = x  # preferăm pozitivul

print(closest)
