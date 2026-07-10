# stck  queue, built in fn,
from queue import TollQueue

class FastTag:
    def __init__(self, fastag_id,bank,balance):
        self.fastag_id = fastag_id
        self.bank = bank
        self.balance = balance
    def show(self):
        print('-----FastTag-----------')
        print(f'{self.fastag_id} | {self.bank} | {self.balance}')
class vehicle:
    def __init__(self,registration_no, type,fasttag):
        self.registration_no = registration_no
        self.type = type
        self.fasttag = fasttag
    def show(self):
        print('-----Vehicle-----------')
        print(f'{self.registration_no} | {self.type}')
        self.fasttag.show()
Q=TollQueue()
v1=Q.add(vehicle(1234, '2 wheeler', FastTag('ABC1234',"HDFC",'₹5000')))
v2=Q.add(vehicle(2222, '2 wheeler', FastTag('ABC2222',"HDFC",'₹5000')))
v3=Q.add(vehicle(3333, '4 wheeler', FastTag('ABC3333',"HDFC",'₹50')))
v4=Q.add(vehicle(1434, '4 wheeler', FastTag('ABC1434',"HDFC",'₹5000')))
v5=Q.add(vehicle(1254, '2 wheeler', FastTag('ABC1254',"HDFC",'₹5000')))
Q.delete()
Q.show()