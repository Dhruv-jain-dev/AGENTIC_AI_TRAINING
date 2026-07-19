numbers = list(range(10, 101, 10))

print("Original List:", numbers)

# ---------------------------------
# 1. Slicing
# ---------------------------------

print("\n--- Slicing ---")
print("First Five Elements:", numbers[:5])
print("Last Five Elements:", numbers[-5:])
print("Elements from Index 2 to 6:", numbers[2:7])
print("Elements Except Last Five:", numbers[:-5])
print("Elements from -5 to -2:", numbers[-5:-2])

# ---------------------------------
# 2. Concatenation
# ---------------------------------

list1 = [10, 20, 30]
list2 = [40, 50, 60]

concatenated_list = list1 + list2

print("\n--- Concatenation ---")
print("List 1:", list1)
print("List 2:", list2)
print("After Concatenation:", concatenated_list)

# ---------------------------------
# 3. Multiplicity (Repetition)
# ---------------------------------

print("\n--- Multiplicity ---")
print("Original List:", list1)
print("Repeated 3 Times:", list1 * 3)

# ---------------------------------
# 4. Membership Testing
# ---------------------------------

print("\n--- Membership Testing ---")
print("20 in list1:", 20 in list1)
print("100 in list1:", 100 in list1)
print("30 not in list1:", 30 not in list1)
print("90 not in list1:", 90 not in list1)
