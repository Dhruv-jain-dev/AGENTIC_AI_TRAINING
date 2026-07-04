from Search_flight import flights

def filter_flights(flights, carrier=None, fare=None, price_condition='less_than', duration=None):
    results = []

    for flight in flights:
        if carrier is not None and flight['carrier'].lower() != carrier.lower():
            continue

        if fare is not None:
            if price_condition == 'less_than' and flight['fare'] >= fare:
                continue
            if price_condition == 'greater_than' and flight['fare'] <= fare:
                continue

        if duration is not None and flight['duration'] >= duration:
            continue

        else:
            results.append(flight)

    return results


def fliter(flights, carrier=None, fare=None, price_condition='less_than', duration=None):
    return filter_flights(flights, carrier, fare, price_condition, duration)


filtered_flights = fliter(
    flights,
    carrier='indigo',
    fare=4000,
    price_condition='less_than',
    duration=5
)

for flight in filtered_flights:
    print(flight)