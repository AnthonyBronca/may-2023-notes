
## Importing

Terms

1. A __module__ is simply Python code in a separate file.
2. A __package__ is the path to a directory that contains modules, which is also a special type of module.
3. __init__.py is the default file for a package.
4. A __submodule__ is another file in a module's folder.
5. A __function__ is (obviously!) a function in a module.

Examples

1. `import <module>` - most basic
2. `import <package>.<subpackage>.<module>` - dot syntax
3. `from <package> import <module>` - one module in a package
4. `from <package> import <module>, <module>` - multiple modules or submodules in a package
5. `from . import <submodule>` - special case for module's __init__.py to get submodules in the same folder
6. `from <module> import <function>, <function>` - down to the function level
7. `from <package> import <module> as <altName>` - renaming to avoid confusion or conflict


## The Python Import System

---

To import code from a module, we use the `import` keyword. The import keyword will locate and initialize a module, and give you access to the specific names you have imported in the file.

There are no exports in Python! Anything we define in a module/file is automatically available for import.

---

### The `import` keyword
The Python standard library has a number of packages you can import without having to install them. Let's use the `random` package as an example (this would work the same with any package).

```python=
import random  # import everything from random
print(random.randint(0, 10))
```
Use the `as` keyword to alias package/object names.
```python=
import random as rand  # import everything, alias random as rand
print(rand.randint(0, 10))
```
You can also import specific objects from a package using the `from` keyword.

```python=
from random import randint, shuffle  # import multiple functions at the same time
print(randint(0, 10))
```

---


### Import Python code from another file
If two files are at the same level, import using the filename (without the `.py` extension).
```
project_folder
|  my_code.py
|  other_code.py
```

```python=
# inside my_code.py
import other_code
# import just a specific item
from other_code import my_function
```

If we need to specify a path to a file, we use dot notation:

```python=
# inside my_code.py
from folder.subfolder.filename import something
```

---

###  `__init__.py`

This file should go in any directory being imported. It will transform a plain old directory into a Python module/package. It can be completely empty, and often will be!

Upon import from a module/package,  its`__init__.py` file is implicitly executed, and all objects it defines are bound to the module's namespace ([documentation](https://docs.python.org/3/reference/import.html#regular-packages)).

---

### Import Practices (30 min)
Python Import Short Practice - 15 min


---
