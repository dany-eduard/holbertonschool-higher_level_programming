# 0x0F. Python - Object-relational mapping

## Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module `MySQLdb` to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module `SQLAlchemy` (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

_Without ORM:_

```py
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

_With an ORM:_
```py
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.


## Resources

<ul>
<li><a href="https://www.fullstackpython.com/object-relational-mappers-orms.html" title="Object-relational mappers" target="_blank">Object-relational mappers</a> </li>
<li><a href="https://mysqlclient.readthedocs.io/" title="mysqlclient/MySQLdb documentation" target="_blank">mysqlclient/MySQLdb documentation</a> (<em>please don&rsquo;t pay attention to <code>_mysql</code></em>)</li>
<li><a href="https://www.mikusa.com/python-mysql-docs/index.html" title="MySQLdb tutorial" target="_blank">MySQLdb tutorial</a> </li>
<li><a href="https://docs.sqlalchemy.org/en/13/orm/tutorial.html" title="SQLAlchemy tutorial" target="_blank">SQLAlchemy tutorial</a> </li>
<li><a href="https://docs.sqlalchemy.org/en/13/" title="SQLAlchemy" target="_blank">SQLAlchemy</a> </li>
<li><a href="https://github.com/PyMySQL/mysqlclient" title="mysqlclient/MySQLdb" target="_blank">mysqlclient/MySQLdb</a> </li>
<li><a href="https://www.youtube.com/watch?v=woKYyhLCcnU" title="Introduction to SQLAlchemy" target="_blank">Introduction to SQLAlchemy</a> </li>
<li><a href="https://www.youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW" title="Flask SQLAlchemy" target="_blank">Flask SQLAlchemy</a> </li>
<li><a href="http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html" title="10 common stumbling blocks for SQLAlchemy newbies" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a> </li>
<li><a href="https://www.pythonsheets.com/notes/python-sqlalchemy.html" title="Python SQLAlchemy Cheatsheet" target="_blank">Python SQLAlchemy Cheatsheet</a> </li>
<li><a href="https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/" title="SQLAlchemy ORM Tutorial for Python Developers" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
<li><a href="https://overiq.com/sqlalchemy-101/" title="SQLAlchemy Tutorial" target="_blank">SQLAlchemy Tutorial</a></li>
</ul>


<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>Your files will be executed with <code>MySQLdb</code> version <code>1.3.x</code></li>
<li>Your files will be executed with <code>SQLAlchemy</code> version <code>1.2.x</code></li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (<code>version 1.7.*</code>)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>You are not allowed to use <code>execute</code> with sqlalchemy</li>
</ul>

<h2>More Info</h2>

<h3>Install <code>MySQLdb</code> module version <code>1.3.x</code></h3>

<p>For installing <code>MySQLdb</code>, you need to have <code>MySQL</code> installed: <a href="/rltoken/mqTU28SAIfz_-9w7rZipMw" title="How to install MySQL 5.7 in Ubuntu 14.04" target="_blank">How to install MySQL 5.7 in Ubuntu 14.04</a></p>

<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.__version__ 
&#39;1.3.10&#39;
</code></pre>

<h3>Install <code>SQLAlchemy</code> module version <code>1.2.x</code></h3>

<pre><code>$ sudo pip3 install SQLAlchemy==1.2.5
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
&#39;1.2.5&#39;
</code></pre>

<p>Also, you can have this warning message:</p>

<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, &quot;&#39;@@SESSION.GTID_EXECUTED&#39; is deprecated and will be re
moved in a future release.&quot;)                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>

<p>You can ignore it.</p>

</div>



## Tasks

### 0. Get all states
Write a script that lists all states from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments:` mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
- File: **[0-select_states.py](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/0-select_states.py)**

_*Example:*_

```bash
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

---
### 1. Filter states
Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

- Your script should take 3 arguments:` mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported
- File: **[1-filter_states.py](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/1-filter_states.py)**

_*Example:*_

```py
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$ 
```

---
### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa `where name matches the argument.

Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
You must use the module `MySQLdb` (`import MySQLdb`)
Your script should connect to a MySQL server running on `localhost` at port `3306`
You must use `format` to create the SQL query with the user input
Results must be sorted in ascending order by `states.id`
Results must be displayed as they are in the example below
Your code should not be executed when imported
- File: **[2-my_filter_states.py](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/2-my_filter_states.py)**

_*Example:*_

```py
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$ 
```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---
### 
- File: **[](https://github.com/dany-eduard/holberton-system_engineering-devops/tree/master/0x0F-python-object_relational_mapping/)**

_*Example:*_

```py

```

---


⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊