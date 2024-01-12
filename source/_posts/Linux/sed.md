---
title: "sed 匹配编辑"
description: "sed 匹配编辑"
url: sed2
date: 2020/06/26
toc: true
excerpt: "sed ('stream editor') is a Unix utility that parses and transforms text, using a simple, compact programming language. sed was developed from 1973 to 1974 by Lee E. McMahon of Bell Labs, and is available today for most operating systems."
tags: [Linux, Scripting, bash, CLI Tools]
category: [Linux, Bash, awk/grep/sed]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## sed 匹配编辑


## Sed substitute

```bash
## substitute the first 't' to 'T'
sed 's/t/T/' file
## substitute all 't' to 'T'
sed 's/t/T/g' file

## substitute 'all little letters' to 'T'
sed 's/[a-z]/T/g' file
## similarly, you can substitute 'all numbers' to 'T'
sed 's/[0-9]/T/g' File
```

## Deleted matched line

```bash
sed '/pattern/d' filename

sed '1d' filename # deleted the first line only
sed '2d' filename # deleted the second line only
```

## Adding a line

```bash
## adding a line before the matched line
sed -i '/allow chengyongxu.com/i\allow chengyongxu.cn' file
## adding a line after the matched line
sed -i '/allow chengyongxu.com/a\allow chengyongxu.cn' file
```

## Match pattern
|Pattern|Meanings|Example|Result|
|--|--|--|--|
|`^`|The begin of each line|`sed '/^A/d' file`|Delete all lines which begin with 'A'|
|`$`|The end of each line|`sed 's/$/+/' file`| Add a '+' at the end of all lines|
|`[ ]`|match all single elements in it|`sed 's/[abcd]/T/g' file`|Replace all 'a', 'b', 'c', and 'd' to 'T'|


## Sed
```bash
sed 's/^t/000/g' filename #the t on beginning of the lines replaced by ***
sed 's/t$/000/g' filename #000 as a substitute for the t on the end of the lines

sed 's/[0-9]/*/' filename # * as a subustitute for every number with *

sed 's/[a-z][A-Z]/--/' filename # looking for a pattern that a lower capital followed a capital
## TaT -->  T--

sed 's/[a-zA-Z]/--/g' filename # -- as a substitute for all letters on the filename
or
sed 's/[a-Z]/--/g' filename

sed 's/[0-z]/--/g' filename

sed 's/[0-9]/-&-/g' filename # exp: 833 new -- > -8--3--3- new
sed 's/[0-9][0-9]/-&-/g' filename # exp: 833 new -- > -833- new

sed 's/\w/_/g' filename # or letters except symples.(including chinese)

sed 's/\b/==/g' filename # add a "==" on the begin and the end of all words
## ==4811==  ==that==  [==ðæt==; ==ðət==]

sed 's/[^0-9]/*/g' filename # ^ means negated match

sed 's/A/B/g;s/C/D/f' FILENAME

#############################
### deleted the match line ##
#############################

sed '/\bnew\b/d' filename #boundary (new),( new),(new ),( new ),( new, )

sed '/^$/d' # remove the line which beginning with end (blank line)


sed '5,$ d' filename
equo
sed '4 q' filename
equo head -n 4 filename
```


## Others

### remove ^M

!!! note Before
    <pre>
    TGCTGATCGATCGTAGCTAGCTAGCG<font color="red">^M</font>
    CATGTCTGATCAGTGCTAGCTGATCG<font color="red">^M</font>
    </pre>

`sed -i 's/\r//' file`

!!! note After
    <pre>
    TGCTGATCGATCGTAGCTAGCTAGCG
    CATGTCTGATCAGTGCTAGCTGATCG
    </pre>


<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
