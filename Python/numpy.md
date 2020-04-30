# numpy

<a name="gXQd0"></a>
# 1. np array
<a name="Gf9EI"></a>
## 1.1 np arry to list
```python
import numpy as np

List = arry.tolist()
```

<br />

<a name="wUuDx"></a>
# 2 np arrary caculating


<a name="ZazdT"></a>
## 2.1 np.arrary sum()
```python
np.sum(array1-array2)
```

<br />

<a name="4r3Wb"></a>
# 3 np arrary append #


<a name="y3YRe"></a>
## 3.1 append


```python
np.appedn(np1, np2,axis=0)
```

<br />

<a name="bDJYs"></a>
## Reduce Dimension


```python
x = np.array([[1, 2],[3, 4]])
print(np.ravel(x))      
print(np.ravel(x,'F'))  
```

<br />

<a name="LXdEA"></a>
# 4 Locating (argwhere)


```python
arr = np.random.randint(0,10, (3,4))  
index = np.argwhere(arr < 5)
index2 = np.where(arr < 5)

>>> index
array([[0, 2],
       [0, 3],
       [1, 1],
       [2, 0],
       [2, 3]])
>>> index2
(array([0, 0, 1, 2, 2]), array([2, 3, 1, 0, 3]))
```


<a name="ZLpsN"></a>
# Replace


```python
arr[arr > 255] = x
```

<br />
<br />
<br />
<br />ummmm... I am not really like to using numpy because I thing data.frame() in R is much better.
