# 0x12. JavaScript - Warm up

JavaScript is used for many things. At Holberton School, you will use JavaScript for 2 reasons:

- Scripting (same as we did with Python)
- Web front-end

For the moment, and for learning all basic concepts of this language, we will do some scripting. After, we will make our AirBnB project dynamic by using Javascript and JQuery.

## Resources

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics" title="Writing JavaScript Code" target="_blank">Writing JavaScript Code</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables" title="Variables" target="_blank">Variables</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures" title="Data Types" target="_blank">Data Types</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics" title="Operators" target="_blank">Operators</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence" title="Operator Precedence" target="_blank">Operator Precedence</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling" title="Controlling Program Flow" target="_blank">Controlling Program Flow</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions" title="Functions" target="_blank">Functions</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects" title="Objects and Arrays" target="_blank">Objects and Arrays</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects" title="Intrinsic Objects" target="_blank">Intrinsic Objects</a> </li>
<li><a href="http://darrenderidder.github.io/talks/ModulePatterns/#/" title="Module patterns" target="_blank">Module patterns</a> </li>
<li><a href="https://www.youtube.com/watch?v=sjyJBL5fkp8" title="var, let and const" target="_blank">var, let and const</a> </li>
<li><a href="https://www.youtube.com/watch?v=vZBCTc9zHtI" title="JavaScript Tutorial" target="_blank">JavaScript Tutorial</a> </li>
<li><a href="https://github.com/mbeaudru/modern-js-cheatsheet" title="Modern JS" target="_blank">Modern JS</a> </li>
</ul>

## Requirements

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS using <code>node</code> (version 10.14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant (version 14.x.x). <a href="https://standardjs.com/rules.html" title="Rules of Standard" target="_blank">Rules of Standard</a> + <a href="https://github.com/standard/semistandard" title="semicolons on top" target="_blank">semicolons on top</a>. Also as reference: <a href="https://github.com/airbnb/javascript" title="AirBnB style" target="_blank">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

## More Info

### Install Node 10

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

[Documentation](https://github.com/standard/semistandard)

```
$ sudo npm install semistandard --global
```

## Tasks

### 0. First constant, first print

Write a script that prints “JavaScript is amazing”:

- You must create a constant variable called `myVar` with the value “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- File: **[0-javascript_is_amazing.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/0-javascript_is_amazing.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js
JavaScript is amazing
guillaume@ubuntu:~/0x12$
guillaume@ubuntu:~/0x12$ semistandard ./0-javascript_is_amazing.js
guillaume@ubuntu:~/0x12$
```

---

### 1. 3 languages

Write a script that prints 3 lines:

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- File: **[1-multi_languages.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/1-multi_languages.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./1-multi_languages.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$
```

---

### 2. Arguments

Write a script that prints a message depending of the number of arguments passed:

- If no arguments are passed to the script, print “No argument”
- If only one argument is passed to the script, print “Argument found”
- Otherwise, print “Arguments found”
- You must use `console.log(...)` to print all output
- You are not allowed to use var
- File: **[2-arguments.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/2-arguments.js)**

Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv)

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./2-arguments.js
No argument
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton
Argument found
guillaume@ubuntu:~/0x12$ ./2-arguments.js Holberton School
Arguments found
guillaume@ubuntu:~/0x12$
```

---

### 3. Value of my argument

Write a script that prints the first argument passed to it:

- If no arguments are passed to the script, print “No argument”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `length`
- File: **[3-value_argument.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/3-value_argument.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./3-value_argument.js
No argument
guillaume@ubuntu:~/0x12$ ./3-value_argument.js Holberton
Holberton
guillaume@ubuntu:~/0x12$
```

---

### 4. Create a sentence

Write a script that prints two arguments passed to it, in the following format: “ is ”

- You must use console.log(...) to print all output
- You are not allowed to use var
- File: **[4-concat.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/4-concat.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/0x12$ ./4-concat.js c
c is undefined
guillaume@ubuntu:~/0x12$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/0x12$
```

---

### 5. An Integer

Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

- If the argument can’t be converted to an integer, print “Not a number”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use `try/catch`
- File: **[5-to_integer.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/5-to_integer.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./5-to_integer.js
Not a number
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/0x12$ ./5-to_integer.js Holberton
Not a number
guillaume@ubuntu:~/0x12$
```

---

### 6. Loop to languages

Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

- The first line: “C is fun”
- The second line: “Python is cool”
- The third line: “JavaScript is amazing”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You are not allowed to use any `if/else` statement
- You can use only one `console.log`
- You must use a loop (`while`, `for`, etc.)
- File: **[6-multi_languages_loop.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/6-multi_languages_loop.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/0x12$
```

---

### 7. I love C

Write a script that prints `x` times “C is fun”

- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print “Missing number of occurrences”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (`while`, `for`, etc.)
- File: **[7-multi_c.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/7-multi_c.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$
```

---

### 7. I love C

Write a script that prints `x` times “C is fun”

- Where `x` is the first argument of the script
- If the first argument can’t be converted to an integer, print “Missing number of occurrences”
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You can use only two `console.log`
- You must use a loop (`while`, `for`, etc.)
- File: **[7-multi_c.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/7-multi_c.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$ ./7-multi_c.js
Missing number of occurrences
guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
guillaume@ubuntu:~/0x12$
```

---

### 8. Square

Write a script that prints a square

- The first argument is the size of the square
- If the first argument can’t be converted to an integer, print “Missing size”
- You must use the character `X` to print the square
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- You must use a loop (`while`, `for`, etc.)
- File: **[8-square.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/8-square.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./8-square.js
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js Holberton
Missing size
guillaume@ubuntu:~/0x12$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/0x12$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x12$ ./8-square.js -3
guillaume@ubuntu:~/0x12$
```

---

### 9. Add

Write a script that prints the addition of 2 integers

- The first argument is the first integer
- The second argument is the second integer
- You have to define a function with this prototype: `function add(a, b)`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- File: **[9-add.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/9-add.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./9-add.js
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1
NaN
guillaume@ubuntu:~/0x12$ ./9-add.js 1 7
8
guillaume@ubuntu:~/0x12$ ./9-add.js 13 89
102
guillaume@ubuntu:~/0x12$
```

---

### 10. Factorial

Write a script that computes and prints a factorial

- The first argument is integer (argument can be cast as integer) used for computing the factorial
- Factorial of `NaN` is `1`
- You must do it recursively
- You must use a function
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- File: **[10-factorial.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/10-factorial.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./10-factorial.js
1
guillaume@ubuntu:~/0x12$ ./10-factorial.js 3
6
guillaume@ubuntu:~/0x12$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/0x12$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/0x12$
```

---

### 11. Second biggest!

Write a script that searches the second biggest integer in the list of arguments.

- You can assume all arguments can be converted to integer
- If no argument passed, print `0`
- If the number of arguments is `1`, print `0`
- You must use `console.log(...)` to print all output
- You are not allowed to use `var`
- File: **[11-second_biggest.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/11-second_biggest.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/0x12$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/0x12$
```

---

### 12. Object

Update this script to replace the value `12` with `89`:

You are not allowed to use `var`

- File: **[12-object.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/12-object.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/0x12$
```

---

### 13. Add file

Write a function that returns the addition of 2 integers.

- The function must be visible from outside
- The name of the function must be `add`
- You are not allowed to use `var`
- File: **[13-add.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/13-add.js)**

[Tip](http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/0x12$ ./13-main.js
8
guillaume@ubuntu:~/0x12$
```

---

### 14. Const or not const

Write a file that modifies the value of `myVar` to `333`

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/0x12$ ./100-main.js
333
guillaume@ubuntu:~/0x12$
```

Do you get it? Tweet! Post! Talk about it!

Hint: Scope

**This exercise doesn’t pass** **`semistandard`** so don’t worry about it.

- File: **[0x12-javascript-warm_up](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/0x12-javascript-warm_up)**

---

### 15. Call me Moby

Write a function that executes x times a function.

- The function must be visible from outside
- Prototype: `function (x, theFunction)`
- You are not allowed to use `var`
- File: **[101-call_me_moby.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/101-call_me_moby.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/0x12$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/0x12$
```

---

### 16. Add me maybe

Write a function that increments and calls a function.

- The function must be visible from outside
- Prototype: `function (number, theFunction)`
- You are not allowed to use `var`
- File: **[102-add_me_maybe.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/102-add_me_maybe.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ cat 102-main.js
#!/usr/bin/node
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
guillaume@ubuntu:~/0x12$ ./102-main.js
New value: 5
guillaume@ubuntu:~/0x12$
```

---

### 17. Increment object

Update this script by adding a new function `incr` that increments the integer value.

- You are not allowed to use `var`
- File: **[103-object_fct.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x12-javascript-warm_up/103-object_fct.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x12$ cat 103-object_fct.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);

guillaume@ubuntu:~/0x12$ ./103-object_fct.js
{ type: 'object', value: 12 }
{ type: 'object', value: 13, incr: [Function] }
{ type: 'object', value: 14, incr: [Function] }
{ type: 'object', value: 15, incr: [Function] }
guillaume@ubuntu:~/0x12$
```

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
