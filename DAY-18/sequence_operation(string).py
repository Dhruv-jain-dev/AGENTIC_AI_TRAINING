text = "Python Programming"

print("Original String:", text)

# ---------------------------------
# 1. Slicing
# ---------------------------------

print("\n--- Slicing ---")
print("First 6 Characters:", text[:6])
print("Last 11 Characters:", text[-11:])
print("Characters from Index 2 to 7:", text[2:8])
print("Characters Except Last 11:", text[:-11])
print("Characters from -11 to -1:", text[-11:-1])

# ---------------------------------
# 2. Concatenation
# ---------------------------------

text1 = "Hello "
text2 = "World"

concatenated_string = text1 + text2

print("\n--- Concatenation ---")
print("String 1:", text1)
print("String 2:", text2)
print("After Concatenation:", concatenated_string)

# ---------------------------------
# 3. Multiplicity (Repetition)
# ---------------------------------

print("\n--- Multiplicity ---")
print("Original String:", text1)
print("Repeated 3 Times:", text1 * 3)

# ---------------------------------
# 4. Membership Testing
# ---------------------------------

print("\n--- Membership Testing ---")
print("'Python' in text:", "Python" in text)
print("'Java' in text:", "Java" in text)
print("'Programming' not in text:", "Programming" not in text)
print("'C++' not in text:", "C++" not in text)
