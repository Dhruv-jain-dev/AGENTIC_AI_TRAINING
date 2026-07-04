def sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1-i):
            print('[LOG] i:', i, 'j', j, '|' ,'data[j]', data[j], 'data[j+1]', data[j+1])
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                print('[LOG] >> SWAP: data[j]', data[j], 'data[j+1]', data[j+1])
            
            
        


numbers=[10,30,20,5,15]
sort(numbers)                                                                                                                                                                                                                                                                                                                                                                   
print("numbers:",numbers)