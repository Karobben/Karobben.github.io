---
url: leaei2
---

# If & whle & case



```bash
if [ expression ]
then
   Statement(s) to be executed if expression is true
fi
```

<br />字符串判断
```bash
#https://blog.csdn.net/Primeprime/article/details/79625306
strA="long string"
strB="string"
result=$(echo $strA | grep "${strB}")
if [[ "$result" != "" ]]
then
  echo "包含"
else
  echo "不包含"
fi
```
```bash
while [ expression ]
do
   Statement(s) to be executed if expression is true
done
```


