---
toc: true
url: threading
covercopy: © thepythoncode.com
date: 2021-03-19 09:02:38
title: "Python|Threading: Thread-based parallelism for beginner"
description: "Threading is a separate flow of execution. With the help of `Threading`, you can run different tasks without blocking the main-stream."
excerpt: "Threading is a separate flow of execution. With the help of 'Threading', you can run different tasks without blocking the main-stream."
tags: [Python]
category: [Python, Scripting, Module]
cover: "https://www.thepythoncode.com/media/articles/using-threads-in-python.PNG"
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---
## Tutorial from [RealPython](https://realpython.com/intro-to-python-threading/)[^realpython]

[^realpython]: https://realpython.com/intro-to-python-threading/

> Python threading allows you to have different parts of your program run concurrently and can simplify your design. If you’ve got some experience in Python and want to speed up your program using threads, then this tutorial is for you![^realpython]

## What's a Threading?
Threading is a separate flow of execution. In bash, you can run a background process by adding a symbol `&` at the end of commands. In python, we can achieve this with the example below.

As you might expect, if you run the codes below, `thread_function(3)` will be started at the end of `thread_function(4)`

```python PYTHON
import threading
import time

def thread_function(Time):
  for i in range(Time):
    time.sleep(i)
    print(i)

thread_function(4)
thread_function(3)
```
<pre>
  0
  1
  2
  3
  0
  1
  2
</pre>

But if we execute it in a `threading` or background process, they can run simultaneously.
```diff PYTHON
- thread_function(4)
+ x = threading.Thread(target=thread_function, args=(4,))
+ x.start()
+ # x.join()
thread_function(3)
```
<pre>
  0
  0
  1
  1
  2
  2
  3
</pre>

This is how we expect the background process, or **daemon threads**, to be performed.

## `join()`
Some times, we'd like waiting for the threads. By doing so, we can call `.join()` to do so.

By uncomment `x.join()`, we can get the same result as the first.
```python PYTHON
import threading
import time

def thread_function(Time):
  for i in range(Time):
    time.sleep(i)
    print(i)

x = threading.Thread(target=thread_function, args=(4,))
x.start()
x.join()
thread_function(3)
```
<pre>
  0
  1
  2
  3
  0
  1
  2
</pre>

## Working in a loop

```python
threads = list()  
for Time in range(5):
  x = threading.Thread(target=thread_function, args=(Time,))
        threads.append(x)
        x.start()
```
<pre style="height-max:300px">
  0
  0
  0
  0
  1
  1
  1
  2
  2
  3
</pre>

## ThreadPoolExecutor
```python
import threading
import time
import concurrent.futures

def thread_function(Time):
  for i in range(Time):
    time.sleep(i)
    print(i,"from", Time)
  print(Time, "is Down")

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(10))
```

<pre style="max-height:300px">
  0 is Down
  0 from 1
  0 from 2
  1 is Down
  0 from 3
  0 from 4
  1 from 2
  2 is Down
  0 from 5
  1 from 4
  1 from 3
  1 from 5
  2 from 4
  2 from 3
  3 is Down
  0 from 6
  1 from 6
  2 from 5
  3 from 4
  4 is Down
  0 from 7
  2 from 6
  1 from 7
  3 from 5
  2 from 7
  3 from 6
  4 from 5
  5 is Down
  0 from 8
  3 from 7
  1 from 8
  4 from 6
  2 from 8
  4 from 7
  3 from 8
  5 from 6
  6 is Down
  0 from 9
  1 from 9
  5 from 7
  2 from 9
  4 from 8
  3 from 9
  5 from 8
  6 from 7
  7 is Down
  4 from 9
  6 from 8
  5 from 9
  6 from 9
  7 from 8
  8 is Down
  7 from 9
  8 from 9
  9 is Down
</pre>

> The code creates a ThreadPoolExecutor as a context manager, telling it how many worker threads it wants in the pool. It then uses .map() to step through an iterable of things, in your case range(3), passing each one to a thread in the pool.[^realpython]



## TEST

```python
import threading, time
def sleep():
  time.sleep(30)
  print("sleep is down")

x = threading.Thread(target=test, args=())
x.start()
x = threading.Thread(target=test, args=())
x.is_alive()

```
