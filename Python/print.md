# print


```python
A =" "
B =u"\u2581"
C =u"\u2582"
D =u"\u2583"
E =u"\u2584"
F =u"\u2585"
G =u"\u2586"
H =u"\u2587"
I =u"\u2588"

for i in A,B,C,D,E,F,G,H,I:
  print("\x1b[3;45;6m%s\x1b[0m"%(i),end='')	
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1579675315341-8baaaabd-65cc-411c-8c8b-0b3232f9018c.png#align=left&display=inline&height=79&name=image.png&originHeight=79&originWidth=443&size=9295&status=done&style=none&width=443)
