from functools import reduce
product_prices=[100,300,450,120,900]
discounted_price = []
discount = lambda price , percentage : price * percentage
for price in product_prices:
    discounted_price.append(discount(price, 0.50))
print('product_price:',product_prices)
print('discounted_prices:',discounted_price)
new_prices= list(map(lambda price: price*0.50 , product_prices))
print('new_prices:',new_prices)
filtered_prices = list(filter(lambda price: price>200, product_prices))
print('filtered_prices:',filtered_prices)
total = reduce(lambda x, y : x+y, product_prices)
print('total:',total)
