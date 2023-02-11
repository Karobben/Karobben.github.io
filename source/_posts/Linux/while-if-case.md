---
title: "If & whle & case"
description: "If & whle & case"
url: leaei2
date: 2020/06/26
toc: true
excerpt: "Add a user"
tags: [Linux, bash, Script]
category: [Linux, Bash, More]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## If & whle & case



```bash
if [ 1 -eq 1 ] #expression
then
   #Statement(s) to be executed if expression is true
   echo Yes
fi
```

pairwise-compare with if loop

[© Ole Tange; 2018](https://unix.stackexchange.com/questions/490649/pairwise-combinations-of-filenames)
```bash
for i in *.txt ; do
  for j in *.txt ; do
    if [ "$i" '<' "$j" ] ; then
      echo "Pairs $i and $j"
    fi
  done
done
```

### 字符串判断

```bash
##https://blog.csdn.net/Primeprime/article/details/79625306
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

## while
```bash
while [ expression ]
do
   Statement(s) to be executed if expression is true
done
```

## try

reference:[筱光](https://blog.csdn.net/womeng2009/article/details/80814284)
```bash
{ # try

    command1
    #save your output

} || { # except
    # save log for exception
}
```
