def deliver_orders():
    yield 'Pizza'
    yield 'Burger'
    yield 'Noodles'

orders = deliver_orders()

print(orders)
print(type(orders))

for order in orders:
    print(order)
  
