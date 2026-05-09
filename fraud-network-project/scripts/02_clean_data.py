import csv
import re


input_file = r"C:\Date excel si CSV\date 3roi csv.csv"
output_file = r"C:\Date excel si CSV\cleaned_transactions.csv"


def clean_empty(value):
    if value is None:
        return None

    value = value.strip()

    if value == "":
        return None

    return value


def clean_email(email):
    email = clean_empty(email)

    if email is None:
        return None

    return email.lower()


def clean_phone(phone):
    phone = clean_empty(phone)

    if phone is None:
        return None

    phone = re.sub(r"[^0-9]", "", phone)

    if phone == "":
        return None

    return phone


def clean_amount(amount):
    amount = clean_empty(amount)

    if amount is None:
        return None

    amount = re.sub(r"[^0-9.]", "", amount)

    if amount == "":
        return None

    return float(amount)


def clean_integer(value):
    value = clean_empty(value)

    if value is None:
        return None

    if value.isdigit():
        return int(value)

    return None


def clean_card(card):
    card = clean_empty(card)

    if card is None:
        return None

    return card


def extract_bin(card):
    card = clean_card(card)

    if card is None:
        return None

    digits = re.sub(r"[^0-9]", "", card)

    if len(digits) >= 6:
        return digits[:6]

    return None


with open(input_file, mode="r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    transactions = list(reader)


cleaned_transactions = []

for transaction in transactions:
    cleaned_transaction = {
        "ret_ref_nr": clean_empty(transaction.get("Ret Ref Nr")),
        "divisionid": clean_empty(transaction.get("Divisionid")),
        "tran_date": clean_empty(transaction.get("Tran Date")),
        "fraudstatus": clean_empty(transaction.get("Fraudstatus")) or "SUCCESSFUL",
        "masked_card": clean_card(transaction.get("MaskedCard")),
        "card_bin": extract_bin(transaction.get("MaskedCard")),
        "total": clean_amount(transaction.get("Total")),
        "tran_currency": clean_empty(transaction.get("Tran Currency")),
        "card_issuing_country": clean_empty(transaction.get("Card Issuing Country")),
        "cust_ip": clean_empty(transaction.get("Cust Ip")),
        "ip_country": clean_empty(transaction.get("Ip Country")),
        "channel": clean_empty(transaction.get("Channel")),
        "src_msisdn": clean_phone(transaction.get("Src Msisdn")),
        "dst_msisdn": clean_phone(transaction.get("Dst Msisdn")),
        "home_msisdn": clean_phone(transaction.get("Home Msisdn")),
        "act_age": clean_integer(transaction.get("Act Age")),
        "cust_email": clean_email(transaction.get("Cust Email")),
        "cust_first_name": clean_empty(transaction.get("Cust First Name")),
        "cust_last_name": clean_empty(transaction.get("Cust Last Name")),
        "bill_address1": clean_empty(transaction.get("Bill Address1")),
        "bill_country": clean_empty(transaction.get("Bill Country")),
        "postal_code": clean_empty(transaction.get("Postal Code")),
        "reversed": clean_empty(transaction.get("Reversed")),
    }

    cleaned_transactions.append(cleaned_transaction)


fieldnames = list(cleaned_transactions[0].keys())

with open(output_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_transactions)


print("Raw transactions:", len(transactions))
print("Cleaned transactions:", len(cleaned_transactions))
print("Output file created:", output_file)

print("\nFirst cleaned transaction:\n")
print(cleaned_transactions[0])
