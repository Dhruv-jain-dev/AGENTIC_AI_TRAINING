import re
# 5. PAN Validation
pan = "BBVPK2144K"

print("5. PAN")
print("Valid" if re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]", pan) else "Invalid")


# 6. Vehicle Number Validation
vehicle = "PB10AL2937"

print("\n6. Vehicle")
print("Valid" if re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}", vehicle) else "Invalid")
