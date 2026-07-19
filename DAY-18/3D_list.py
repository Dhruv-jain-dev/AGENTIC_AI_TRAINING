large_data = [
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ],
    [
        [11, 22, 33],
        [44, 55, 66],
        [77, 88, 99]
    ]
]

print("3-D List:")
print(large_data)

print("\nAccessing Elements")
print("large_data[0][1][2]:", large_data[0][1][2])  
print("large_data[1][2][1]:", large_data[1][2][1])  
print("large_data[1][0][0]:", large_data[1][0][0])  

print("\nAccessing Complete Blocks and Rows")
print("First Block:")
print(large_data[0])

print("\nSecond Block:")
print(large_data[1])

print("\nFirst Row of Second Block:")
print(large_data[1][0])
