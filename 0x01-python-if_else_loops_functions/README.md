# 0x01. Python - if/else, loops, functions

![Python Loop for](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png)

Besides the while statement, Python knows the usual control flow statements known from other languages, with some twists.

## Resources
* [More Control Flow Tools](https://docs.python.org/3.4/tutorial/controlflow.html)(Read until “4.6. Defining Functions” included)
* [Myths about Indentation](https://files.meetup.com/1544869/Python%20Indentation%20Myths.pdf)
* [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
* [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Learn to Program 2 : Looping - YouTube](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

**Man or Help**
* ```python3```

## Requirements
### Python Scripts
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using ```python3``` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly ```#!/usr/bin/python3```
* Your code should use the ```PEP 8``` style (version ```1.7.*```)
* All your files must be executable

### C Scripts
* All your files will be compiled on Ubuntu 14.04 LTS
* Your programs and functions will be compiled with ```gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic```
* All your files should end with a new line
* Your code should use the ```Betty``` style. It will be checked using [betty-style](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc-pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)

## Tasks
### 0. Positive anything is better than negative nothing
_This program will assign a random signed number to the variable_ ```number``` _each time it is executed. Complete the [source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py) in order to print whether the number stored in the variable_ ```number``` _is positive or negative._
* The variable ```number``` will store a different value every time you will run this program
* You don’t have to understand what ```import```, ```random.``` ```randint``` do. Please do not touch this code
* The output of the program should be:
    * The number, followed by
        * if the number is greater than 0: is positive
        * if the number is 0: is zero
        * if the number is less than 0: is negative
    * followed by a new line
* File: **[0-positive_or_negative.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/0-positive_or_negative.py)**  
  
***Example:***
```sh
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
dany@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
dany@ubuntu:~/0x01$ 
```  
  
________________________________________________
### 1. The last digit
_This program will assign a random signed number to the variable_ ```number``` _each time it is executed. Complete the [source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py) in order to print the last digit of the number stored in the variable_ ```number```.
* The variable ```number``` will store a different value every time you will run this program
* You don’t have to understand what ```import```, ```random.randint``` do. Please do not touch this code. This line should not change: ```number = random.randint(-10000, 10000)```
* The output of the program should be:
    * The string ```Last digit of```, followed by
    * the number, followed by
    * the string ```is```, followed by the last digit of ```number```, followed by
        * if the last digit is greater than 5: the string ```and is greater than 5```
        * if the last digit is 0: the string ```and is 0```
        * if the last digit is less than 6 and not 0: the string ```and is less than 6 and not 0```
    * followed by a new line
* File: **[1-last_digit.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/1-last_digit.py)**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
dany@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
dany@ubuntu:~/0x01$ 
```  
  
________________________________________________
### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
_Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line._
* You can only use one ```print``` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module
* File: **[2-print_alphabet.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/2-print_alphabet.py)**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzdany@ubuntu:~/0x01$
```  
  
________________________________________________
### 3. When I was having that alphabet soup, I never thought that it would pay off
_Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line._
* Print all the letters except ```q``` and ```e```
* You can only use one ```print``` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module
* File: **[3-print_alphabt.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/3-print_alphabt.py)**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzdany@ubuntu:~/0x01$
```  
  
________________________________________________
### 4. Hexadecimal printing
_Write a program that prints all numbers from ```0``` to ```98``` in decimal and in hexadecimal (as in the following example)_
* You can only use one ```print``` function with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
* File: **[4-print_hexa.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/4-print_hexa.py)**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
dany@ubuntu:~/0x01$
```  
  
________________________________________________
### 5. 00...99 
_Write a program that prints numbers from ```0``` to ```99```._
* Numbers must be separated by ```,```, followed by a space
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 2 ```print``` functions with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
* File: **[5-print_comb2.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/5-print_comb2.py)**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
dany@ubuntu:~/0x01$ 
```  
  
________________________________________________
### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
_Write a program that prints all possible different combinations of two digits._
* Numbers must be separated by ```,```, followed by a space
* The two digits must be different
* ```01``` and ```10``` are considered the same combination of the two digits ```0``` and ```1```
* Print only the smallest combination of two digits
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 3 ```print``` functions with string format
* You can only use no more than 2 loops in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
* File: **[6-print_comb3.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/6-print_comb3.py)**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
dany@ubuntu:~/0x01$ 
```  
  
________________________________________________
### 7. islower
_Write a function that checks for lowercase character._
* Prototype: ```def islower(c):```
* Returns ```True``` if ```c``` is lowercase
* Returns ```False``` otherwise
* You are not allowed to import any module
* You are not allowed to use ```str.upper()``` and ```str.isupper()```
* [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
* File: **[]()**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

dany@ubuntu:~/0x01$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
dany@ubuntu:~/0x01$ 
```  
  
________________________________________________
### 8. To uppercase
_Write a function that prints a string in uppercase followed by a new line._
* Prototype: ```def uppercase(str):```
* You can only use no more than 2 ```print``` functions with string format
* You can only use one loop in your code
* You are not allowed to import any module
* You are not allowed to use ```str.upper()``` and ```str.isupper()```
* [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
* File: **[8-uppercase.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/8-uppercase.py)**  
  
***Example:***
```bash
dany@ubuntu:~/0x01$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("holberton")
uppercase("Holberton School 98 Battery street")

dany@ubuntu:~/0x01$ ./8-main.py
HOLBERTON
HOLBERTON SCHOOL 98 BATTERY STREET
dany@ubuntu:~/0x01$ 
```  
  
________________________________________________
### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
_Write a function that prints the last digit of a number._
* Prototype: ```def print_last_digit(number):```
* Returns the value of the last digit
* You are not allowed to import any module
* File: **[9-print_last_digit.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x01-python-if_else_loops_functions/9-print_last_digit.py)**  
  
***Example:***
```bash
guillaume@ubuntu:~/0x01$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

guillaume@ubuntu:~/0x01$ ./9-main.py
8044
guillaume@ubuntu:~/0x01$ 
```  
  
________________________________________________
### 10. a + b 
_Write a function that adds two integers and returns the result._
* Prototype: ``def add(a, b):``
* Returns the value of a + b
* You are not allowed to import any module
* File: **[]()**  
  
***Example:***
```bash

```  
  
________________________________________________
### 
_
* File: **[]()**  
  
***Example:***
```bash

```  
  
________________________________________________
### 
_
* File: **[]()**  
  
***Example:***
```bash

```  
  
________________________________________________
### 
_
* File: **[]()**  
  
***Example:***
```bash

```  
  
________________________________________________
### 
_
* File: **[]()**  
  
***Example:***
```bash

```  
  
________________________________________________
### 
_
* File: **[]()**  
  
***Example:***
```bash

```  
  
________________________________________________
### 
_
* File: **[]()**  
  
***Example:***
```bash

```  
  
________________________________________________
  
⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊