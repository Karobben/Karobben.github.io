---
url: awk2
---

# awk 语言基础


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
# = grep -c
awk 'END{print  NR}' filename # Counts the lines in a file. similar to 'wc -l'
```

# pipline on awk

```bash
awk 'BEGIN{print "the start"};{print}; END{print "the end"}' filename
```

# Simple Logic
```bash
awk '{if(NR~/^2#/)print}' filename # would print line 2 from filename
awk '{if(NR~2)print}' filename # would print any line numbers contain 2 from filename
## 2, 12, 22, 32...
awk '{if(NR!~2)print}' filename # negated match
awk '{if(NR==2)print}' filename
awk '{if(NR!=2)print}' filename
```

# FS
```bash
awk '{FS="\t";print $6}' filename
or
awk -F"\t" '{print $6}' filename
awk -F"\t" 'NR==1,NR==10{print $6}' filename #print the cloum 6 from line 1 to line 10;
awk -F"\t" '{print  length($5)}' filename # length() function to count the
```

#Delete columns
```bash
awk '$1="";{print;OFS=\t}' FILENAME
```
