Finally, there are some conditions under which none of these messages will get printed. Instead of ending the program without outputting anything, we should print the message

```text
Perfect weather. Enjoy the outdoors!
```

Find out what condition must go in the `elif` header in line 22 to do so.

<div class="hint">
  We want to print this message only if none of our other messages gets printed. Thus we want to print it when all of the conditions that lead to one of those messages are false.
</div>

<div class="hint">
  You should combine the negations of each condition that leads to printing a message (e.g. for <pre style="display: inline">Take an umbrella!</pre>, the condition is <pre style="display: inline">rain</pre>) with <pre style="display: inline">and</pre> operations.
</div>
