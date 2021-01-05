# 0x06. Python - Classes and Objects

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type int which translates to saying that variables that store integers are variables which are instances (objects) of the int class.

Objects can store data using ordinary variables that belong to the object. Variables that belong to an object or class are referred to as fields. Objects can also have functionality by using functions that belong to a class. Such functions are called methods of the class. This terminology is important because it helps us to differentiate between functions and variables which are independent and those which belong to a class or object. Collectively, the fields and methods can be referred to as the attributes of that class.

Fields are of two types - they can belong to each instance/object of the class or they can belong to the class itself. They are called instance variables and class variables respectively.

## Resources

- [Object Oriented Programming - swaroopch](https://python.swaroopch.com/oop.html)
- [Object-Oriented Programming - Python Course](https://www.python-course.eu/python3_object_oriented_programming.php)
- [Propiedades vs. Getters y Setters - Python Course](https://www.python-course.eu/python3_properties.php)
- [Learn to Program 9 : Object Oriented Programming - YouTube](https://www.youtube.com/watch?v=1AGyBuVCTeE)
- [Python Classes and Objects || Python Tutorial || Learn Python Programming - YouTube](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Object Oriented Programming - YouTube](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Requirements

- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the `PEP 8` style (version `1.7.*`)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

## Tasks

### 0. My first square

_Write an empty class Square that defines a square:_

- You are not allowed to import any module
- File: **[0-square.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/0-square.py)**

**_Example:_**

```py
dany@ubuntu:~/0x06$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

dany@ubuntu:~/0x06$ ./0-main.py
<class '0-square.Square'>
{}
dany@ubuntu:~/0x06$
```

---

### 1. Square with size mandatory

_Write a class_` Square` _that defines a square by: (based on `0-square.py`)_

- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module
- File: **[1-square.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/1-square.py)**

**Why?**

Why `size` is private attribute?

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.

**_Example:_**

```py
dany@ubuntu:~/0x06$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

dany@ubuntu:~/0x06$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
dany@ubuntu:~/0x06$
```

---

### 2. Size validation

_Write a class_ `Square` _that defines a square by: (based on `1-square.py`)_

- Private instance attribute: `size`
- Instantiation with optional `size: def __init__(self, size=0):`
     - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
     - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are not allowed to import any module
- File: **[2-square.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/2-square.py)**

**_Example:_**

```py
dany@ubuntu:~/0x06$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

dany@ubuntu:~/0x06$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
dany@ubuntu:~/0x06$
```

---

### 3. Area of a square

_Write a class_ `Square` _that defines a square by: (based on `2-square.py`)_

- Private instance attribute: `size`
- Instantiation with optional `size: def __init__(self, size=0):`
     - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
     - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module
- File: **[3-square.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/3-square.py)**

**_Example:_**

```py
dany@ubuntu:~/0x06$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

dany@ubuntu:~/0x06$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
dany@ubuntu:~/0x06$
```

---

### 4. Access and update private attribute

_Write a class_ `Square` _that defines a square by: (based on `3-square.py`)_

- Private instance attribute: `size`:
     - property `def size(self):` to retrieve it
     - property setter `def size(self, value):` to set it:
          - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
          - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module
- File: **[4-square.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/4-square.py)**

**Why?**

Why a getter and setter?

Reminder: size is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

**_Example:_**

```py
dany@ubuntu:~/0x06$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

dany@ubuntu:~/0x06$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
dany@ubuntu:~/0x06$
```

---

### 5. Printing a square

_Write a class_ `Square` _that defines a square by: (based on `4-square.py`)_

- Private instance attribute: `size`:
     - property `def size(self):` to retrieve it
     - property setter `def size(self, value):` to set it:
          - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
          - if `size` is less than `0`, raise a `ValueError` exception with the `message size must be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
     - if `size` is equal to 0, print an empty line
- You are not allowed to import any module
- File: **[5-square.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/5-square.py)**

**_Example:_**

```py
dany@ubuntu:~/0x06$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

dany@ubuntu:~/0x06$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
dany@ubuntu:~/0x06$
```

---

### 6. Coordinates of a square

_Write a class_ `Square` _that defines a square by: (based on `5-square.py`)_

- Private instance attribute: `size`:
     - property `def size(self):` to retrieve it
     - property setter `def size(self, value):` to set it:
          - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
          - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position:`
     - property `def position(self):` to retrieve it
     - property setter `def position(self, value):` to set it:
          - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional `position: def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
     - if `size` is equal to 0, print an empty line
     - `position` should be use by using space - **Don’t fill lines by spaces** when `position[1] > 0`
- You are not allowed to import any module
- File: **[6-square.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes/6-square.py)**

**_Example:_**

```py
dany@ubuntu:~/0x06$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

dany@ubuntu:~/0x06$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
dany@ubuntu:~/0x06$
```

---
<!-- 
###

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes)**

**_Example:_**

```py

```

---

###

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes)**

**_Example:_**

```py

```

---

###

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes)**

**_Example:_**

```py

```

---

###

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x06-python-classes)**

**_Example:_**

```py

``` -->

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
