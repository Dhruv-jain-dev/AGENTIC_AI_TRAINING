import re

# 1. Search a Word
text = "Python is easy to learn"

result = re.search(r"easy", text)

print("1. Search")
print(result)
print("'easy' Found" if result else "'easy' Not Found")


# 2. Extract Numbers
text = "Order ID 101 costs 2500 INR"

numbers = re.findall(r"\d+", text)

print("\n2. Numbers")
print(numbers)
