* The variable `rain` is a boolean. If it is `True`, it means there's a chance of rain, otherwise it's `False`. 
* The variable `uvi` contains the [UV index <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/UV_index) as an integer
* The variable `temp` contains the temperature in degrees Celsius
* The variable `wind` contains the wind speed in meters per second $(\mathrm{m/s})$

Now, we want to do something about temperature.

* If the temperature is between $12\\, º\mathrm{C} $ and $5\\, º\mathrm{C} $ (both included), print `Wear a raincoat!` if it is raining and a `Wear a winter coat!` otherwise.

* If the temperature is *at least* $20\\, º\mathrm{C} $, print `Wear light clothes!`.

* If the temperature is *lower* than $5\\, º\mathrm{C} $, print `Wear a winter jacket!`.


You'll have to do this in a single `if`-`else` statement with exactly 3 clauses! (Keep in mind that `elif` clauses are part of the same `if`-`else` statement.)

<div class="hint">
  Use a conditional expression inside the `print` call of one of the clauses.
</div>

<div class="hint">
  Use string concatenation in combination with a conditional expression in the clause mentioned by Hint 1.
</div>


------------

If you want a small challenge, there's also a way to write this as a single `if`-`else` statement (with one or more clauses), without any conditional expressions or other control flow statements.

