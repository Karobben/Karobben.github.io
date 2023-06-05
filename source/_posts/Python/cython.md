---
toc: true
url: cython
covercopy: © Karobben
priority: 10000
date: 2023-05-17 22:34:30
title: 'Cython'
ytitle: 'Cython'
description: 'Cython, make python faster!'
excerpt: 'Cython, make python faster!'
tags: [Python]
category: [Python]
cover: "https://cython.readthedocs.io/en/latest/_static/cythonlogo.png"
thumbnail: "https://cython.readthedocs.io/en/latest/_static/cythonlogo.png"
---

## Cython 

Tutorial: [cython](https://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html)

## Hello world

First, write the code in the file `helloworld.pyx`
```python
print("Hello World")
```

Then, write a file `setup.py` with codes below: 
```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("helloworld.pyx")
)
```

Now, let's setup the Cython in the terminal/cmd

```bash
python setup.py build_ext --inplace
```
<pre>
Compiling helloworld.pyx because it changed.
[1/1] Cythonizing helloworld.pyx
/home/ken/.local/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /home/ken/test/helloworld.pyx
  tree = Parsing.p_module(s, pxd, full_module_name)
running build_ext
building 'helloworld' extension
gcc -pthread -B /mnt/8A26661926660713/Conda/miniconda/compiler_compat -Wno-unused-result -Wsign-compare -DNDEBUG -fwrapv -O2 -Wall -fPIC -O2 -isystem /mnt/8A26661926660713/Conda/miniconda/include -fPIC -O2 -isystem /mnt/8A26661926660713/Conda/miniconda/include -fPIC -I/mnt/8A26661926660713/Conda/miniconda/include/python3.8 -c helloworld.c -o build/temp.linux-x86_64-cpython-38/helloworld.o
gcc -pthread -B /mnt/8A26661926660713/Conda/miniconda/compiler_compat -shared -Wl,--allow-shlib-undefined -Wl,-rpath,/mnt/8A26661926660713/Conda/miniconda/lib -Wl,-rpath-link,/mnt/8A26661926660713/Conda/miniconda/lib -L/mnt/8A26661926660713/Conda/miniconda/lib -Wl,--allow-shlib-undefined -Wl,-rpath,/mnt/8A26661926660713/Conda/miniconda/lib -Wl,-rpath-link,/mnt/8A26661926660713/Conda/miniconda/lib -L/mnt/8A26661926660713/Conda/miniconda/lib build/temp.linux-x86_64-cpython-38/helloworld.o -o build/lib.linux-x86_64-cpython-38/helloworld.cpython-38-x86_64-linux-gnu.so
copying build/lib.linux-x86_64-cpython-38/helloworld.cpython-38-x86_64-linux-gnu.so -> 
</pre>

Finally, import it in any python interpreter:
```python
import helloworld
```

<pre>
Hello World
</pre>


## Speed up the for loop

First, let's create a file named `example.pyx` with the following Cython code:

```python
# example.pyx
def sum_elements(double[:] array):
    cdef int i
    cdef double result = 0

    for i in range(array.shape[0]):
        result += array[i]

    return result
```

To compile and use the Cython code, you'll need a setup.py file. Create a `setup.py` file with the following content:

```python
# setup.py
from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("example.pyx"),
    include_dirs=[np.get_include()]
)
```

Next, compile the example.pyx file:
```bash
python setup.py build_ext --inplace
```

Now, you can test it in the python

```python
import time
import numpy as np
from example import sum_elements

# define the same function in python to compare the time consuming
def sum_elements_py(array):
  result = 0
  for i in range(array.shape[0]):
    result += array[i]
  return(result)


array = np.array([1.0, 2.0, 3.0, 4.0, 5.0]*200000, dtype=np.float64)

A = time.time()
sum_elements(array)
print(time.time() - A)

A = time.time()
sum_elements_py(array)
print(time.time() - A)

from numba import njit

@njit
def sum_elements_numba(array):
    result = 0.0
    for i in range(array.shape[0]):
        result += array[i]
    return result

```

<pre>
0.001369476318359375
0.11698126792907715
</pre>

When there are 1M loops, Cython is 85 times faster than python.


```python
array = np.array([1.0, 2.0, 3.0, 4.0, 5.0]*20000000, dtype=np.float64)

A = time.time()
sum_elements_py(array)
print(time.time() - A)


A = time.time()
sum_elements(array)
print(time.time() - A)

A = time.time()
sum_elements_numba(array)
print(time.time() - A)
```

<pre>
13.218583345413208
0.11868596076965332
0.19266653060913086
</pre>

When there are 10000M loops, Cython is 85 times faster than python.






<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
