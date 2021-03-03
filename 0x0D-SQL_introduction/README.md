# 0x0D. SQL - Introduction

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" alt="" style="" /></p>

<div>
<h2>Resources</h2>

<ul>
<li><a href="https://www.youtube.com/watch?v=FR4QIeZaPeM" title="What is Database &amp; SQL?" target="_blank">What is Database &amp; SQL?</a> </li>
<li><a href="https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial" title="A Basic MySQL Tutorial" target="_blank">A Basic MySQL Tutorial</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php" title="Basic SQL statements: DDL and DML" target="_blank">Basic SQL statements: DDL and DML</a> (<em>no need to read the chapter &ldquo;Privileges&rdquo;</em>)</li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php" title="Basic queries: SQL and RA" target="_blank">Basic queries: SQL and RA</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php" title="SQL technique: functions" target="_blank">SQL technique: functions</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
<li><a href="https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458" title="What makes the big difference between a backtick and an apostrophe?" target="_blank">What makes the big difference between a backtick and an apostrophe?</a> </li>
<li><a href="https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdfb" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html" title="MySQL 5.7 SQL Statement Syntax" target="_blank">MySQL 5.7 SQL Statement Syntax</a> </li>
</div>

<div>
<h2>Requirements</h2>

<ul>
<li>All your files will be executed on Ubuntu 14.04 LTS using <code>MySQL 5.7</code> (version 5.7.8-rc)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>

<h2>More Info</h2>

<h3>Comments for your SQL file:</h3>

<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>

<h3>Install MySQL 5.7 on Ubuntu 14.04 LTS</h3>

<pre><code>$ echo &#39;deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr&#39; | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$
</code></pre>

<p><strong>Don&rsquo;t forget your <code>root</code> password</strong></p>

<p>Connect to your MySQL server:</p>

<pre><code>$ mysql -hlocalhost -uroot -p
Password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &#39;help;&#39; or &#39;\h&#39; for help. Type &#39;\c&#39; to clear the current input statement.

mysql&gt; 
mysql&gt; quit
Bye
$
</code></pre>
</div>

## Tasks

### 0. List databases

Write a script that lists all databases of your MySQL server.

- File: **[0-list_databases.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/0-list_databases.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$
```

---

### 1. Create a database

Write a script that creates the database `hbtn_0c_0` in your MySQL server.

If the database `hbtn_0c_0` already exists, your script should not fail
You are not allowed to use the `SELECT` or `SHOW` statements

- File: **[1-create_database_if_missing.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/1-create_database_if_missing.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$
```

---

### 2. Delete a database

Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

- If the database `hbtn_0c_0` doesn’t exist, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements
- File: **[2-remove_database.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/2-remove_database.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password:
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$
```

---

### 3. List tables

Write a script that lists all the tables of a database in your MySQL server.

The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

- File: **[3-list_tables.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/3-list_tables.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password:
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
guillaume@ubuntu:~/$
```

---

### 4. First table

Write a script that creates a table called `first_table` in the current database in your MySQL server.

- `first_table` description:
     - `id` INT
     - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `first_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` or `SHOW` statements
- File: **[4-first_table.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/4-first_table.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$
```

---

### 5. Full description

Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements

- File: **[5-full_table.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/5-full_table.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$
```

---

### 6. List all in table

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

- All fields should be printed
- The database name will be passed as an argument of the mysql command
- File: **[6-list_values.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/6-list_values.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
```

---

### 7. First add

Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

- New row:
     - `id` = 89
     - `name` = Holberton School
- The database name will be passed as an argument of the `mysql` command
- File: **[7-insert_value.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/7-insert_value.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Holberton School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
id  name
89  Holberton School
89  Holberton School
89  Holberton School
guillaume@ubuntu:~/$
```

---

### 8. Count 89

Write a script that displays the number of records with `id = 89` in the table `first_table` of the database hbtn_0c_0 in your MySQL server.

- The database name will be passed as an argument of the `mysql` command
- File: **[8-count_89.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/8-count_89.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password:
3
guillaume@ubuntu:~/$
```

---

### 9. Full creation

Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

- `second_table` description:
     - `id` INT
     - `name` VARCHAR(256)
     - `score` INT
- The database name will be passed as an argument to the `mysql` command
- If the table `second_table` already exists, your script should not fail
- You are not allowed to use the `SELECT` and `SHOW` statements
- Your script should create these records:
     - `id` = 1, `name` = “John”, `score` = 10
     - `id` = 2, `name` = “Alex”, `score` = 3
     - `id` = 3, `name` = “Bob”, `score` = 14
     - `id` = 4, `name` = “George”, `score` = 8
- File: **[9-full_creation.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/9-full_creation.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$
```

---

### 10. List by best

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command
- File: **[10-top_score.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/10-top_score.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$
```

---

### 11. Select the best

Write a script that lists all records with a `score >= 10` in the table `second_table` of the database hbtn_0c_0 in your MySQL server.

- Results should display both the score and the name (in this order)
- Records should be ordered by score (top first)
- The database name will be passed as an argument of the `mysql` command
- File: **[11-best_score.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/11-best_score.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
14  Bob
10  John
guillaume@ubuntu:~/$
```

---

### 12. Cheating is bad

Write a script that updates the score of Bob to `10` in the table `second_table`.

- You are not allowed to use Bob’s id value, only the `name` field
- The database name will be passed as an argument of the `mysql` command
- File: **[12-no_cheating.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/12-no_cheating.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$
```

---

### 13. Score too low

Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- The database name will be passed as an argument of the mysql command
- File: **[13-change_class.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/13-change_class.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$
```

---

### 14. Average

Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- The result column name should be `average`
- The database name will be passed as an argument of the `mysql` command
- File: **[14-average.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/14-average.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
average
9.3333
guillaume@ubuntu:~/$
```

---

### 15. Number by score

Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- The result should display:
     - the `score`
     - the number of records for this `score` with the label `number`
- The list should be sorted by the number of records (descending)
- The database name will be passed as an argument to the `mysql` command
- File: **[15-groups.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/15-groups.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   number
10  2
8   1
guillaume@ubuntu:~/$
```

---

### 16. Say my name

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

- Don’t list rows without a `name` value
- Results should display the score and the name (in this order)
- Records should be listed by descending score
- The database name will be passed as an argument to the `mysql` command

In this example, new data have been added to the table `second_table`.

- File: **[16-no_link.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/16-no_link.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$
```

---

### 17. Go to UTF8

Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

You need to convert all of the following to `UTF8`:

- Database `hbtn_0c_0`
- Table `first_table`
- Field name in `first_table`
- File: **[100-move_to_utf8.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/100-move_to_utf8.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$
```

---

### 18. Temperatures #0

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

- File: **[101-avg_temperatures.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/101-avg_temperatures.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$
```

---

### 19. Temperatures #1

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

- File: **[102-top_city.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/102-top_city.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
guillaume@ubuntu:~/$
```

---

### 20. Temperatures #2

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)

Write a script that displays the max temperature of each state (ordered by State name).

- File: **[103-max_state.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0D-SQL_introduction/103-max_state.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password:
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$
```

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
