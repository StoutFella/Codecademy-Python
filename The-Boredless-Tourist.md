<h1 align="center">The Boredless Tourist</h1>

<p align="center">Welcome to <strong>The Boredless Tourist</strong>, an online application giving you the power to find the parts of the city that fit the pace of your life.</p>
<p>
  We at <em>The Boredless Tourist</em> run a recommendation engine using <em>Python</em>. We first evaluate what a person’s interests are and then give them recommendations in their area to venues, restaurants, and historical destinations that we think they’ll be engaged by.
</p>

<p align="center">
  <img src="https://i.pinimg.com/originals/d3/0c/5e/d30c5e2a19f3d791530dbb164246f562.gif" align="center" width="330" alt="The Borderless Tourist"  title="Traveling Tourist"/>
</p>

<div align="center"><h3>Let’s get started!</h3></div>

<div align="center">
  <hr width="150">
</div><br>

<p>1. We here at <em>The Boredless Tourist</em> believe that mistakes should be easily corrected, so we keep all of our code version controlled using <code>git</code>. Start by running <code>git init</code> in the terminal.</br></p>

<p>2. We’ll do most of our coding in <code>script.py</code> so we want to make sure, we are tracking that in git. Add <code>script.py</code> to git’s staging area.</p>

<p>3. Let’s create the first commit for this project. Perform a <code>git commit</code> with the message "initial commit".</p>


<p>4. Now let’s create some data that we’re going to use to test the functionality that we create for The Boredless Tourist. The first is our list of destinations that we’re going to be using.

Create a list with the following destinations and save it into a variable called <code>destinations</code>.

<ul>
  <li>“Paris, France”</li>
  <li>“Shanghai, China”</li>
  <li>“Los Angeles, USA”</li>
  <li>“São Paulo, Brazil”</li>
  <li>“Cairo, Egypt”</li>
</ul>
</p>

<p>5. Let’s define a test traveler to see how our functionality is working so far.

Create a <code>test_traveler</code> variable. Assign to it the following list:

<code>['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]</code>

This is a traveler (a user of The Boredless Tourist application) whose name is Erin Wilkes who likes historical buildings and art. Erin is in China right now, hopefully we can find some good places to show her.</p>

<p>6. Looks like we’ve got some good sample data to get started with. Let’s commit these changes.</br>

First, save the file, then add <code>script.py</code> to the git index using <code>git add</code>.</p>

<p>7. Next, perform a <code>git commit</code> with the message <code>"Added test objects"</code>.</p>

<h3 align="center">Travelling To Faraway Lands</h3>

<p>8. Now that we have test data for a traveler and a list of destinations that we can use, we can start building some of the Boredless Tourist‘s functionality.</br></br>

When a traveler arrives at a destination, we want to know where they are! Since we use lists for all of our data — we are going to identify each location based on its index in our destinations list. But we need to retrieve that index first.

Define a function called <code>get_destination_index()</code>. It should take a single parameter, <code>destination</code>, the destination as a string.</p>

<p>9. In the body of <code>get_destination_index()</code>, find the index of destination and save the results into a variable called <code>destination_index</code>.</p>

<p>10. In the body of <code>get_destination_index()</code>, after you’ve defined <code>destination_index</code>, <strong>return</strong> it.</p>

<p>11. Test out your function. Try to call <code>get_destination_index()</code> with the argument <em>"Los Angeles, USA"</em>.

Print out the results. Save your code and then run it by typing <code>python3 script.py</code> in the terminal.

Is the destination index for <em>“Los Angeles, USA”</em> equal to 2?</p>

<p>12. Try to call <code>get_destination_index()</code> with the argument <em>“Paris, France”</em> instead. Since that is the first element on our <code>destinations</code> list, it should return the index 0.</p>

<p>13. What happens if we call <code>get_destination_index()</code> with a destination not in our destinations list? :thinking:

Try it now: call <code>get_destination_index()</code> with the argument <em>“Hyderabad, India”</em>. What happens?</p>

<p>14. If you used the <code>.index()</code> method to get the index of a destination from the list, you’ll notice that calling <code>get_destination_index()</code> with data that is missing from our destinations list will raise a <strong>ValueError</strong>. </br></br>

Don’t add logic to avoid triggering this ValueError, it’s going to be useful for us in the future.</p>

<p>15. Now let’s define a function called <code>get_traveler_location()</code></br></br>

<code>get_traveler_location()</code> is going to take a single parameter, <em>traveler</em></p>

<p>16. In the body of <code>get_traveler_location()</code>, access the traveler’s destination string and save it into <code>traveler_destination</code>.</p> 

<p>17. Use <code>traveler_destination</code> along with <code>get_destination_index()</code> to retrieve the index of the destination where the traveler is. 

Save the index of the traveler’s destination into the variable <code>traveler_destination_index</code>.</p>

<p>18. Make <code>get_traveler_location()</code> <em>return</em> the destination index of the traveler by returning <code>traveler_destination_index</code></p>

<p>19. Create a variable called <code>test_destination_index</code>. Save the results of calling <code>get_traveler_location()</code> with our <code>test_traveler</code>.</p>

<p>20. Print out <code>test_destination_index</code>.</p>

<p>21. Save your code and run it by calling <code>python3 script.py</code> in the terminal. Is the <code>test_destination_index</code> you created equal to 1?</p> 

<p>22. Let’s save our work to the git tracker. Add <code>script.py</code> to the git index with <code>git add</code></p>

<p>23. And commit your changes with the message <em>"Added logic to find traveler destinations and convert to internal data"</em></p>

<h3 align="center">Visiting Interesting Places</h3>

<p>24. Now we want to create and maintain a list of attractions. Let’s start by defining a list called <code>attractions</code></p>

<p>25. Actually, we want attractions to be an empty list for every destination in destinations. You can do this with this code:

<code python>attractions = [[], [], [], [], []]</code> <strong>But</strong> there are other ways to accomplish the same thing: <em>by looping through destinations</em> or with a <em>list comprehension</em>.

Define attractions to be a list of 5 (one for each test destination) empty lists using a loop or list comprehension.</p>

<p>26. Print out your attractions. Save, and then run your code by typing <code>python3 script.py</code> in the terminal. Does attractions look like: <code python>[[], [], [], [], []]</code></p>

<p>27. Now let’s create a function called <code>add_attraction()</code>. This function should take two parameters: <em>destination</em>, the name of the location and attraction, the <em>attraction</em>.</p>

<p>28. First we should attempt to find the index of the destination. Use <code>get_destination_index()</code> with the passed in destination in order to retrieve the index of the destination. Save the results into <code>destination_index</code>.</p>

<h4>29 - 30. This task is no longer necessary. It has been left blank so the project tasks stay aligned with the walkthrough video. <code>Move on to task 31.</code></h4>

<p>31. If the destination does exist, then we already have a list for it in attractions. Use the <code>destination_index</code> to find the appropriate list in attractions and save that list to <code>attractions_for_destination</code>.</p>

<p>32. <em>Append</em> the attraction passed into <code>add_attraction</code> to the list <code>attractions_for_destination</code>. That’s all we want this function to do, so we can return after adding the attraction to the list.</p>

<p>33. Try adding the following attraction: <code>['Venice Beach', ['beach']]</code>
To the “Los Angeles, USA” destination by calling <code>add_attraction()</code> with the two as arguments.</p>

<p>34. Print out attractions. Then save and run your code with <code>python3 script.py</code>. Your print statement should render the following: <code>[[], [], [['Venice Beach', ['beach']]], [], []]</code> If it doesn’t something went wrong with <code>add_attraction()</code>.

<p>34. Let’s add a few more interesting places to go, paste the following code to add a few more attractions:

<p>35. <code python>add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])</code>.</p>

<p>36. Let’s add this change to our git repo. First add <code>script.py</code> to your git index.</p>

<p>36. Then <code>commit</code> the changes with the message:

<em>"Created attractions and functionality for adding new attractions"</em></p>

<h3 align="center">Finding the Best Places to Go</h3>

<h1>To be Continued...</h1>
