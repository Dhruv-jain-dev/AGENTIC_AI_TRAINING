def product(numbers, length):
    if length == 0:
        return 1
    else:
        previous = product(numbers, length-1)
        current = numbers[length-1]
        return current * previous
        # return numbers[length-1] *  product(numbers, length-1)

data = [2, 3, 8]
result = product(data, len(data))
print('result is:', result)