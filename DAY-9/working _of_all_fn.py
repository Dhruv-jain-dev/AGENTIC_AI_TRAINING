from Flights_info import Flight
from List_OF_Flights import CircularDoublyLinkedList

flight_list = CircularDoublyLinkedList()
Flight1 = Flight(code= '6E810',
    carrier= 'indigo',
    source= 'delhi',
    destination= 'bengaluru',
    fare= 9000,
    duration= 2)

Flight2 = Flight(code= '6E2314',
    carrier= 'indigo',
    source= 'delhi',
    destination= 'bengaluru',
    fare= 2500,
    duration= 4)

Flight3 = Flight(code= 'AI2973',
    carrier= 'air india',
    source= 'delhi',
    destination= 'bengaluru',
    fare= 6000,
    duration= 2.5)

flight_list.add(element=Flight1)

flight_list.add(element=Flight2)

flight_list.add(element=Flight3)

Flight4 = Flight(code= '6E6673',
    carrier= 'indigo',
    source= 'delhi',
    destination= 'bengaluru',
    fare= 5000,
    duration= 3.5)
# print(vars(flight_list))
print('=========================================')
flight_list.add_in_front(element=Flight4)
# print("-------After Adding in Front----------")
# flight_list.show()
# print('=========================================')

Flight5 = Flight(code= 'AI5962',
    carrier= 'air india',
    source= 'delhi',
    destination= 'bengaluru',
    fare= 3500,
    duration= 3)

flight_list.add_in_between(element=Flight5,element1=Flight2,element2=Flight3)
print("-------After Adding in Between----------")
flight_list.show()
print(vars(flight_list))
print('=========================================')

# flight_list.delete_last()
# print("-------After Deleting Last----------")
# flight_list.show()
# print('=========================================')

# flight_list.delete_front()
# print("-------After Deleting Front----------")
# flight_list.show()
# print('=========================================')

# flight_list.delete(code= '6E2314',
#     carrier= 'indigo',
#     source= 'delhi',
#     destination= 'bengaluru',
#     fare= 2500,
#     duration= 4)
# print("-------After Deleting in Between----------")
# flight_list.show()
# print('=========================================')
