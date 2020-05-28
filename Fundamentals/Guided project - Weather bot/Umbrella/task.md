
Now that we've validated the input, we can proceed to output messages based on the weather conditions we got. 
We can do this under the `else` clause of line 17 (if the program runs it, we know that the input is valid and `forecast` is not `None`).

Line 18 extracts the data we're interested in from the `weather` object into the variables `rain`, `clouds`, `temp`, `wind` .

* The variable `rain` is a boolean. If it is `True`, it means there's a chance of rain, otherwise it's `False`. 
* The variable `uvi` contains the [UV index <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/UV_index) as an integer
* The variable `temp` contains the temperature in degrees Celsius
* The variable `wind` contains the wind speed in meters per second $(\mathrm{m/s})$

Your task is to print `Take an umbrella!` if there's a chance of rain. 

Make sure to run your program to see if it works so far.
