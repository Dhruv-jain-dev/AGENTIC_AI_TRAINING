from functools import reduce


flights = [
    {"flight_no": "AI101", "source": "Delhi", "destination": "Mumbai", "price": 5000},
    {"flight_no": "AI102", "source": "Delhi", "destination": "Bangalore", "price": 7000},
    {"flight_no": "AI103", "source": "Mumbai", "destination": "Chennai", "price": 4500},
    {"flight_no": "AI104", "source": "Delhi", "destination": "Goa", "price": 6000},
    {"flight_no": "AI105", "source": "Jaipur", "destination": "Delhi", "price": 3500}
]

print("Original Flight Details:")
for flight in flights:
    print(flight)


discounted_flights = list(map(
    lambda flight: {
        **flight,
        "price": flight["price"] * 0.90
    },
    flights
))

print("\nFlights after 10% Discount:")
for flight in discounted_flights:
    print(flight)


expensive_flights = list(filter(
    lambda flight: flight["price"] > 5000,
    flights
))

print("\nFlights with Price Greater Than 5000:")
for flight in expensive_flights:
    print(flight)


total_price = reduce(
    lambda total, flight: total + flight["price"],
    flights,
    0
)

print("\nTotal Price of All Flights:", total_price)
