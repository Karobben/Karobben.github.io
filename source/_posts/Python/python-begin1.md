---
toc: true
url: python_begin1
covercopy: © getcodify.com
priority: 10000
date: 2021-03-29 22:10:23
title: "Python Challenge for Beginner | rosalind"
ytitle: "Python 入门练习"
description: "Python challenges for beginners"
excerpt: "Python challenges for beginners"
tags: [Python]
category: [Python, Beginner]
cover: "https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680"
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
---

Notation: Those Challenges come from [Rosalind](http://rosalind.info)

## Introduction

Function:

```python
def run(a, b):
  Result = a + b
  print("hello function")
  return Result
```

Function test:

```python
C = run(1 , 5)
print(C)
```

<pre>
hello function
6
</pre>

## Let the fun begin!

### Calculate
[Link](http://rosalind.info/problems/ini2/)
Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
<pre>
in: 3 5
out: 34
</pre>
```python
def run(a, b):
  Result = (a+b)**2 - 2ab
  print(Result)

run(3, 4)
```

### String splice
[Link](http://rosalind.info/problems/ini3/)
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

<pre>
in:
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

out:
Humpty Dumpty
</pre>

```python
def run(Str, a, b, c, d):
  Result = Str[a:b+1] + " " Str[c:d+1]
  print(Result)

Str = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
a = 22; b = 27; c = 97; d = 102

run(Str, a, b, c, d)
```

### loop
[Link](http://rosalind.info/problems/ini4/)
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.

<pre>
in:
100 200
out:
7500
</pre>

```python
def run(a, b):
  List = [a, b]
  List.sort()
  Result = 0
  for i in range(List[0], List[1]+1):
    if i % 2 == 1:
      Result += i
  print(Result)

run(100, 200)
```

### Reading and writing
[Link](http://rosalind.info/problems/ini5/)
Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

```python
def run(INPUT, OUTPUT):
  In = open(INPUT, 'r').readlines()
  Num = 0
  Result = ""
  for i in In:
    if Num % 2 == 1:
      Result += i
    Num += 1
  print(Result)
  F = open(OUTPUT, 'w')
  F.write(Result)
  F.close()
```

### Words count
[Link](http://rosalind.info/problems/ini6/)
Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

<pre>
In:
We tried list and we tried dicts also we tried Zen

Out:
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
</pre>

```python
def run(Str):
  List = Str.split(" ")
  Index = list(set(List))
  Result = ""
  for i in Index:
    if i != "":
      Result += i +" " + str(List.count(i)) +"\n"
  print(Result)
```
