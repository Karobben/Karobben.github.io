---
title: "Quick Guide of Mysql for Newbies"
description: "Quick Guide of Mysql for Newbies| Mysql 快速入门"
date: 2021/01/31
url: mysql
toc: true
excerpt: "A quick guide to familiar with Mysql"
tags: [Linux, Database, Mysql, bash]
category: [Linux, Data]
cover: 'https://www.educba.com/academy/wp-content/uploads/2018/10/CheatSheet-on-MySQL.jpg'
thumbnail: 'https://cn.bing.com/th?id=AMMS_5c8bbd728b92b1a4b68f74bc8acdd216&w=110&h=110'
priority: 10000
covercopy: '© educba'
---

## Quick Guide of Mysql for Newbies

[Video tutorial](https://www.bilibili.com/video/BV1iJ411m7Fj?from=search&seid=986172806903606724)
[Text Tutorial](https://www.runoob.com/mysql/mysql-like-clause.html)

## Dataabse type

|Relation Database|Non-relational Database|
|:--|:--|
|- Store specific types of project like customer, products.<br>- Store as tables|- No tables or relationships<br>- Don't understand SQL|

## INSTALL

For Ubuntu:[雪梦科技 2020; 云栖社区](https://yq.aliyun.com/articles/758177), Mac: [WebCoder 2016, 简书](https://www.jianshu.com/p/fd3aae701db9); Windows: [BruceLong 2020; 博客园](https://www.cnblogs.com/yunlongaimeng/p/12558638.html)

## Quick Start

```bash
mysql
```
```sql
-- print store location
show variables like '%datadir%';

-- print database in stoarage
SHOW DATABASES;

-- Create a new database
CREATE DATABASE `sql_invoicing`;
-- Access the database
USE `sql_invoicing`;

-- Create a table
CREATE TABLE runoob_tbl(
  runoob_id INT NOT NULL AUTO_INCREMENT,
  runoob_title VARCHAR(100) NOT NULL,
  runoob_author VARCHAR(40) NOT NULL,
  submission_date DATE,
  PRIMARY KEY ( runoob_id )
  )ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- show tables
SHOW TABLES

-- Check the index
desc runoob_tbl

/*
INT: datatype = integer;
DATE: datatype = date;
NOT NULL: value auto-fill;
AUTO_INCREMENT:  fill-logic;
VARCHAR(10): ??? I don't know
*/
-- Insert value to table
INSERT INTO runoob_tbl
  (runoob_title, runoob_author, submission_date)
  VALUES
  ("学习 PHP", "菜鸟教程", NOW());

-- Insert multi-lines value to table
INSERT INTO runoob_tbl
  (runoob_title, runoob_author, submission_date)
  VALUES
  ("学习 myspl", "karobben", NOW()),
  ('learn python', 'Karobben', NOW());

-- Print the whole table
SELECT * from runoob_tbl;
-- Print the `runoob_title` column(field)
SELECT `runoob_title` from runoob_tbl;
-- Print the filtered result by WHEN
SELECT * from runoob_tbl WHERE runoob_author='karobben'; #Capitals letters tolerant
SELECT * from runoob_tbl WHERE BINARY runoob_author='Karobben'; #Capital letter matters
-- Print the filtered result by LIKE
SELECT * from runoob_tbl  WHERE runoob_author LIKE '%rob%';

-- Change the value of tables by update
UPDATE runoob_tbl SET runoob_title='sleep' WHERE runoob_id=3;
-- Change a part of string in column(field)
UPDATE runoob_tbl  SET runoob_author=REPLACE(runoob_author, 'ka', 'Ka')
-- Change the value of table by delete
DELETE FROM runoob_tbl WHERE runoob_id=1;

-- delete the tale
DROP TABLE `runoob_tbl`;
-- delete the database
DROP DATABASE `sql_invoicing`
```


## Set Environment

Change the store directory: [虫文儿~ 2019; 博客园](https://www.cnblogs.com/Lans-word/p/12080177.html)

### Show the directory of the DATABASE
```sql
show variables like '%datadir%';
```

### Show all databases
```sql
SHOW DATABASES;
```

## Create & Drop

### Database
ps: ';' is needed for separate commands in sql language.

```sql
CREATE DATABASE IF NOT EXISTS `sql_invoicing`;
USE `sql_invoicing`;

SET NAMES utf8;
SET character_set_client= utf8mb4;

SHOW DATABASES;
```
<pre>
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sql_invoicing      |
| sys                |
+--------------------+
</pre>

```sql
drop database `sql_invoicing`; #deleting sql_invoicing
```

### Table
```sql
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

SHOW TABLES;
desc runoob_tbl;
```
<pre>
+-------------------------+
| Tables_in_sql_invoicing |
+-------------------------+
| runoob_tbl              |
+-------------------------+
1 row in set (0.00 sec)

+-----------------+--------------+------+-----+---------+----------------+
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| runoob_id       | int(11)      | NO   | PRI | NULL    | auto_increment |
| runoob_title    | varchar(100) | NO   |     | NULL    |                |
| runoob_author   | varchar(40)  | NO   |     | NULL    |                |
| submission_date | date         | YES  |     | NULL    |                |
+-----------------+--------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
</pre>

```sql
DROP TABLE runoob_tbl;
```
### Datatypes
Details: [runoob.com](https://www.runoob.com/mysql/mysql-data-types.html)

## INSERT
### Insert a Row
```sql
-- Insert value to table
INSERT INTO runoob_tbl
  (runoob_title, runoob_author, submission_date)
  VALUES
  ("学习 PHP", "菜鸟教程", NOW());

-- Insert multi-lines value to table
INSERT INTO runoob_tbl
  (runoob_title, runoob_author, submission_date)
  VALUES
  ("学习 myspl", "karobben", NOW()),
  ('learn python', 'Karobben', NOW());
```

### ALTER (insert a column)
```sql
ALTER TABLE runoob_tbl
ADD COLUMN Citation VARCHAR(15) AFTER runoob_author;
```

## Select the column
### WHERE
```sql
SELECT * from runoob_tbl WHERE runoob_author='karobben';
```
<pre>
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         2 | 学习 myspl   | <span style='background-color:salmon'>Karobben</span>      | 2021-01-31      |
|         3 | sleep        | <span style='background-color:salmon'>Karobben</span>      | 2021-01-31      |
|         4 | learn python | <span style='background-color:salmon'>Karobben</span>      | 2021-01-31      |
+-----------+--------------+---------------+-----------------+
3 rows in set (0.00 sec)
</pre>
### LIKE
```sql
-- match the column which end with a| grep a$
'%a'     
-- match the column which start with a| grep ^a
'a%'     
-- match the column which contain a| grep a
'%a%'    
-- match pattern: grep ^.a.$
'_a_'    
-- match pattern: grep ^.a$
'_a'
-- match pattern: grep ^a$
'a_'

SELECT * from runoob_tbl  WHERE runoob_title LIKE '% %';
```
<pre>
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         2 | 学习<span style='background-color:salmon'> </span>myspl   | Karobben      | 2021-01-31      |
|         4 | learn<span style='background-color:salmon'> </span>python | Karobben      | 2021-01-31      |
+-----------+--------------+---------------+-----------------+
2 rows in set (0.00 sec)
</pre>

## UPDATE & DELETE
```sql
UPDATE runoob_tbl SET runoob_title='学习 C++' WHERE runoob_id=3;
DELETE FROM runoob_tbl WHERE runoob_id=3;
```
## UNION

So, union could combine the unique values from different selected columns to a new table
``sql
SELECT runoob_title FROM runoob_tbl
UNION
SELECT runoob_author FROM runoob_tbl;
``
<pre>
+--------------+
| runoob_title |
+--------------+
| 学习 myspl   |
| sleep        |
| learn python |
| Karobben     |
+--------------+
</pre>

it can also be used to merge tables: [Example](https://www.runoob.com/mysql/mysql-union-operation.html)


## ORDER
```sql
SELECT * from runoob_tbl;
SELECT * from runoob_tbl ORDER BY runoob_title ASC;
```
<pre>
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         2 | 学习 myspl   | Karobben      | 2021-01-31      |
|         3 | sleep        | Karobben      | 2021-01-31      |
|         4 | learn python | Karobben      | 2021-01-31      |
+-----------+--------------+---------------+-----------------+
+-----------+--------------+---------------+-----------------+
| runoob_id | runoob_title | runoob_author | submission_date |
+-----------+--------------+---------------+-----------------+
|         4 | learn python | Karobben      | 2021-01-31      |
|         3 | sleep        | Karobben      | 2021-01-31      |
|         2 | 学习 myspl   | Karobben      | 2021-01-31      |
+-----------+--------------+---------------+-----------------+
</pre>

## INPUT and Output

### Input

```sql
-- insert and replace
LOAD DATA INFILE '/var/lib/mysql-files/test.csv' REPLACE
INTO TABLE regulation_net
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n';

IGNORE 1 ROWS;
```

### output
```bash
## output sql as txt file
mysqldump -h other-host.com -P port -u root -p database_name > dump.txt
```

```sql
-- output as csv
SELECT * FROM regulation_net;


SELECT * INTO OUTFILE '/var/lib/mysql-files/test.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM regulation_net;
```
