#!/usr/bin/env bash
for i in $(head -n 2 $1/*.md| grep url| awk -F: '{print $2}'|sed 's/^ /(/;s/$/)/');
do SUM=$(cat $1/summary.md)
Num=$(grep -ciw $i $1/summary.md)
if [[ $Num == 0 ]]
then
  echo $i
  grep -w "url: $(echo $i|sed 's/[()]//g')" $1/*.md| awk -F":" '{print $1}'|awk -F"//" '{print $2}'
fi
done
