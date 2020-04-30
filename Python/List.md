---
url: ogsro7
---

# List


<br />int list to str list<br />

```python
a_list = ["1", "2", "3"]
#int list to str list
list(map(str, a_list))
#str list to int list
list(map(int, a_list))


# 逐个相减
c = [b[i] - a[i] for i in range(len(a))]
```


<a name="YhYad"></a>
# Compare Two list


```python
l = [1, 2, 3, 5]
l_one = [2, 8, 6, 10]
print set(l) & set(l_one)
```


