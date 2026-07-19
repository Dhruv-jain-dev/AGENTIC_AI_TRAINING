number = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]


print("2-D List:")
print(number)

print("\nLength of 2-D List")
print("Number of rows:", len(number))
print("Number of columns:", len(number[0]))

print("\nAccessing Elements")
print("First row, third column:", number[0][2])   
print("Second row, second column:", number[1][1]) 
print("Third row, first column:", number[2][0])  

print("\nNegative Indexing")
print("Last row:", number[-1])
print("Second last element of last row:", number[-1][-2])
