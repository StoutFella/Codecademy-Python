<br><h1 align="center">Scrabble</h1>
<p align="center">
  <img src="https://i.giphy.com/media/l2JejeFAnbX7Ixrag/giphy.webp" align="right" width="220" alt="Simpons playing scrabble"  title="Scrabble"/><br>
</p>
<p align="left">In this project, you will process some data from a group of friends playing scrabble. You will use dictionaries to organize players, words, and points. There are many ways you can extend this project on your own if you finish and want to get more practice!</p>
</br>
</br></br></br>
<h3 align="center">BUILD YOUR POINT DICTIONARY</h3></br>

```python
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

```

<p>1. We have provided you with two lists, <code>letters</code> and <code>points</code>. We would like to combine these two into a dictionary that would map a letter to its point value. Using a list comprehension and zip, create a dictionary called <code>letter_to_points</code> that has the elements of letters as the <em>keys</em> and the elements of points as the <em>values</em>.</p>

<p>2. Our letters list did not take into account blank tiles. Add an element to the <code>letter_to_points</code> dictionary that has a key of <mark>" "</mark> and a point value of <mark>0</mark>.</p>

<p>3. We want to create a function that will take in a word and return how many points that word is worth. Define a function called <code>score_word</code> that takes in a parameter <code>word</code>.</p>

<p>4. Inside <code>score_word</code>, create a variable called <code>point_total</code> and set it to <code>0</code>.</p>

<p>5. After defining <code>point_total</code>, create a for loop that goes through the letters in word and adds the point value of each letter to <code>point_total</code>. You should get the point value from the <code>letter_to_points</code> dictionary. If the letter you are checking for is not in <code>letter_to_points</code>, add 0 to the <code>point_total</code>.</p>

<p>6. After the for loop is finished, return <code>point_total</code>.</p>

<p>7. Let’s test this function! Create a variable called <code>brownie_points</code> and set it equal to the value returned by the <code>score_word()</code> function with an input of <mark>"BROWNIE"</mark></p>

<p>8. We expect the word BROWNIE to earn 15 points:</p>

```python
(B + R + O + W + N + I + E)
 
(3 + 1 + 1 + 4 + 4 + 1 + 1) = 15
```
</br>

<h3 align="center">SCORE A GAME</h3></br>

<p>9. Create a dictionary called <code>player_to_words</code> that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:


| player1  | wordNerd  | Lexi Cont| Prof Reader|
| :------- |:----------| :--------| ----------:|
| BLUE     |   EARTH   | ERASER   | ERASER     |
| TENNIS   |   EYES    | BELLY    | BELLY      |
| EXIT     |   MACHINE | HUSKY    | HUSKY      |

</p><br>
<p>10. Create an empty dictionary called <code>player_to_points</code></p>

<p>11. Iterate through the items in <code>player_to_words</code>. Call each player player and each list of words words. Within your loop, create a variable called <code>player_points</code> and set it to <mark>0</mark>

<p>12. Within the loop, create another loop that goes through each word in words and adds the value of <code>score_word()</code> with <em>word</em> as an input.</mark></p>

<p>13. After the inner loop ends, set the current player value to be a key of <code>player_to_points</code>, with a value of <code>player_points</code></p>

<p>14. <code>player_to_points</code> should now contain the mapping of players to how many points they’ve scored. Print this out to see the current standings for this game! If you’ve calculated correctly, <code>wordNerd</code> should be winning by <mark>1</mark> point.</p></br>

<h3 align="center">IDEAS FOR FURTHER PRACTICE</h3></br>

<p>15. If you want extended practice, try to implement some of these ideas with the Python you’ve learned:

<ul>
  <li><code>play_word()</code> — a function that would take in a player and a word, and add that word to the list of words they’ve played</li>
  <li><code>update_point_totals()</code> — turn your nested loops into a function that you can call any time a word is played</li>
  <li>Make your <code>letter_to_points</code> dictionary able to handle lowercase inputs as well</li>
</ul>
</p>
