# 0x09. Python - Everything is object

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```py
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>>
```

OK. But what about this?

```py
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>>
```

## Resources

- [9.10. Objects and values](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation (Only this chapter)](http://composingprograms.com/pages/24-mutable-data.html#sequence-objects)
- [9.12. Cloning lists](http://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](http://radar.oreilly.com/2014/10/python-tuples-immutable-but-potentially-changing.html)

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the `PEP 8` style (version `1.7.*`)
- All your files must be executable
- The length of your files will be tested using wc

### `.txt` Answer Files

- Only one line
- No Shebang
- All your files should end with a new line

## Tasks

### 0. Who am I?

What function would you use to print the type of an object?

Write the name of the function in the file, without `()`.

- File: **[0-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/0-answer.txt)**

---

### 1. Where are you?

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without `()`.

- File: **[1-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/1-answer.txt)**

---

### 2. Right count

In the following code, do a and b point to the same object? Answer with Yes or No.

- File: **[2-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/2-answer.txt)**

**_Example:_**

```py
>>> a = 89
>>> b = 100
```

---

### 3. Right count =

In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

- File: **[3-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/3-answer.txt)**

**_Example:_**

```py
>>> a = 89
>>> b = 89
```

---

### 4. Right count =

In the following code, do a and b point to the same object? Answer with Yes or No.

- File: **[4-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/4-answer.txt)**

**_Example:_**

```py
>>> a = 89
>>> b = a
```

---

### 5. Right count =+

In the following code, do a and b point to the same object? Answer with Yes or No.

- File: **[5-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/5-answer.txt)**

**_Example:_**

```py
>>> a = 89
>>> b = a + 1
```

---

### 6. Is equal

What do these 3 lines print?

- File: **[6-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/6-answer.txt)**

**_Example:_**

```py
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 == s2)
```

---

### 7. Is the same

What do these 3 lines print?

- File: **[7-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/7-answer.txt)**

**_Example:_**

```py
>>> s1 = "Holberton"
>>> s2 = s1
>>> print(s1 is s2)
```

---

### 8. Is really equal

What do these 3 lines print?

- File: **[8-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/8-answer.txt)**

**_Example:_**

```py
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 == s2)
```

---

### 9. Is really the same

What do these 3 lines print?

- File: **[9-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/9-answer.txt)**

**_Example:_**

```py
>>> s1 = "Holberton"
>>> s2 = "Holberton"
>>> print(s1 is s2)
```

---

### 10. And with a list, is it equal

What do these 3 lines print?

- File: **[10-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/10-answer.txt)**

**_Example:_**

```py
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 == l2)
```

---

### 11. And with a list, is it the same

What do these 3 lines print?

- File: **[11-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/11-answer.txt)**

**_Example:_**

```py
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> print(l1 is l2)
```

---

### 12. And with a list, is it really equal

What do these 3 lines print?

- File: **[12-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/12-answer.txt)**

**_Example:_**

```py
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

---

### 13. And with a list, is it really the same

What do these 3 lines print?

- File: **[13-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/13-answer.txt)**

**_Example:_**

```py
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

---

### 14. List append

What does this script print?

- File: **[14-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/14-answer.txt)**

**_Example:_**

```py
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

---

### 15. List add

What does this script print?

- File: **[15-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/15-answer.txt)**

**_Example:_**

```py
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

---

### 16. Integer incrementation

What does this script print?

- File: **[16-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/16-answer.txt)**

**_Example:_**

```py
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

---

### 17. List incrementation

What does this script print?

- File: **[17-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/17-answer.txt)**

**_Example:_**

```py
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

---

### 18. List assignation

What does this script print?

- File: **[18-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/18-answer.txt)**

**_Example:_**

```py
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

---

### 19. Copy a list object

Write a function `def copy_list(l):` that returns a copy of a list.

- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module
- File: **[19-copy_list.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/19-copy_list.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x09$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

guillaume@ubuntu:~/0x09$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
guillaume@ubuntu:~/0x09$ wc -l 19-copy_list.py
3 19-copy_list.py
guillaume@ubuntu:~/0x09$
```

---

### 20. Tuple or not?

Is `a` a tuple? Answer with Yes or No.

- File: **[20-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/20-answer.txt)**

**_Example:_**

```py
a = ()
```

---

### 21. Tuple or not?

Is `a` a tuple? Answer with Yes or No.

- File: **[21-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/21-answer.txt)**

**_Example:_**

```py
a = (1, 2)
```

---

### 22. Tuple or not?

Is `a` a tuple? Answer with Yes or No.

- File: **[22-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/22-answer.txt)**

**_Example:_**

```py
a = (1)
```

---

### 23. Tuple or not?

Is `a` a tuple? Answer with Yes or No.

- File: **[23-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/23-answer.txt)**

**_Example:_**

```py
a = (1, )
```

---

### 24. Who I am?

What does this script print?

- File: **[24-answer.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/24-answer.txt)**

**_Example:_**

```py
a = (1)
b = (1)
a is b
```

---

### 25. Tuple or not

What does this script print?

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/)**

**_Example:_**

```py
a = (1, 2)
b = (1, 2)
a is b
```

---

### 26. Empty is not empty

What does this script print?

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/)**

**_Example:_**

```py
a = ()
b = ()
a is b
```

---

### 27. Still the same?

Will the last line of this script print `139926795932424`? Answer with `Yes` or `No`.

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/)**

**_Example:_**

```py
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

---

### 28. Same or not?

Will the last line of this script print `139926795932424`? Answer with Yes or No.

- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/)**

**_Example:_**

```py
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

---

### 29. Python3: Mutable, Immutable... everything is object!

Write a blog post about everything you just learned / this project is covering. Your blog post should be articulated this way (one paragraph per item):

- introduction
- id and type
- mutable objects
- immutable objects
- why does it matter and how differently does Python treat mutable and immutable objects
- how arguments are passed to functions and what does that imply for mutable and immutable objects

Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

- My blog **[here]()**

---
### 30. #pythonic ***#advanced***
Write a function `magic_string()` that returns a string “Holberton” n times the number of the iteration (see code):

- Format: see example
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module
- File: **[](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/)**

**_Example:_**

```py
guillaume@ubuntu:~/0x09$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

guillaume@ubuntu:~/0x09$ ./100-main.py | cat -e
Holberton$
Holberton, Holberton$
Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton, Holberton$
guillaume@ubuntu:~/0x09$ wc -l 100-magic_string.py 
4 100-magic_string.py
guillaume@ubuntu:~/0x09$ 
```

---
### 31. Low memory cost ***#advanced***
Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.

- You are not allowed to import any module
- File: **[101-locked_class.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/101-locked_class.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x09$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/0x09$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
guillaume@ubuntu:~/0x09$ 
```

---
### 32. int 1/3 ***#advanced***
Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many int objects are created by the execution of the first line of the script? (`103-line1.txt`)
- How many int objects are created by the execution of the second line of the script (`103-line2.txt`)
- File: **[103-line1.txt,](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/103-line1.txt,)**, **[103-line2.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/103-line2.txt)**

**_Example:_**

```py
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
```

---
### 33. int 2/3 ***#advanced***
Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (`104-line1.txt`)
How many int objects are created by the execution of the second line of the script (`104-line2.txt`)
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (`104-line3.txt`)
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (`104-line4.txt`)
How many int objects are created by the execution of the last line of the script (`104-line5.txt`)
- File: **[104-line1.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line1.txt)**, **[104-line2.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line2.txt)**, **[104-line3.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line3.txt)**, **[104-line4.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line4.txt)**, **[104-line5.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/104-line5.txt)**, 

**_Example:_**

```py
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
```

---
### 34. int 3/3 ***#advanced***
Assuming we are using a CPython implementation of Python3 with default options/configuration:

- Before the execution of line 2 (`print("Love")`), how many int objects have been created and are still in memory? (`105-line1.txt`)
- Why? (optional blog post :))
Hint: NSMALLPOSINTS, NSMALLNEGINTS
- File: **[105-line1.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/105-line1.txt)**

**_Example:_**

```py
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
```

---
### 35. Clear strings
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

- How many string objects are created by the execution of the first line of the script? (`106-line1.txt`)
- How many string objects are created by the execution of the second line of the script (`106-line2.txt`)
- After the execution of line 3, is the string object pointed by `a` deleted? Answer with `Yes` or `No` (`106-line3.txt`)
- After the execution of line 4, is the string object pointed by `b` deleted? Answer with `Yes` or `No` (`106-line4.txt`)
- How many string objects are created by the execution of the last line of the script (`106-line5.txt`)
- File: **[106-line1.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line1.txt)**, **[106-line2.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line2.txt)**, **[106-line3.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line3.txt)**, **[106-line4.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line4.txt)**, **[106-line5.txt](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x09-python-everything_is_object/106-line5.txt)**, 

**_Example:_**

```py
guillaume@ubuntu:/python3$ cat string.py 
a = "HBTN"
b = "HBTN"
del a
del b
c = "HBTN"
guillaume@ubuntu:/python3$ 
```

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
