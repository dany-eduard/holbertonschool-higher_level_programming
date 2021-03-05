# 0x0E. SQL - More queries

<d>
<h2>Resources</h2>

<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql" title="How To Create a New User and Grant Permissions in MySQL" target="_blank">How To Create a New User and Grant Permissions in MySQL</a> </li>
<li><a href="https://www.mysqltutorial.org/mysql-grant.aspx" title="How To Use MySQL GRANT Statement To Grant Privileges To a User" target="_blank">How To Use MySQL GRANT Statement To Grant Privileges To a User</a> </li>
<li><a href="https://zetcode.com/mysql/constraints/" title="MySQL constraints" target="_blank">MySQL constraints</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php" title="Basic query operation: the join" target="_blank">Basic query operation: the join</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php" title="SQL technique: multiple joins and the distinct keyword" target="_blank">SQL technique: multiple joins and the distinct keyword</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php" title="SQL technique: join types" target="_blank">SQL technique: join types</a> </li>
<li><a href="https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php" title="SQL technique: union and minus" target="_blank">SQL technique: union and minus</a> </li>
<li><a href="https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a> </li>
<li><a href="https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html" title="The Seven Types of SQL Joins" target="_blank">The Seven Types of SQL Joins</a> </li>
<li><a href="https://www.youtube.com/watch?v=yPu6qV5byu4" title="MySQL Tutorial" target="_blank">MySQL Tutorial</a> </li>
<li><a href="https://www.sqlstyle.guide/" title="SQL Style Guide" target="_blank">SQL Style Guide</a> </li>
<li><a href="https://dev.mysql.com/doc/refman/5.7/en/sql-statements.html" title="MySQL 5.7 SQL Statement Syntax" target="_blank">MySQL 5.7 SQL Statement Syntax</a> </li>
</ul>

<p><strong>Extra resources around relational database model design:</strong></p>

<ul>
<li><a href="https://www.guru99.com/database-design.html" title="Design" target="_blank">Design</a></li>
<li><a href="https://www.guru99.com/database-normalization.html" title="Normalization" target="_blank">Normalization</a></li>
<li><a href="https://www.guru99.com/er-modeling.html" title="ER Modeling" target="_blank">ER Modeling</a></li>
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

<h3>How to import a SQL dump</h3>

<pre><code>$ echo &quot;CREATE DATABASE hbtn_0d_tvshows;&quot; | mysql -uroot -p
Enter password: 
$ curl &quot;https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql&quot; -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo &quot;SELECT * FROM tv_genres&quot; | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
</code></pre>

</div>

## Tasks

### 0. My privileges!

Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

- File: **[0-privileges.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/0-privileges.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_1' on host 'localhost'
guillaume@ubuntu:~/$
guillaume@ubuntu:~/$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$
```

---

### 1. Root user

Write a script that creates the MySQL server user `user_0d_1`.

- `user_0d_1` should have all privileges on your MySQL server
- The `user_0d_1` password should be set to user_0d_1_pwd
- If the user `user_0d_1` already exists, your script should not fail
- File: **[1-create_user.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/1-create_user.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
guillaume@ubuntu:~/$
```

---

### 2. Read user

Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.

- `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
- The `user_0d_2` password should be set to `user_0d_2_pwd`
- If the database `hbtn_0d_2` already exists, your script should not fail
- If the user `user_0d_2` already exists, your script should not fail
- File: **[2-create_read_user.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/2-create_read_user.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
Grants for user_0d_1@localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
Grants for user_0d_2@localhost
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost'
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost'
guillaume@ubuntu:~/$
```

---

### 3. Always a name

Write a script that creates the table force_name on your MySQL server.

- `force_name` description:
     - `id` INT
     - `name` VARCHAR(256) can’t be null
- The database name will be passed as an argument of the `mysql` command
- If the table `force_name` already exists, your script should not fail
- File: **[3-force_name.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/3-force_name.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
guillaume@ubuntu:~/$ echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Holberton School
guillaume@ubuntu:~/$
```

---

### 4. ID can't be null

Write a script that creates the table `id_not_null` on your MySQL server.

- `id_not_null` description:
     - `id` INT with the default value 1
     - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `id_not_null` already exists, your script should not fail
- File: **[4-never_empty.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/4-never_empty.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO id_not_null (name) VALUES ("Holberton");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Holberton School
1   Holberton
guillaume@ubuntu:~/$
```

---

### 5. Unique ID

Write a script that creates the table `unique_id` on your MySQL server.

- `unique_id` description:
     - `id` INT with the default value 1 and must be unique
     - `name` VARCHAR(256)
- The database name will be passed as an argument of the `mysql` command
- If the table `unique_id` already exists, your script should not fail
- File: **[5-unique_id.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/5-unique_id.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Holberton School
guillaume@ubuntu:~/$ echo 'INSERT INTO unique_id (id, name) VALUES (89, "Holberton");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'id'
guillaume@ubuntu:~/$ echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password:
id  name
89  Holberton School
guillaume@ubuntu:~/$
```

---

### 6. States table

Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.

- `states` description:
     - `id` INT unique, auto generated, can’t be null and is a primary key
     - `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `states` already exists, your script should not fail
- File: **[6-states.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/6-states.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   California
2   Arizona
3   Texas
guillaume@ubuntu:~/$
```

---

### 7. Cities table

Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.

- `cities` description:
     - `id` INT unique, auto generated, can’t be null and is a primary key
     - `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
     - `name` VARCHAR(256) can’t be null
- If the database `hbtn_0d_usa` already exists, your script should not fail
- If the table `cities` already exists, your script should not fail
- File: **[7-cities.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/7-cities.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password:
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$ echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  state_id    name
1   1   San Francisco
guillaume@ubuntu:~/$
```

---

### 8. Cities of California

Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.

- The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)
- Results must be sorted in ascending order by `cities.id`
- You are not allowed to use the `JOIN` keyword
- The database name will be passed as an argument of the `mysql` command
- File: **[8-cities_of_california_subquery.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/8-cities_of_california_subquery.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   San Francisco
2   San Jose
guillaume@ubuntu:~/$
```

---

### 9. Cities by States

Write a script that lists all cities contained in the database `hbtn_0d_usa`.

- Each record should display: `cities.id` - `cities.name` - `states.name`
- Results must be sorted in ascending order by `cities.id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[9-cities_by_state_join.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/9-cities_by_state_join.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name
1   California
2   Arizona
3   Texas
4   Utah
guillaume@ubuntu:~/$ echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  state_id    name
1   1   San Francisco
2   1   San Jose
4   2   Page
6   3   Paris
7   3   Houston
8   3   Dallas
guillaume@ubuntu:~/$ cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password:
id  name    name
1   San Francisco   California
2   San Jose    California
4   Page    Arizona
6   Paris   Texas
7   Houston Texas
8   Dallas  Texas
guillaume@ubuntu:~/$
```

---

### 10. Genre ID by show

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[10-genre_id_by_show.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/10-genre_id_by_show.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title   genre_id
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$
```

---

### 11. Genre ID for all shows

Import the database dump of `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `10-genre_id_by_show.sql`)

Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- If a show doesn’t have a genre, display `NULL`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[11-genre_id_all_shows.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/11-genre_id_all_shows.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title   genre_id
Better Call Saul    NULL
Breaking Bad    1
Breaking Bad    6
Breaking Bad    7
Breaking Bad    8
Dexter  1
Dexter  2
Dexter  6
Dexter  7
Dexter  8
Game of Thrones 1
Game of Thrones 3
Game of Thrones 4
Homeland    NULL
House   1
House   2
New Girl    5
Silicon Valley  5
The Big Bang Theory 5
The Last Man on Earth   1
The Last Man on Earth   5
guillaume@ubuntu:~/$
```

---

### 12. No genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as 11-genre_id_all_shows.sql)

Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

- Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
- Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[12-no_genre.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/12-no_genre.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title   genre_id
Better Call Saul    NULL
Homeland    NULL
guillaume@ubuntu:~/$
```

---

### 13. Number of shows by genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `12-no_genre.sql`)

Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

- Each record should display: `<TV Show genre> - <Number of shows linked to this genre>`
- First column must be called `genre`
- Second column must be called `number_of_shows`
- Don’t display a genre that doesn’t have any shows linked
- Results must be sorted in descending order by the number of shows linked
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[13-count_shows_by_genre.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/13-count_shows_by_genre.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
genre   number_of_shows
Drama   5
Comedy  4
Mystery 2
Crime   2
Suspense    2
Thriller    2
Adventure   1
Fantasy 1
guillaume@ubuntu:~/$
```

---

### 14. My genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `13-count_shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.

- The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
- Each record should display: `tv_genres.name`
- Results must be sorted in ascending order by the genre name
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[14-my_genres.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/14-my_genres.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
name
Crime
Drama
Mystery
Suspense
Thriller
guillaume@ubuntu:~/$
```

---

### 15. Only Comedy

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `14-my_genres.sql`)

Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
- Each record should display: `tv_shows.title`
- Results must be sorted in ascending order by the show title
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[15-comedy_only.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/15-comedy_only.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title
New Girl
Silicon Valley
The Big Bang Theory
The Last Man on Earth
guillaume@ubuntu:~/$
```

---

### 16. List shows and genres

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `15-comedy_only.sql`)

Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

- If a show doesn’t have a genre, display `NULL` in the genre column
- Each record should display:` tv_shows.title` - `tv_genres.name`
- Results must be sorted in ascending order by the show title and genre name
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[16-shows_by_genre.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/16-shows_by_genre.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title   name
Better Call Saul    NULL
Breaking Bad    Crime
Breaking Bad    Drama
Breaking Bad    Suspense
Breaking Bad    Thriller
Dexter  Crime
Dexter  Drama
Dexter  Mystery
Dexter  Suspense
Dexter  Thriller
Game of Thrones Adventure
Game of Thrones Drama
Game of Thrones Fantasy
Homeland    NULL
House   Drama
House   Mystery
New Girl    Comedy
Silicon Valley  Comedy
The Big Bang Theory Comedy
The Last Man on Earth   Comedy
The Last Man on Earth   Drama
guillaume@ubuntu:~/$
```

---

### 17. Not my genre

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `16-shows_by_genre.sql`)

Write a script that uses the `hbtn_0d_tvshows` database to list all genres not linked to the show `Dexter`

- The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
- Each record should display: `tv_genres.name`
- Results must be sorted in ascending order by the genre name
- You can use a maximum of two `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[100-not_my_genres.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/100-not_my_genres.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 100-not_my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
name
Adventure
Comedy
Fantasy
guillaume@ubuntu:~/$
```

---

### 18. No Comedy tonight!

Import the database dump from `hbtn_0d_tvshows` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql) (same as `100-not_my_genres.sql`)

Write a script that lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`.

- The `tv_genres` table contains only one record where `name` = `Comedy` (but the id can be different)
- Each record should display: `tv_shows.title`
- Results must be sorted in ascending order by the show title
- You can use a maximum of two `SELECT` statement
- The database name will be passed as an argument of the mysql command
- File: **[101-not_a_comedy.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/101-not_a_comedy.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 101-not_a_comedy.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password:
title
Better Call Saul
Breaking Bad
Dexter
Game of Thrones
Homeland
House
guillaume@ubuntu:~/$
```

---

### 19. Rotten tomatoes

Import the database `hbtn_0d_tvshows_rate` dump to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql)

Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_shows.title` - `rating sum`
- Results must be sorted in descending order by the rating
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the `mysql` command
- File: **[102-rating_shows.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/102-rating_shows.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 102-rating_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password:
title   rating
Better Call Saul    163
Homeland    145
Silicon Valley  82
Game of Thrones 79
Dexter  24
House   21
Breaking Bad    16
The Last Man on Earth   10
The Big Bang Theory 0
New Girl    0
guillaume@ubuntu:~/$
```

---

### 20. Best genre

Import the database dump from `hbtn_0d_tvshows_rate` to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql) (same as `102-rating_shows.sql`)

Write a script that lists all genres in the database `hbtn_0d_tvshows_rate` by their rating.

- Each record should display: `tv_genres.name` - `rating sum`
- Results must be sorted in descending order by their rating
- You can use only one `SELECT` statement
- The database name will be passed as an argument of the mysql command
- File: **[103-rating_genres.sql](https://github.com/dany-eduard/holbertonschool-higher_level_programming/tree/main/0x0E-SQL_more_queries/103-rating_genres.sql)**

_*Exaple:*_

```sql
guillaume@ubuntu:~/$ cat 103-rating_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
Enter password:
name    rating
Drama   150
Comedy  92
Adventure   79
Fantasy 79
Mystery 45
Crime   40
Suspense    40
Thriller    40
guillaume@ubuntu:~/$
```

---

### 21. How Do SQL Database Engines Work?

Based on this video:

[![Watch the video](https://img.youtube.com/vi/Z_cX3bzkExE/0.jpg)](https://www.youtube.com/watch?v=Z_cX3bzkExE)

You can find [here](https://github.com/dany-eduard/holbertonschool-higher_level_programming/files/6092554/how-sqlite-works.pdf) the presentation used in the video.

Write a blog post to explain to your mother “How Do SQL Database Engines Work?”. Your blog post should contain:

- an introduction
- complete explanation
- examples (not the same as the video)
- diagrams
- a summary/conclusion
- Your posts should have many code/output examples to illustrate what you are explaining, and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

My post [here]()

---

⌨️ con ❤️ por [dany eduard](https://github.com/dany-eduard) 😊
