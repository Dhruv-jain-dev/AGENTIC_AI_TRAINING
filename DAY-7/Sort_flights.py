from Search_flight import flights
# print(flights)

# Sort on the fare, LOW to HIGH
def sort(flights, key, low_to_high=True):
    for i in range(len(flights)):
        for j in range(len(flights) - 1 - i):

            if low_to_high:
                if flights[j][key] > flights[j+1][key]:
                    flights[j], flights[j+1] = flights[j+1], flights[j]
            else:
                if flights[j][key] < flights[j+1][key]:
                    flights[j], flights[j+1] = flights[j+1], flights[j]


criteria = input('Enter Sorting Criteria: fare/duration: ')

# sort(flights)
sort(flights, criteria, low_to_high=False)

for flight in flights:
    print(flight)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')