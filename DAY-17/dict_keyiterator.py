orders = {
     '01': 'Pizza',
     '02': 'Burger',
     '03': 'Pasta',   # <-- Missing comma added here
     '04': 'Noodles',
     '05': 'Coke'
}

orders_iterator = iter(orders)
print(orders_iterator, type(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
