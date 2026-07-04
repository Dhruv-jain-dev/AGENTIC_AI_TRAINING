class User:
    def __init__(self, name, phone, location):
        self.name = name
        self.phone = phone
        self.location = location

    def book_cab(self):
        pass


class Driver:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.available = True

    def accept_ride(self):
        self.available = False


class Cab:
    def __init__(self, number, model, cab_type, price):
        self.number = number
        self.model = model
        self.cab_type = cab_type
        self.price = price
        self.available = True

    def calculate_fare(self, distance):
        return distance * self.price


class Booking:
    def __init__(self, pickup, destination, distance):
        self.pickup = pickup
        self.destination = destination
        self.distance = distance
        self.status = "Pending"

    def confirm(self):
        self.status = "Confirmed"

    def cancel(self):
        self.status = "Cancelled"


class Payment:
    def __init__(self, amount, mode):
        self.amount = amount
        self.mode = mode
        self.status = "Pending"

    def pay(self):
        self.status = "Paid"
    

user = User("Dhruv", "9876543210", "Ludhiana")
print(vars(user))
driver = Driver("XYZ", 4.8)
print(vars(driver))
cab = Cab("PB10AB1234", "Swift Dzire", "Mini", 15)
print(vars(cab))
booking = Booking("HOME", "Railway Station", 12)
print(vars(booking))
fare = cab.calculate_fare(booking.distance)
print('fare: ₹',fare)
payment = Payment(fare, "UPI")
print(vars(payment))