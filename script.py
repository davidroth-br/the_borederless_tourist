destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    #for i in range(len(destinations)):
    #    if destinations[i] == destination:
    #        destination_index = i
    #return destination_index
    return destinations.index(destination)

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = destinations.index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)
# print(get_destination_index("São Paulo, Brazil"))