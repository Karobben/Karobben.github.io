---
toc: true
url: dictionary
covercopy: '<a href="https://pixabay.com/users/geralt-9301/">© geralt</a>'
priority: 10000
date: 2023-03-01 12:41:49
title: "Python Dictionary is awesome"
ytitle: "Python Dictionary is awesome"
description: "Python Dictionary is awesome"
excerpt: "A dictionary in Python is an unordered collection of key-value pairs. It is a mutable, indexed, and iterable data structure that is commonly used to store and retrieve data. The keys in a dictionary must be unique and immutable (strings, integers, tuples) while the values can be of any data type (strings, integers, lists, sets, other dictionaries, etc.)"
tags: [Python]
category: [Python, Beginner]
cover: "https://cdn.pixabay.com/photo/2018/04/25/08/41/books-3348990_960_720.jpg"
thumbnail: "https://cdn.pixabay.com/photo/2018/04/25/08/41/books-3348990_960_720.jpg"
---



## Dictionary


A dictionary in Python is an unordered collection of key-value pairs. It is a mutable, indexed, and iterable data structure that is commonly used to store and retrieve data. The keys in a dictionary must be unique and immutable (strings, integers, tuples) while the values can be of any data type (strings, integers, lists, sets, other dictionaries, etc.). It could be create by `my_dict = {"name": "John", "age": 25, "city": "New York"}`


Here is some basic operations for Python dictionary
1. Creating a dictionary
```python
my_dict = {"name": "John", "age": 25, "city": "New York"}
```
2. Accessing values using keys

```python
print(my_dict["name"]) 
print(my_dict["age"]) 
```
<pre>
John
25
</pre>


3. Adding a new key-value pair

```python
my_dict["country"] = "USA"
print(my_dict)  
```
<pre>
{"name": "John", "age": 25, "city": "New York", "country": "USA"}
</pre>


4. Removing and Updating

```python
del my_dict["city"]
my_dict["age"] = 26
```

5. Checking if a key exists in a dictionary
```python
if "name" in my_dict:
    print("Name is present")
else:
    print("Name is not present")

# Iterating through a dictionary
for key, value in my_dict.items():
    print(key, value)
```

## Find the max value from a dictionary

```python
d = {'a': 10, 'b': 5, 'c': 20}
max_value = max(d, key=d.get)
print(max_value)
```

<pre>
c
</pre>












































































































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
