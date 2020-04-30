---
url: opencv_gif
---

# Opencv & gif

reference: [https://blog.csdn.net/qq_41500251/article/details/82820806](https://blog.csdn.net/qq_41500251/article/details/82820806)
```python
import time, cv2
from PIL import Image
import numpy as np

def GIF(file):
    List = []
    im = Image.open(file)
    im.seek(1)#skip to the second frame
    try:
        while 1:
            List += [cv2.cvtColor(np.asarray(im.convert()),cv2.COLOR_RGB2BGR)]
            im.seek(im.tell()+1)
    except EOFError:#the sequence ends
        pass
    Num = 0
    while Num < len(List)*2:
        Num +=1
        ID = Num%(len(List))
        cv2.imshow("OpenCV",List[ID])
        print(ID)
        cv2.waitKey(1)
        time.sleep(0.1)
    cv2.destroyAllWindows()
```


