
import csv

file_path = "C:\\Date excel si CSV\\date 3roi csv.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    transactions = list(reader)

print("Total transactions:", len(transactions))

print("\nFirst transaction:\n")
print(transactions[0])
