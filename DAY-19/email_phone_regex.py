# 3. Extract Emails
import re
text = """
john@example.com
admin@finlo.in
hello@gmail.com
"""

emails = re.findall(r"\S+@\S+", text)

print("3. Emails")
print(emails)


# 4. Phone Validation
phone = "9876512345"

print("\n4. Phone")
print("phone is valid" if re.fullmatch(r"\d{10}", phone) else "Invalid")
