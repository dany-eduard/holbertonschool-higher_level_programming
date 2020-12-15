# 0x03. Python - Data Structures: Lists, Tuples

You can think of a data structure as a way of organizing and storing data such that we can access and modify it efficiently.

### List

A data structure that stores an ordered collection of items in Python is called a list. In other words, a list holds a sequence of items. You need to put all the items, separated by commas, in square brackets to let Python know that a list has been specified. The general syntax of a list is:

```py
some_list = [item 1, item 2, item 3,….., item n]
```

Any list can have any number of elements and of different data types. Moreover, a list can have another list as an element. Such a list is known as a nested list. For example:

```py
some_nested_list = [item 1, some_list, item 3,….., item n]
```

### Tuple

Similar to a list, the tuple is a built-in data structure in Python. However, it doesn’t support the same level of extensive functionality. The most important difference between a list and a tuple is mutability. Unlike lists, tuples are immutable i.e. they can’t be modified.

Typically, a tuple in the Python programming language is defined using parentheses with each item separated by commas. Though adding parentheses to the tuple is optional, its use is recommended to clearly define the end and start of the tuple. The general syntax of a tuple is:

```py
some_tuple = (item 1, item 2, item 3,….., item n)
```

## Resources

- [3.1.3. Lists](https://docs.python.org/3.4/tutorial/introduction.html#lists)
- [Data structures ](https://docs.python.org/3.4/tutorial/datastructures.html) (until `5.3. Tuples and Sequences` included)
- [Learn to Program 6 : Lists - YouTube](https://www.youtube.com/watch?v=A1HUzrvS-Pw)
- [Python Data Structures Explained in Detail - hackr.io](https://hackr.io/blog/python-data-structures#:~:text=Similar%20to%20a%20list%2C%20the,they%20can't%20be%20modified.)

## Requirements

### Python

- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the `PEP 8` style (version `1.7.*`)
- All your files must be executable

### C

- All your files will be compiled on Ubuntu 14.04 LTS
- Your programs and functions will be compiled with `gcc 4.8.4 using the flags -Wall -Werror -Wextra and -pedantic`
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc-pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
- The prototypes of all your functions should be included in your header file called `lists.h`

## Tasks

### 0. Print a list of integers

_Write a function that prints all integers of a list._

- Prototype: `def print_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
- File: **[0-print_list_integer.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/0-print_list_integer.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```

---

### 1. Secure access to an element in a list
_Write a function that retrieves an element from a list like in C._

- Prototype: `def element_at(my_list, idx):`
- If `idx` is negative, the function should return `None`
- If `idx` is out of range (> of number of element in `my_list`), the - function should return `None`
- You are not allowed to import any module
- You are not allowed to use `try/except`
- File: **[1-element_at.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/1-element_at.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```

---

### 2. Replace element
_Write a function that replaces an element of a list at a specific position (like in C)._

- Prototype: `def replace_in_list(my_list, idx, element):`
- If `idx` is negative, the function should not modify anything, and returns the original list
- If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use `try/except`
- File: **[2-replace_in_list.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/2-replace_in_list.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```

---

### 3. Print a list of integers... in reverse!
_Write a function that prints all integers of a list, in reverse order._

- Prototype: `def print_reversed_list_integer(my_list=[]):`
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
- File: **[3-print_reversed_list_integer.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/3-print_reversed_list_integer.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```

---

### 4. Replace in a copy
_Write a function that replaces an element in a list at a specific position without modifying the original list (like in C)._

- Prototype: `def new_in_list(my_list, idx, element):`
- If `idx` is negative, the function should return a copy of the original list
- If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
- You are not allowed to import any module
- You are not allowed to use `try/except`
- File: **[4-new_in_list.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/4-new_in_list.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```

---

### 5. Can you C me now?
_Write a function that removes all characters c and C from a string._

- Prototype: `def no_c(my_string):`
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use `str.replace()`
- File: **[5-no_c.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/5-no_c.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Holberton Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```

---

### 6. Lists of lists = Matrix
_Write a function that prints a matrix of integers._

- Prototype: `def print_matrix_integer(matrix=[[]]):`
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use `str.format()` to print integers
- File: **[6-print_matrix_integer.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/6-print_matrix_integer.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```

---

### 7. Tuples addition
_Write a function that adds 2 tuples._

- Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
- Returns a tuple with 2 integers:
    - The first element should be the addition of the first element of each argument
    - The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value `0` for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers
- File: **[7-add_tuple.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/7-add_tuple.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```

---

### 8. More returns!
_Write a function that returns a tuple with the length of a string and its first character._

- Prototype: `def multiple_returns(sentence):`
- If the sentence is empty, the first character should be equal to `None`
- You are not allowed to import any module
- File: **[8-multiple_returns.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/8-multiple_returns.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 32 - First character: A
guillaume@ubuntu:~/0x03$ 
```

---

### 9. Find the max
_Write a function that finds the biggest integer of a list._

- Prototype: `def max_integer(my_list=[]):`
- If the list is empty, return `None`
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin `max()`
- File: **[9-max_integer.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/9-max_integer.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 
```

---

### 10. Only by 2
_Write a function that finds all multiples of 2 in a list._

- Prototype: `def divisible_by_2(my_list=[]):`
- Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module
- File: **[10-divisible_by_2.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/10-divisible_by_2.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 
```

---

### 11. Delete at
_Write a function that deletes the item at a specific position in a list._

- Prototype: `def delete_at(my_list=[], idx=0):`
- If `idx` is negative or out of range, nothing change (returns the same list)
- You are not allowed to use `pop()`
- You are not allowed to import any module
- File: **[11-delete_at.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/11-delete_at.py)**

**_Example:_**

```py
guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
```

---

### 12. Switch
_Complete the source code in order to switch value of_ `a` _and_ `b`

- You can find the source code [here](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
- Your code should be inserted where the comment is (line 4)
- Your program should be exactly 5 lines long
- File: **[12-switch.py](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/12-switch.py)**

**_Example:_**

```py
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$ 
```

---

### 13. Linked list palindrome
_Technical interview preparation:_

- You are not allowed to google anything
- Whiteboard first
_Write a function in C that checks if a singly linked list is a palindrome._

- Prototype: `int is_palindrome(listint_t **head);`
- Return: 0 if it is not a palindrome, 1 if it is a palindrome
- An empty list is considered a palindrome
- File: **[13-is_palindrome.c](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/13-is_palindrome.c)**, **[lists.h](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/lists.h)**

```c++
carrie@ubuntu:0x03$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
carrie@ubuntu:0x03$
```

```c++
carrie@ubuntu:0x03$ cat linked_lists.c 
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
carrie@ubuntu:0x03$
```
```c++
carrie@ubuntu:0x03$ cat 13-main.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for Holberton School students.
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
carrie@ubuntu:0x03$
```

**_Example:_**

```c++
carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
carrie@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
carrie@ubuntu:0x03$
```

---

### 14. CPython #0: Python lists ***#advanced***
_CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language._
_Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use._

_Create a C function that prints some basic info about Python lists._

- Prototype: `void print_python_list_info(PyObject *p);`
- Format: see example
- Python version: 3.4
- Your shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
- OS: `Ubuntu 14.04 LTS`
- Start by reading:
    - listobject.h
    - object.h
    - [Common Object Structures](https://docs.python.org/3.4/c-api/structures.html)
    - [List Objects](https://docs.python.org/3.4/c-api/list.html)
- File: **[100-print_python_list_info.c](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x03-python-data_structures/100-print_python_list_info.c)**

**_Example:_**

```py
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
julien@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py 
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
julien@CPython:~/CPython$ 
```

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
