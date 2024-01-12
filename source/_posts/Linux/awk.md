---
title: "awk 语言基础"
description: "awk 语言基础"
url: awk2
date: 2020/06/23
toc: true
excerpt: "AWK (awk) is a domain-specific language designed for text processing and typically used as a data extraction and reporting tool. Like sed and grep, it is a filter, and is a standard feature of most Unix-like operating systems."
tags: [Linux, Scripting, bash, CLI Tools]
category: [Linux, Bash, awk/grep/sed]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## awk 语言基础

<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>

```bash
awk -F\; '{print $1}' filename # print the first column
awk -F\; '{print $(NF)}' filename # print the last column
```

```bash
awk '/^the/' filename # the every line starting with the 'the'
awk '/the$/' filename # the every line ending with the 'the'
awk '/[0-9]/' filename # the every line contain numbers
awk '/[a-z]/' filename # the every line contain the lower capital letters
awk '/hel+0/' filename #  helllllo hello
awk '/abc|123/' filename # return for 'abc' or '123'. | --> or
FS = Input field separator value
OFS = Output field separator value
NF = Number of fields on the current line
NR = Number of records in the current file
RS = Record separator value
ORS = Output record separator
FILENAME = Current file name being processed and probably a few more
awk '{print NR}' filename # would print the line number for every line processed
## = grep -c
awk 'END{print  NR}' filename # Counts the lines in a file. similar to 'wc -l'
```

## pipline on awk

```bash
awk 'BEGIN{print "the start"};{print}; END{print "the end"}' filename
```

## Simple Logic
```bash
awk '{if(NR~/^2#/)print}' filename # would print line 2 from filename
awk '{if(NR~2)print}' filename # would print any line numbers contain 2 from filename
### 2, 12, 22, 32...
awk '{if(NR!~2)print}' filename # negated match
awk '{if(NR==2)print}' filename
awk '{if(NR!=2)print}' filename
```

## FS
```bash
awk '{FS="\t";print $6}' filename
or
awk -F"\t" '{print $6}' filename
awk -F"\t" 'NR==1,NR==10{print $6}' filename #print the cloum 6 from line 1 to line 10;
awk -F"\t" '{print  length($5)}' filename # length() function to count the
```

##Delete columns
```bash
awk '$1="";{print;OFS=\t}' FILENAME
```


## Conditions

```bash
awk '$3>10' FILENAME
```



## Deleted the line after calculation

the grammar `gawk` is much the same like `awk` but more flexible

To delete some lines which doesn't contain `Baeldung`
```bash
awk '!/Baeldung/' myfile.txt > tmpfile && mv tmpfile myfile.txt
```

To delete lines which the second column is larger than 0.5:
```bash
gawk -i inplace '$2>=0.5' file_name
```

## Turn one columns into few different rows

[RavinderSingh13, 2016](https://www.unix.com/shell-programming-and-scripting/265041-split-columns-into-rows.html)
From:
<pre>
10000|[12080000000]
10002|[13075200000]
10003|[13939200000]
10004|[1347200000,133600000,1152000000,106400000,12800000,117200000,145180000,1451000000,148400000,14240000]
10005|[16000000]
</pre>

To:
<pre>
PARTY|PART_DT
10000|12080000000
10002|13075200000
10003|13939200000
10004|1347200000
10004|133600000
10004|1152000000
10004|106400000
10004|12800000
10004|117200000
10004|145180000
10004|1451000000
10004|148400000
10004|14240000
10005|16000000
</pre>

```bash
awk -F"|" 'BEGIN{print "PARTY|PART_DT"} {gsub(/\[|\]/,X,$NF);num=split($NF, array,",");for(i=1;i<=num;i++){print $1 OFS array[i]}}' OFS="|"  Input_file
```

### Merge one column into three columns to reduce the row number
[kumaran_5555, 2011](https://www.unix.com/shell-programming-and-scripting/160974-how-convert-single-column-into-several-columns.html)

From
<pre>
AAA
BBB
CCC
DDD
EEE
FFF
GGG
HHH
III
</pre>

To
<pre>
AAA DDD GGG
BBB EEE HHH
CCC FFF III
</pre>

```bash
awk -v col=3 '{if(NR%col){printf "%s ",$0 }else {printf "%s\n",$0}} ' test.txt
```

[RudiC, 2019](https://www.unix.com/unix-for-beginners-questions-and-answers/283205-how-split-one-long-column-into-multiple-rows-3-each.html)
From
<pre>
A	value1
A	value2
A	value3
B	value1
B	value2
B	value3
C	value1
C	value2
C	value3
</pre>
To
<pre>
A	value1	value2	value3
B	value1	value2	value3
C	value1	value2	value3
</pre>

```bash
awk 'LAST != $1 {printf "%s%s", DL, $0; LAST = $1; DL = RS; next}; {printf "\t%s", $2} END {printf RS}' file
```

### Match to print

print the rows when the first column contains ','

From:
<pre>
123,1	123,1
123	1123,1
12,12	12314
1231	123123
</pre>

To:
<pre>
123,1	123,1
12,12	12314
</pre>

```bash
awk -F "\t" '$1 ~ /,/ {print}' file_name
```



## Calculation

### Sum of a column

Cite:[Ajo, 2015](https://stackoverflow.com/questions/28905083/how-to-sum-a-column-in-awk)
```bash
awk -F',' '{sum+=$57;} END{print sum;}' file.txt
```
### Mean of a column

Cite: [orges, 2010](https://stackoverflow.com/questions/3122442/how-do-i-calculate-the-mean-of-a-column)
```bash
awk '{ total += $3 } END { print total/NR }' file.name
```


## Print a column by match

<pre>
CHROM	X	A	B
1	1	1	1
1	2	2	2
</pre>
Let's say, I want first two columns and the column which names is "B":

<pre>
CHROM	X	B
1	1	1
1	2	2
</pre>

```bash
awk -v tmp=$(grep -i CHROM test.txt| tr '\t' '\n'| grep -wn B | awk -F: '{print $1}') '{OFS="\t"; print $1,$2,$tmp}' test.txt
```
