import re
# 7. Extract Phone, Email & Vehicle
text = """
Call +919876512345
Email: john@example.com
Vehicle: PB10AL2937
"""

phones = re.findall(r"\+91\d{10}", text)
emails = re.findall(r"\S+@\S+", text)
vehicles = re.findall(r"[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}", text)

print("7. Extracted Data")
print("Phone  :", phones)
print("Email  :", emails)
print("Vehicle:", vehicles)
