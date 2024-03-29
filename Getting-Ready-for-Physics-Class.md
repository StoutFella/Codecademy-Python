<h1 align="center"># Getting-Ready-for-Physics-Class</h1>


You are a physics teacher :man_teacher: preparing for the upcoming semester. You want to provide your students with some  `functions` that will help them calculate some fundamental physical properties.


<em><h4>Equations to use:</h4></em>
  <ul>
    <li>
      <samp>Temp (C) = (Temp (F) - 32) * 5/9</samp>
    </li>
      <li>	
        <samp>Temp (F) = Temp (C) * (9/5) + 32</samp>
    </li>
  </ul>
  
<em><h4>Given Variables:</h4></em>
  <ul>
    <li>
      <samp>train_mass = 22680</samp>
    </li>
    <li>
      <samp>train_acceleration = 10</samp>
    </li>
      <li>
      <samp>train_distance = 100</samp>
    </li>
    <li>
      <samp>bomb_mass = 1</samp>
    </li>
  </ul>
  

<hr style="border:1px solid gray"> </hr>

1. Write a function called `f_to_c` that takes an input `f_temp`, a temperature in Fahrenheit, and converts it to `c_temp`, that temperature in Celsius. It should then return `c_temp`.

2. Let’s test your function with a value of 100 Fahrenheit. Define a variable `f100_in_celsius` and set it equal to the value of `f_to_c` with 100 as an input.

3. Write a function called `c_to_f` that takes an input `c_temp`, a temperature in Celsius, and converts it to `f_temp`, that temperature in Fahrenheit. It should then return `f_temp`.

4. Test your function with a value of 0 Celsius. Define a variable `c0_in_fahrenheit` and set it equal to the value of `c_to_f` with 0 as an input.

5. Define a function called `get_force` that takes in mass and acceleration. It should return mass multiplied by acceleration.

6. Test `get_force` by calling it with the variables `train_mass` and `train_acceleration`. Save the result to a variable called `train_force` and print it.

7. Print the string **“The GE train supplies `X` Newtons of force.”**, with `X` replaced by `train_force`.

8. Define a function called `get_energy` that takes in mass and c. c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8. `get_energy` should return mass multiplied by c squared.

9. Test `get_energy` by using it on `bomb_mass`, with the default value of c. Save the result to a variable called `bomb_energy`.

10. Print the string **“A 1kg bomb supplies `X` Joules.”**, with `X` replaced by `bomb_energy**.

11. Define a final function called `get_work` that takes in mass, acceleration, and distance. Work is defined as force multiplied by distance. First, get the force using `get_force`, then multiply that by **distance**. Return the result.

12. Test `get_work` by using it on `train_mass`, `train_acceleration`, and `train_distance`. Save the result to a variable called `train_work`.

13. Print the string **"The GE train does `X` Joules of work over `Y` meters."**, with `X` replaced with `train_work` and `Y` replaced with `train_distance`.

<hr style="border:1px solid gray"> </hr>

<p align="center">
<img src="https://c.tenor.com/ANQ5MHKx7EYAAAAC/star-wars-dark-side.gif" alt="may the force with you!" width="auto" height="150" border="10"/>
</p>
