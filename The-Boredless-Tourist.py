                    #LEGEND
# You can test your code in terminal by typing: python3 script.py 


#1 Start by initializing our project in terminal with: git init
#2 Add script.py to the staging aread by running in terminal: git add script.py
#3 Perform a git commit with the message "inital commit"

#4
destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

#5
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#6 Save the file and add script.py to git index using: git add
#7 git commit with message "Added test objects"

                    #TRAVELLING TO FARAWAY LANDS

#8-10
#returns an index of a destination as variable, destination_index | see #11 & #12 as example
def get_destinations_index(destination):  
  destination_index = destinations.index(destination) 
  return destination_index

#11
los_angeles_index = get_destinations_index('Los Angeles, USA')
print(los_angeles_index)  #Output: 2

#12
paris_index = get_destinations_index('Paris, France')
print(paris_index) #Output: 0

#13-14
print(get_destinations_index('Hyderabad, India')) #Output: Argument not in list, python throws ValueError

#15-18
#returns an index of the traveler as variable, traveler_destination_index | see #20 & #21 as example
def get_traveler_location(traveler):
  traveler_destination = traveler[1]  #travelers location is the 2nd element on list, test_traveler
  traveler_destination_index = get_destinations_index(traveler_destination) #The function, get_destinations_index takes the travelers location index (traveler_destination) as argument and returns the index of the location (if it exists) inside the destinations list as the variable, traveler_destination_index.
  return traveler_destination_index

#19
test_destination_index = get_traveler_location(test_traveler) #Test if our get_traveler_location function works, results in #20-21

#20-21
print(test_destination_index) #Output: 1 (Shanghai, China)

                    #VISITING INTERESTING PLACES

#24
attractions = []  #There should be an attraction for each destination. Lets loop through each destination and add an empty list (this empty list will hold the argument from the function, add_attraction (Example: if a user wants to add an attraction)

#25-26
for destination in destinations:
  #Option 1(using .append method append an empty array)
  attractions.append([])  # Output: [[], [], [], [], []]
  #Option 2 (List Comprhension): 
  # attractions = [[] for destination in destinations]  
print(attractions)  #Output: [[], [], [], [], []]
print(destinations) #Output: ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

#27-28
#MISSING STEPS FROM CODECADEMY COURSE 29 & 30 - MOVE ON TO #31
def add_attraction(destination,attraction): #If a user wants to add an attraction (attraction argument is a list type)
#31
    #destination_index is locally scoped inside this function, add_attraction (not to be confused with the variable named the same from function, get_destinations_index (you shouldn't have scope error)
    destination_index = get_destinations_index(destination) #Function call that returns an index
#32
    #goes to the attractions list (#24) and appends an attraction a user provides as the second argument from add_attraction function
    attractions_for_destination = attractions[destination_index].append(attraction) #appends the attraction list after the destination (because the destination index is the result of calling the get_destinations_index(destination) function)
    return attractions_for_destination

#33
add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])

#34
print(attractions)  #Output: [[], [], [['Venice Beach', ['beach']]], [], []]

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

#38-42
def find_attractions(destination,interests):
  destination_index = get_destinations_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []

#43-44
#This will iterate through the attractions  
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1] #returns tags of attractions like, ['museum], ['zoo']
#45-46
    for interest in interests:
      if interest in attraction_tags:
#49 
        attractions_with_interest.append(possible_attraction[0]) 
        # By adding an index[0] to possible_attraction, you show the name of the attraction & not the search tags ('art', 'museum' etc...) 
        #IS THIS WHAT PROGRAMMERS CALL ABSTRACTION?
  return attractions_with_interest

#47
la_arts = find_attractions('Los Angeles, USA', ['art'])  
#48
print(la_arts)  #Output: [['LACMA', ['art', 'museum']]]

#50
print(la_arts) #Output after step #49: ['LACMA']

#51
#git add script.py

#52
#git commit - m "Added interest finder logic"



                    #SEE THE PARTS OF A CITY YOU WANT TO SEE

#53-60
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi ' + traveler[0].title() + ", we think you'll like these places around " + traveler_destination.title() + ": "

  for i in range(len(traveler_attractions)):
    if(traveler_attractions[-1] == traveler_attractions[i]):
      interests_string += 'the ' + traveler_attractions[i].title() + '.'
    else:
      interests_string += 'the ' + traveler_attractions[i].title() + ', '
  return interests_string

#61
smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']]) 

#62
print(smills_france)  #Output: Hi Dereck Smill, we think you'll like these places around Paris, France: the Arc De Triomphe.

#63
#git add script.py

#64
#git commit -m "Added function to generate message for traveler and present attractions they might be interested in."