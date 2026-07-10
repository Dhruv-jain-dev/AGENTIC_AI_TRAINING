class TollQueue:
    def __init__(self):
        self.head=None
        self.tail = None
        self.size = 0
    def add(self, element):    
        self.size += 1

        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.head.previous = element
            element.previoust = self.tail
            element.next = self.head
            self.tail = element
    def deduct_toll(self,element):
        if (element.type=="2 wheeler"):
            element.fastag.balance-=100
        else:
            element.fastag.balance-=200

    def delete(self):
        self.size -= 1
        self.head = self.head.next

    def show(self, traverse=True):        
        if traverse == True:
            element = self.head
            while True:
                element.show()
                element = element.next
                if element == self.head:
                    break
        else:
            element = self.tail
            while True:
                element.show()
                element = element.previous_
                if element == self.tail:
                    break