---
title: "sed 匹配编辑"
description: "sed 匹配编辑"
url: sed2
---

# sed 匹配编辑

Sed
```bash


sed 's/t/T/' filename # sed 's/t/T/g' filename

sed 's/^t/000/g' filename #the t on beginning of the lines replaced by ***
sed 's/t$/000/g' filename #000 as a substitute for the t on the end of the lines

sed 's/[0-9]/*/' filename # * as a subustitute for every number with *

sed 's/[a-z][A-Z]/--/' filename # looking for a pattern that a lower capital followed a capital
# TaT -->  T--

sed 's/[a-zA-Z]/--/g' filename # -- as a substitute for all letters on the filename
or
sed 's/[a-Z]/--/g' filename

sed 's/[0-z]/--/g' filename

sed 's/[0-9]/-&-/g' filename # exp: 833 new -- > -8--3--3- new
sed 's/[0-9][0-9]/-&-/g' filename # exp: 833 new -- > -833- new

sed 's/\w/_/g' filename # or letters except symples.(including chinese)

sed 's/\b/==/g' filename # add a "==" on the begin and the end of all words
# ==4811==  ==that==  [==ðæt==; ==ðət==]

sed 's/[^0-9]/*/g' filename # ^ means negated match

sed 's/A/B/g;s/C/D/f' FILENAME

############################
## deleted the match line ##
############################

sed '/pattern/d' filename
sed '/\bnew\b/d' filename #boundary (new),( new),(new ),( new ),( new, )

sed '/^$/d' # remove the line which beginning with end (blank line)


sed '5,$ d' filename
equo
sed '4 q' filename
equo head -n 4 filename

sed '1d' filename # deleted the first line only
sed '2d' filename # deleted the second line only

```



---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
