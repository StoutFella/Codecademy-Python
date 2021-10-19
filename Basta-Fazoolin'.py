                    #CREATING BUSINESSES!

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises                 

                  
                    #CREATING THE FRANCHISES

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

#15A
  def __repr__(self):
    return self.address

  def available_menus (self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus


                       #MAKING THE MENUS

class Menu:

  def __init__(self,name,items,start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return self.name + " menu available from " + str(self.start_time) + " to " + str(self.end_time)

  def calculate_bill(self, purchased_items):
    bill = 0
    for purhcased_item in purchased_items:
      if purhcased_item in self.items:
        bill += self.items[purhcased_item]
    return bill


#Brunch Menu
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print(brunch_menu)

#The purchased items ('pancakes', 'home fries', 'coffee') below can be passed into the calculate_bill function as dictionary items {} or list itmes []. The function has to loop through each item so you have to pass each items in an iteratable data type (dictionary or list).
#print(brunch_menu.calculate_bill({'pancakes', 'home fries', 'coffee'})) #dictionary items

#Early Bird Menu
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

early_bird_menu  = Menu('Early Bird', early_bird_items, 1500, 1800)
#print(early_bird_menu)

#print(early_bird_menu.calculate_bill(['salumeria plate','mushroom ravioli (vegan)'])) #list items

#Dinner Menu
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

dinner_menu  = Menu('Dinner', dinner_items, 1700, 2300)
#print(dinner_menu)

#Kids Menu
kids_menu_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kids_menu  = Menu('Kids', kids_menu_items, 1100, 2100)
#print(kids_menu)

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#15B
#print(flagship_store.address)  #Output: 1232 West End Road
#print(new_installment.address)  #Output: 12 East Mulberry Street

#print(flagship_store.available_menus(1200)) 
#Output: [Brunch menu available...1600, Kids menu...to 2100]

#print(new_installment.available_menus(1700)) 
#Output: [Early Bird menu...1800, Dinner menu...2300, Kids menu...2100]

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])


                        #AREPA BUSINESS
arepeas_items = { 'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Take a’ Arepa", arepeas_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])  #arepas_menu is in a list, because there may be more menu types

#25
arepa = Business("Take a' Arepa", [arepas_place]) #arepas_place is in a list, because there may be more franchise stores, you can access each store with the index

print(arepa.franchises[0].menus[0])   #Take a’ Arepa menu available from 1000 to 2000