numbers = tuple(range(10, 101, 10))

print("Original Tuple:", numbers)

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

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

concatenated_tuple = tuple1 + tuple2

print("\n--- Concatenation ---")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("After Concatenation:", concatenated_tuple)

# ---------------------------------
# 3. Multiplicity (Repetition)
# ---------------------------------

print("\n--- Multiplicity ---")
print("Original Tuple:", tuple1)
print("Repeated 3 Times:", tuple1 * 3)

# ---------------------------------
# 4. Membership Testing
# ---------------------------------

print("\n--- Membership Testing ---")
print("20 in tuple1:", 20 in tuple1)
print("100 in tuple1:", 100 in tuple1)
print("30 not in tuple1:", 30 not in tuple1)
print("90 not in tuple1:", 90 not in tuple1)
