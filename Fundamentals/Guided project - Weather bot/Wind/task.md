* The variable `rain` is a boolean. If it is `True`, it means there's a chance of rain, otherwise it's `False`. 
* The variable `uvi` contains the [UV index <img height="12" style="display: inline" src="https://raw.githubusercontent.com/webartifex/intro-to-python/master/static/link_to_wiki.png">](https://en.wikipedia.org/wiki/UV_index) as an integer
* The variable `temp` contains the temperature in degrees Celsius
* The variable `wind` contains the wind speed in meters per second $(\mathrm{m/s})$


All of these messages aren't of much use if we can't go outside.

Make an `if` statement such that if the wind speed is *strictly above* $20\\, \mathrm{m/s}$, a message saying 
```text
Very strong winds, don't go outside!
```
gets printed and nothing else (so no `Take an umbrella!` messages for example, regardless of rain conditions).



