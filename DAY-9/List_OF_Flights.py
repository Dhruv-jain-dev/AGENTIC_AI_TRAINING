class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        # print('[CircularDoublyLinkedList] [init] Object Constrcuted', self)


    def add(self, element):
        
        self.size += 1

        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next_flight = element
            self.head.previous_flight = element
            element.previous_flight = self.tail
            element.next_flight = self.head
            self.tail = element


    def add_in_front(self, element):
        self.size += 1
        self.head.previous_flight=element
        self.tail.next_flight=element
        element.previous_flight = self.tail
        element.next_flight = self.head
        self.head = element
        

    def add_in_between(self, element, element1, element2):
        self.size += 1
        element.previous_flight = element1
        element.next_flight = element2
        element1.next_flight = element
        element2.previous_flight = element
        

    def delete_last(self):
        self.size -= 1
        self.tail.previous_flight.next_flight=self.head
        self.head.previous_flight=self.tail.previous_flight
        self.tail=self.tail.previous_flight


    def delete_front(self):
        self.size -= 1
        self.head.next_flight.previous_flight = self.tail
        self.tail.next_flight = self.head
        self.head = self.head.next_flight


    def delete(self,element):
        self.size -= 1
        # element.next_flight.previous_flight=element.previous_flight
        # element.previous_flight.next_flight=element.next_flight
        

        if self.head is None:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return

        if element == self.head:
            self.head = self.head.next_flight

        if element == self.tail:
            self.tail = self.tail.previous_flight

        element.previous_flight.next_flight = element.next_flight
        element.next_flight.previous_flight = element.previous_flight




    def show(self, traverse=True):        
        if traverse == True:
            flight = self.head
            while True:
                flight.show_flight()
                flight = flight.next_flight
                if flight == self.head:
                    break
        else:
            flight = self.tail
            while True:
                flight.show_flight()
                flight = flight.previous_flight
                if flight == self.tail:
                    break