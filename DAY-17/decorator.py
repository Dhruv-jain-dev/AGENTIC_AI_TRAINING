def logger(func):
    def wrapper():
        print('[LOG] Order Processing Started.....')
        func()
        print('[LOG] Order Processing Fininshed........')
    return wrapper
@logger
def place_order():
    print('Order placed successfully.....')
place_order()
