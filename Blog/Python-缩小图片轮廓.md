---
url: ghlobk
---

# Python 缩小图片轮廓

![1237527.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581336857706-4fa9eff1-167d-49b1-a0b4-1cfdf23b0e50.png#align=left&display=inline&height=162&name=1237527.png&originHeight=293&originWidth=625&size=4125&status=done&style=none&width=346)<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581340867450-ec0665e8-c7a4-4477-ad08-7c51d9d7714d.png#align=left&display=inline&height=159&name=image.png&originHeight=273&originWidth=591&size=5092&status=done&style=none&width=345)

原图轮廓太粗，希望细一些- -但是不会PS GIMP。所以想用Python解决。<br />思路： 保留四周都有有效颜色的点

```python
import numpy as np
import cv2

def Reduice(img):
    Result=[]
    for i in range(1,H-1):
        for ii in range(1,W-1):
            pix = [list(img[i-1][ii]), # LEFT
                   list(img[i+1][ii]), # RIGHT
                   list(img[i][ii-1]), # UP
                   list(img[i][ii+1]), # DOWN
                   list(img[i-1][ii-1]), # LU
                   list(img[i+1][ii-1]), # RU
                   list(img[i-1][ii+1]), # LD
                   list(img[i+1][ii+1]), # RD
                  ]
            if pix ==[[0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,], [0,0,0,]]:
                Result +=[[i,ii]]
    return Result

img = cv2.imread('111.png')
H = len(img)
W = len(img[0])

#赋值到另一个图片：
for i in range(5):
    Result = Reduice(img)
    img2 = np.array(img)
    img2[img2!=254]=254
    for i in Result:
        img2[i[0],i[1]]=img[i[0],i[1]]
    img =np.array(img2)
    
cv2.imwrite('5.png',img)
# 接下来，减一次，输出一张图

Num = 5
for i in range(5):
    Num +=1
    Result = Reduice(img)
    img2 = np.array(img)
    img2[img2!=254]=254
    for i in Result:
        img2[i[0],i[1]]=img[i[0],i[1]]
    img =np.array(img2)
    cv2.imwrite(str(Num)+'.png',img)

def View(img):
    while(True):
        #img = cv2.imread('111.png')
        cv2.imshow('image',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1581342022215-163873d3-e629-4e20-8fb5-182ecdc509e4.png#align=left&display=inline&height=197&name=image.png&originHeight=197&originWidth=644&size=20529&status=done&style=none&width=644)





--------------------------------------------------------------------------------------------------------------------------------------------<br />github: [https://github.com/Karobben](https://github.com/Karobben)<br />blog: [Karobben.github.io](http://Karobben.github.io)<br />R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
