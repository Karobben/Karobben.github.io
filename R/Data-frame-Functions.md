---
url: data.frame
---

# Data frame Functions


```r
Shrink <-  function(Data, P){
  Num = round(nrow(world)/P)
	Data = Data[c(1:Num)*P,]
}
```

```r
world <- map_data("world")
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1580007783801-b9ff0a91-0801-49f0-959f-16830969c90e.png#align=left&display=inline&height=264&name=image.png&originHeight=264&originWidth=236&size=22009&status=done&style=none&width=236)<br />


