# Loops: the `while` loop


The while loop executes a block of code *while* a condition is true. That is, it executes the block repeatedly until the condition becomes false.


The syntax for a while loop in Python is
```python
while <condition>:
    <stmt_1>
    <stmt_2>
    ...
    <stmt_n>
```
where `<condition>` is an expression that will be interpreted as a boolean (see Truth Value Testing), and `<stmt_1>` through `<stmt_n>` are statements (they form a code block). 
<!-- TODO: add cross-reference -->

Immediately after the while loop ends, the condition is always false, by definition. This can be taken advantage of in the code following the loop.
