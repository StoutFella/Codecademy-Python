#LEGEND
# Test your code in terminal by typing: python3 script.py

#4
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

#5
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#8-10
def get_destinations_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#11
los_angeles_index = get_destinations_index('Los Angeles, USA')
#print(los_angeles_index)  #Output: 2

#12
paris_index = get_destinations_index('Paris, France')
#print(paris_index) #Output: 0

#13-14
#Argument not in list, python throws ValueError
#print(get_destinations_index('Hyderabad, India'))

#15-18
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destinations_index(traveler_destination)
  return traveler_destination_index

#19
test_destination_index = get_traveler_location(test_traveler)

#20-21
#print(test_destination_index) #Output: 1 (Shanghai, China)

#VISITING INTERESTING PLACES

#24
attractions = []

#25-26
for destination in destinations:
  attractions = [[] for destination in destinations]
#print(attractions)

#27-28
#MISSING STEPS FROM CODECADEMY COURSE 29 & 30 - MOVE ON TO #31
def add_attraction(destination,attraction):
#31
    destination_index = get_destinations_index(destination)
#32
    attractions_for_destination = attractions[destination_index].append(attraction)
    return attractions_for_destination

#33
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])

#34
#print(attractions)  #Output: [[], [], [['Venice Beach', ['beach']]], [], []]

#35
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

#36
print(attractions)  #Output: [[['the Louvre', ['art', 'museum']]...['Egyptian Museum', ['museum']]]]

#37 Commit changes to git with message "Created attractions and functionality for adding new attractions"

#FINDING THE BEST PLACES TO GO
#38`
