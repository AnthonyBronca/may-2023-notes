## Today's Topics:
Functions
Lambda Functions
Lists

---

## Functions

---

### Python Functions
- We use the `def` keyword to define a function followed by:
    - The name of the function
    - The parameters that it accepts
    - A new block identified as `:` and indent the next line
```python=
def is_even(num):
    return num % 2 == 0

print(is_even(5)) # False
print(is_even(2)) # True
```

---

### Lambda Functions

- For simple one-line functions, we can also use a lambda, which takes in:
    -  Parameters on left side of `:`
    -  Returns the value resulting from the right side of the `:`
-  They return automatically and cannot contain an explicit `return` keyword
-  Lambda functions are meant to be anonymous, one-liner functions


```python=
is_even = lambda num: num % 2 == 0

print(is_even(8)) # True
```

---

### Python Scoping

- Scoping is done at the function (and class) level
    - In JS, we had block scopes
    - In PY, our `if` statements do not create new scopes

```python=
def make_a_five():
    y = 5
    return y

if True:
    x = 10


print(x) #10
# `x` was created in the global scope

print(y) # NameError: name 'y' is not defined
# `y` was created in the scope of the make_a_five function
```

---

### Docstrings

A docstring is a string literal that is used to document a function, class, or module.

```python=
def my_function():
    """
    This is my function. It doesn't do
    anything special. It's just a
    function.
    """
    return 1
```

We can access docstrings in two ways:
```python=
help(my_function)
print(my_function.__doc__)
```

### Adding n amount of Positional args
- In javascript we are able to use the rest operator (...) to add positional arguments to a function and store them in an array.
- We have something similar we can use is python. with the (*) operator

```
# js example
function add(a, b, ...args) {
  let total = a + b;
  console.log('extra args', args, Array.isArray(args))
  for (let n of args) {
    total += n;
  }
  return total;
}


add(2, 3, 4, 5) // returns 14

# python example
# by convention this i called args
def add(a, b, *args):
    total = a + b;
    print('extra args', args)
    for n in args:
        total += n
    return total

add(2, 3, 4, 5) # Returns 14
```

### Keyword arguments
- Unlike JavaScript, Python has the built-in ability to specify arguments by name without resorting to destructuring. You can just write the name of the parameter and an equal sign before the value you pass as a parameter. By specifying the names of the arguments, you can provide them in any order.

```
def greeting(name, saying="Hello"):
    print(saying, name)
greeting(saying = 'I'll be back', name = "Arnold")
```


---

### Function Practices
Fun With Functions - 5 min
Function Arguments - 2 min
Using Lambdas - 2 min
Add Binary Leet Code Challenge - 5 min
Merge Helper - Challenge - 20 min


---

## Lists

---


Lists are mutable, ordered collections (like arrays in JavaScript). Use square brackets to make lists.

```python=
empty = []
print(empty)   # []
```

Values are separated by commas.
```python=
fruits = ["banana", "apple", "kiwi"]
print(fruits)  # ["banana", "apple", "kiwi"]
```


---

### Indexing with lists

Indexing with lists uses the same syntax as indexing with strings:

- Single index: `list_name[single_index]`
- Index range: `list_name[start:stop:step]`


---

### List Practices
Explore The List - 5 min
Return First Element Of A List - 2 min
Sum The Elements Of A List - 5 min
First And Last Entries - 1 min
First Last List - 5 min
Insertion Sort - 20 min
All Occurrences Of A Value In A List - 5 min
Find Target Indices Leet Code - 10 min
Matrix Diagonal Sum - Leet Code Challenge - 10 min


---
