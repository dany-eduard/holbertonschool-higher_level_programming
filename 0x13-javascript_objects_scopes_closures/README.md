# 0x13. JavaScript - Objects, Scopes and Closures

## Resources

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Basics" title="JavaScript object basics" target="_blank">JavaScript object basics</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object-oriented_JS" title="Object-oriented JavaScript" target="_blank">Object-oriented JavaScript</a> (<em><strong>read all examples!</strong></em>)</li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes" title="Class - ES6" target="_blank">Class - ES6</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/super" title="super - ES6" target="_blank">super - ES6</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/extends" title="extends - ES6" target="_blank">extends - ES6</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Object_prototypes" title="Object prototypes" target="_blank">Object prototypes</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance" title="Inheritance in JavaScript" target="_blank">Inheritance in JavaScript</a> </li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures" title="Closures" target="_blank">Closures</a> </li>
<li><a href="https://alistapart.com/article/getoutbindingsituations/" title="this/self" target="_blank">this/self</a> </li>
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

### 0. Rectangle #0

Write an empty class `Rectangle` that defines a rectangle:

You must use the `class` notation for defining your class

- File: **[0-rectangle.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/0-rectangle.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);

guillaume@ubuntu:~/0x13$ ./0-main.js
Rectangle {}
[Function: Rectangle]
guillaume@ubuntu:~/0x13$
```

---

### 1. Rectangle #1

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments w and h
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- File: **[1-rectangle.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/1-rectangle.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

guillaume@ubuntu:~/0x13$ ./1-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
guillaume@ubuntu:~/0x13$
```

---

### 2. Rectangle #2

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If w or h is equal to 0 or not a positive integer, create an empty object
- File: **[2-rectangle.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/2-rectangle.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 2-main.js
#!/usr/bin/node
const Rectangle = require('./2-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

const r4 = new Rectangle(2, 0);
console.log(r4);
console.log(r4.width);
console.log(r4.height);

guillaume@ubuntu:~/0x13$ ./2-main.js
Rectangle { width: 2, height: 3 }
2
3
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
Rectangle {}
undefined
undefined
guillaume@ubuntu:~/0x13$
```

---

### 3. Rectangle #3

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character X
- File: **[3-rectangle.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/3-rectangle.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 3-main.js
#!/usr/bin/node
const Rectangle = require('./3-rectangle');

const r1 = new Rectangle(2, 3);
r1.print();

const r2 = new Rectangle(10, 5);
r2.print();

guillaume@ubuntu:~/0x13$ ./3-main.js
XX
XX
XX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
guillaume@ubuntu:~/0x13$
```

---

### 4. Rectangle #4

Write a class `Rectangle` that defines a rectangle:

- You must use the `class` notation for defining your class
- The constructor must take 2 arguments: `w` and `h`
- Initialize the instance attribute `width` with the value of `w`
- Initialize the instance attribute `height` with the value of `h`
- If `w` or `h` is equal to 0 or not a positive integer, create an empty object
- Create an instance method called `print()` that prints the rectangle using the character `X`
- Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
- Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2
- File: **[4-rectangle.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/4-rectangle.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 4-main.js
#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

guillaume@ubuntu:~/0x13$ ./4-main.js
Normal:
XX
XX
XX
Double:
XXXX
XXXX
XXXX
XXXX
XXXX
XXXX
Rotate:
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/0x13$
```

---

### 5. Square #0

Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:

- You must use the `class` notation for defining your class and `extends`
- The constructor must take 1 argument: `size`
- The constructor of `Rectangle` must be called (by using `super()`)
- File: **[5-square.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/5-square.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 5-main.js
#!/usr/bin/node
const Square = require('./5-square');

const s1 = new Square(4);
s1.print();
s1.double();
s1.print();

guillaume@ubuntu:~/0x13$ ./5-main.js
XXXX
XXXX
XXXX
XXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
XXXXXXXX
guillaume@ubuntu:~/0x13$
```

---

### 6. Square #1

Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:

- You must use the `class` notation for defining your class and `extends`
- Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
  - If `c` is `undefined`, use the character `X`
- File: **[6-square.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/6-square.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 6-main.js
#!/usr/bin/node
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

guillaume@ubuntu:~/0x13$ ./6-main.js
XXXX
XXXX
XXXX
XXXX
CCCC
CCCC
CCCC
CCCC
guillaume@ubuntu:~/0x13$
```

---

### 7. Occurrences

Write a function that returns the number of occurrences in a list:

- Prototype: `exports.nbOccurences = function (list, searchElement)`
- File: **[7-occurrences.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/7-occurrences.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 7-main.js
#!/usr/bin/node
const nbOccurences = require('./7-occurrences').nbOccurences;

console.log(nbOccurences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurences(["H", 12, "c", "H", "Holberton", 8], "H"));

guillaume@ubuntu:~/0x13$ ./7-main.js
1
4
2
guillaume@ubuntu:~/0x13$
```

---

### 8. Esrever

Write a function that returns the reversed version of a list:

- Prototype: `exports.esrever = function (list)`
- You are not allow to use the built-in method `reverse`
- File: **[8-esrever.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/8-esrever.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 8-main.js
#!/usr/bin/node
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["Holberton", 89, { id: 12 }, "String"]));

guillaume@ubuntu:~/0x13$ ./8-main.js
[ 5, 4, 3, 2, 1 ]
[ 'String', { id: 12 }, 89, 'Holberton' ]
guillaume@ubuntu:~/0x13$
```

---

### 9. Log me

Write a function that prints the number of arguments already printed and the new argument value. (see example below)

- Prototype: `exports.logMe = function (item)`
- Output format: `<number arguments already printed>: <current argument value>`
- File: **[9-logme.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/9-logme.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Holberton");
logMe("School");

guillaume@ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Holberton
2: School
guillaume@ubuntu:~/0x13$
```

---

### 10. Number conversion

Write a function that converts a number from base 10 to another base passed as argument:

- Prototype: `exports.converter = function (base)`
- You are not allowed to import any file
- You are not allowed to declare any new variable (`var`, `let`, etc..)
- File: **[10-converter.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/10-converter.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 10-main.js
#!/usr/bin/node
const converter = require('./10-converter').converter;

let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

guillaume@ubuntu:~/0x13$ ./10-main.js
2
12
89
2
c
59
guillaume@ubuntu:~/0x13$
```

---

### 11. Factor index

Write a script that imports an array and computes a new array.

- Your script must import `list` from the file `100-data.js`
- You must use a `map`. [Tips](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map?v=control)
- A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
- Print both the initial list and the new list
- File: **[100-map.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/100-map.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 100-data.js
#!/usr/bin/node
exports.list = [1, 2, 3, 4, 5];
guillaume@ubuntu:~/0x13$ ./100-map.js
[ 1, 2, 3, 4, 5 ]
[ 0, 2, 6, 12, 20 ]
guillaume@ubuntu:~/0x13$
```

---

### 12. Sorted occurences

Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

- Your script must import `dict` from the file `101-data.js`
- In the new dictionary:
  - A key is a number of occurrences
  - A value is the list of user ids
- Print the new dictionary at the end
- File: **[101-sorted.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/101-sorted.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat 101-data.js
#!/usr/bin/node
exports.dict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};
guillaume@ubuntu:~/0x13$ ./101-sorted.js
{ '1': [ '89', '91', '93' ], '2': [ '90', '94' ], '3': [ '92' ] }
guillaume@ubuntu:~/0x13$
```

---

### 13. Concat files

Write a script that concats 2 files.

- The first argument is the file path of the first source file
- The second argument is the file path of the second source file
- The third argument is the file path of the destination
- File: **[102-concat.js](https://github.com/dany-eduard/holbertonschool-higher_level_programming/blob/main/0x13-javascript_objects_scopes_closures/102-concat.js)**

**_Example:_**

```js
guillaume@ubuntu:~/0x13$ cat fileA
C is fun!
guillaume@ubuntu:~/0x13$ cat fileB
Python is Cool!!!
guillaume@ubuntu:~/0x13$ ./102-concat.js fileA fileB fileC
guillaume@ubuntu:~/0x13$ cat fileC
C is fun!
Python is Cool!!!
guillaume@ubuntu:~/0x13$
```

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
