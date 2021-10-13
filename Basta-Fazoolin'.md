<h1 align="center">Basta Fazoolin'</h1>

<div><p align="center">You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.</p>

<img align="center">![Basta Fazool](https://y.yarn.co/dc000e31-38b3-4785-abed-752c2475a36d_text.gif)</div></br></br> 

<h3 align="center">MAKING THE MENUS</h4></br>

<p>1. At <span title="Basta Fazoolin">Basta Fazoolin’</span> with my Heart our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids.

Create a `Menu class`.</p>

<p>2. Give <code>Menu</code> a constructor with the five parameters <em>self</em>, <em>name</em>, <em>items</em>, <em>start_time</em>, and <em>end_time</em>.</p>

<p>3. Let’s create our first menu: brunch. </br> Brunch is served from 11am to 4pm. The following items are sold during brunch:

```python
{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
```
</p>

<p>4. Let’s create our second menu item <code>early_bird</code>. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:</p>

```python
{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
```

<p>5. Let’s create our third menu, <code>dinner</code>. Dinner is served from 5pm to 11pm. </br>The following items are available for dinner: </p>


```python
{
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
```

<p>6. And let’s create our last menu, <code>kids</code>. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.</p>

```python
{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
```

<p>7. Give our <code>Menu</code> class a string representation method that will tell you the <code>name</code> of the menu. Also, indicate in this representation when the menu is available.</p>

p>8. Try out our string representation. If you call print(brunch) it should print out something like the following:

```python
brunch menu available from 11am to 4pm
```

</p>

<p>9. Give Menu a method <code>.calculate_bill()</code> that has two parameters: <code>self</code>, and <code>purchased_items</code>, a list of the names of purchased items. Have <code>calculate_bill</code> return the total price of a purchase consisiting of all the items in <code>purchased_items</code>.</p>

<p>10. Test out <code>Menu.calculate_bill()</code>. We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into <code>brunch.calculate_bill()</code> and print out the price.</p>

<p>11. What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with <code>.calculate_bill()</code></p>

<h3 align="center">CREATING THE FRANCHISES</h4></br>

<p>12. Basta Fazoolin’ with my Heart has seen tremendous success with the family market, which is fantastic because when you’re at Basta Fazoolin’ with my Heart with family, that’s great!

We’ve decided to create more than one restaurant to offer our fantastic menus, services, and ambience around the country.

First, let’s create a <code>Franchise</code> class.</p>

<p>13. Give the Franchise class a constructor. Take in an <code>address</code>, and assign it to <code>self.address</code>. Also take in a list of <code>menus</code> and assign it to <code>self.menus</code></p>

<p>14. Let’s create our first two franchises! Our flagship store is located at <code>"1232 West End Road"</code> and our new installment is located at <code>"12 East Mulberry Street"</code>. Pass in all four menus along with these addresses to define <code>flagship_store</code> and <code>new_installment</code>.</p>

<p>15. Give our Franchises a string representation so that we’ll be able to tell them apart. If we print out a <code>Franchise</code> it should tell us the address of the restaurant.</p>

<p>16. Let’s tell our customers what they can order! Give <code>Franchise</code> an <code>.available_menus()</code> method that takes in a <code>time</code> parameter and returns a list of the <code>Menu</code> objects that are available at that time.</p>

<p>17. Let’s test out our <code>.available_menus()</code> method! Call it with 12 noon as an argument and print out the results.</p>

<p>18. Let’s do another test! See what is printed if we call <code>.available_menus()</code> with 5pm as an argument and print out the results.</p></br>

<h3 align="center">CREATING BUSINESSES</h4></br>

<p>19. Since we’ve been so successful building out a branded chain of restaurants, we’ve decided to diversify. We’re going to create a restaurant that sells arepas! First let’s define a <code>Business</code> class.</p>

<p>20. Give <code>Business</code> a constructor. A Business needs a <code>name</code> and a list of <code>franchises</code>.</p>

<p>21. Let’s create our first <code>Business</code>. The name is <code>"Basta Fazoolin' with my Heart"</code> and the two franchises are <code>flagship_store</code> and <code>new_installment</code>.</p>

<p>22. Before we create our new business, we’ll need a <code>Franchise</code> and before our Franchise we’ll need a menu. The items for our <em>Take a’ Arepa</em> available from 10am until 8pm are the following:</p>

```python
{
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
```
<p>Save this to a variable called <code>arepas_menu</code>.</p>

<p>23. Next let’s create our first <em>Take a’ Arepa</em> franchise! Our new restaurant is located at <code>"189 Fitzgerald Avenue"</code>. Save the Franchise object to a variable called <code>arepas_place</code>.</p>

<p>24. Now let’s make our new <code>Business</code>! The business is called <code>"Take a' Arepa"!</code></p>

<p>25. <strong>Congrats!</strong> You created a system of classes that help structure your code and perform all business requirements you need. Whenever we need a new feature we’ll have the well-organized code required to make developing and shipping it easy.</p></br>

<h3 align="center"> Well Done!</h3>
