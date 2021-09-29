<h1 align="center">Len's Slice</h1>
<p align="center">You work at Len’s Slice, a new pizza joint in the neighborhood. Use your knowledge of Python lists to organize some of your sales data. </p>

<p align="center">
  <img src="https://c.tenor.com/yBbrOgB6tXQAAAAC/ratatouille-cheese.gif" alt="Remy eating pizza" title="Remy eating pizza"/>
</p>

<h3>Make Some Pizzas</h3>

A. To keep track of the kinds of pizzas you sell, create a list called toppings that holds the following:
<p display="inline" list-style="none">
  <ul>
    <li>"pepperoni"</li><li>"pineapple"</li><li>"cheese"</li><li>"sausage"</li><li>"olives"</li><li>"anchovies"</li><li>"mushrooms"</li>
  </ul>
</p>

B. To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
<p>2, 6, 1, 3, 2, 7, 2</p>

C. Your boss wants you to do some research on $2 slices. Count the number of occurrences of 2 in the prices list, and store the result in a variable called `num_two_dollar_slices`. 
Print it out.

D. Find the length of the toppings list and store it in a variable called `num_pizzas`.

E. Print the string <em>'We sell `num_pizzas` different kinds of pizza!'</em>. `num_pizzas` represents the value of our variable `num_pizzas`.

F. Convert our toppings and prices lists into a 2-dimensional list called `pizza_and_prices` that has the following associated values. Each sublist in `pizza_and_prices` should have one pizza topping and an associated price.

<strong>Price	Topping:</strong>
<ul><li>2	"pepperoni"</li>
<li>6	"pineapple"</li>
<li>1	"cheese"</li>
<li>3	"sausage"</li>
<li>2	"olives"</li>
<li>7	"anchovies"</li>
<li>2	"mushrooms"</li></ul>

<em align="center">For this project make sure the prices come before the topping name like so:</em> [price, topping_name]

G. Print `pizza_and_prices`. Does it look the way you expect?

<h3>Sorting and Slicing Pizzas</h3>

H. Sort `pizza_and_prices` so that the pizzas are in order of increasing price (ascending).

I. Store the first element of `pizza_and_prices` in a variable called cheapest_pizza.

J. A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!” Get the last item of the `pizza_and_prices` list and store it in a variable called `priciest_pizza`.

K. It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. Remove it from our `pizza_and_prices` list since the man bought the last slice.

L. Since there is no longer an "anchovies" pizza, you want to add a new topping called "peppers" to keep your customers excited about new toppings. 
Here is what your new topping looks like: [2.5, "peppers"]. Add the new peppers pizza topping to our list `pizza_and_prices`.

<strong>Note:</strong> Make sure to position it relative to the rest of the sorted data in `pizza_and_prices`, otherwise our data will not be correctly sorted anymore!

M. Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

O. Slice the `pizza_and_prices` list and store the 3 lowest cost pizzas in a list called `three_cheapest`.

P. <strong>Great job! :thumbsup: </strong> The mice are very pleased and will be leaving you a 5-star review.

Q. Print the `three_cheapest` list.
