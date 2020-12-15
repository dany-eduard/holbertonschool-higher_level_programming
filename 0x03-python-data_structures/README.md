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
