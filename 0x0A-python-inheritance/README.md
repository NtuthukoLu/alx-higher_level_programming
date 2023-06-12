# :shell: 0x0A - Python, Inheritance & Multiple Inheritance :shell:

I will be working with inheritance in Python in this project. Previously I have only worked with single inheritance-based languages like C#. Working with multiple inheritance will be interesting.

## :running: Getting Started

* [Ubuntu 20.04 LTS](http://releases.ubuntu.com/20.04/) - Operating system reqd.

* [Python 3.4](https://www.python.org/download/releases/3.4.0/) - Python Version Used

## :warning: Prerequisites

* Must have `git` installed

* Must have repository cloned

* Must have `python3` installed

```
$ sudo apt-get install git
```

```
$ sudo apt-get install python3
```
## TASKS:
### 0. Lookup - 0-lookup.py
Function that returns the list of available attributes and methods of an object.

### 1. My list - 1-my_list.py, tests/1-my_list.txt
Class `MyList` that inherits from `list`, with a public instance method that prints the list in sorted (ascending) order.

### 2. Exact same object - 2-is_same_class.py
Function that returns `True` if the object is exactly an instance of the specified class.

### 3. Same class or inherit from - 3-is_kind_of_class.py
Function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

### 4. Only sub class of - 4-inherits_from.py
Function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

### 5. Geometry module - 5-base_geometry.py
Empty class `BaseGeometry`.

### 6. Improve Geometry - 6-base_geometry.py
Class `BaseGeometry` with a public instance method that raises an exception with the message `area() is not implemented`.

### 7. Integer validator - 7-base_geometry.py, tests/7-base_geometry.txt
Class `BaseGeometry` with the same not-implemented method `area()` and a public instance method that validates `value`.

### 8. Rectangle - 8-rectangle.py
Class `Rectangle` that inherits from `BaseGeometry`, with instantiation for width and height.

### 9. Full rectangle - 9-rectangle.py
Class `Rectangle` that inherits from `BaseGeometry` with an implemented `area()` and `__str__` method.

### 10. Square #1 - 10-square.py
Class `Square` that inherits from `Rectangle`, with an implemented `area()` method.

### 11. Square #2 - 11-square.py
Class `Square` that inherits from `Rectangle` with `__str__` method implemented.

## :blue_book: Authors
* **Ntuthuko Zimu** - [@NtuthukoLu](https://github.com/NtuthukoLu)

