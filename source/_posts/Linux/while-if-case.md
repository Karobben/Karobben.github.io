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

[© Bash Test Operators](https://kapeli.com/cheat_sheets/Bash_Test_Operators.docset/Contents/Resources/Documents/index)

|||
|:-:|:-|
-eq |is equal to
-ne |is not equal to
-gt|is greater than
-ge|is greater than or equal to
-lt|is less than
-le|is less than or equal to
<|is less than
<=|is less than or equal to
>|is greater tha
>=|is greater than or equal to
=|is equal to
==|The == comparison operator behaves differently within a double-brackets test
!=|is not equal to
<|is less than, in ASCII alphabetical order
>|is greater than, in ASCII alphabetical order.
-z|string is null
-n|string is not null.
-e|file exists
-a|is deprecated and its use is discouraged.
-f|file is a regular file (not a directory or device file)
-d|file is a directory
-h|file is a symbolic link
-L|file is a symbolic link
-b|file is a block device
-c|file is a character device
-p|file is a pipe
-S|file is a socket
-s|file is not zero size
-t|file (descriptor) is associated with a terminal device;
-r|file has read permission (for the user running the test)
-w|file has write permission (for the user running the test)
-x|file has execute permission (for the user running the test)
-g|set-group-id (sgid) flag set on file or directory
-u|set-user-id (suid) flag set on file
-k|sticky bit set
-O|you are owner of file
-G|group-id of file same as yours
-N|file modified since it was last read
-nt|file f1 is newer than f2 `if [ "$f1" -nt "$f2" ]`
-ot|file f1 is older than f2 `if [ "$f1" -ot "$f2" ]`
-ef| files f1 and f2 are hard links to the same file `if [ "$f1" -ef "$f2" ]`
!|"not" -- reverses the sense of the tests above (returns true if condition absent).


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
