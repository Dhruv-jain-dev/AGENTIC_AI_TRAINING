class Flight:

    def __init__(self, code, carrier, source,destination,fare,duration):
        self.code = code
        self.carrier = carrier
        self.source=source
        self.destination=destination
        self.duration = duration
        self.fare=fare
        self.next_flight = None
        self.previous_flight = None
        # print('[Flight] [init] Object Constrcuted', self)

    def show_flight(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Flight Code:', self.code)
        print('Carrier:', self.carrier)
        print('Source:', self.source)
        print('Destination:', self.destination)
        print('Duration:', self.duration)
        print('Fare:', self.fare)
        print('HashCode:', self)
        print('next_flight:', self.next_flight)
        print('previous_flight:', self.previous_flight)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')