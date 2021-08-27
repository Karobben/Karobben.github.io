#!/bin/bash
pp=$(pwd)
echo $(date) > $pp/waque.log
for i in Bioinfor  Blog   LearnNotes  Linux  Python  R
do #echo cp layout.md $i/layout.md
# cp layout.md $i/layout.md
cd $i; pwd
echo uploading the files
waque.py -t ~/.yuqueToken -i * >> $pp/waque.log
cd ..
done
grep -v -E "導入|md is updated|updating for:|summary.md|layout.md|index.md|yuque.yml" $pp/waque.log|uniq
