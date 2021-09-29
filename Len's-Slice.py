toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2) #.count method returns the number of elements with the specified value
print(num_two_dollar_slices)  #3

num_pizzas = len(toppings)
print(num_pizzas) #7
print()

print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')  # str() method is needed for string concatenation
print()

pizza_and_prices = [[ 2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3,'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
print(pizza_and_prices)
print()

pizza_and_prices.sort() #sort the two-dimensional list using the first index element (price)
print(pizza_and_prices)
print()

cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza) #cheese

print()
last_item = pizza_and_prices[-1]
priciest_pizza = pizza_and_prices.pop(-2) #anchovies removed from list
print(priciest_pizza) #pineapple
print()

pizza_and_prices.insert(4, [2.5, "peppers"]) 
print(pizza_and_prices) #[[1, 'cheese'], [2, 'mushrooms'], [2, 'olives'], [2, 'pepperoni'], [2.5, 'peppers'], [3, 'sausage'], [7, 'anchovies']]

print()

three_cheapest = pizza_and_prices[:3] #slice the sorted list to 3 elements
print(three_cheapest)

#A slice for a mice is always nice!
