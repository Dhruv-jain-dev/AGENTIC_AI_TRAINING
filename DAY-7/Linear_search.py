def search(*numbers, **number_to_search):
    for number in numbers:
        print('[LOG] comparing:', number, 'with', number_to_search['key'])
        if number == number_to_search['key']:
            print('number found:', number)
            break
    else:
        print('Number Not Found')


search(10, 20, 30, 40, 50, key=int(input('Enter Number to Search ')))