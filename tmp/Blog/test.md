---
title: "无标题"
description: "无标题"
url: cbvwhq
---

# 无标题

<!doctype html><div data-lake-element="root" class="lake-engine lake-typography-traditional" data-parser-by="lake2html"></div>



```flow
st=>start: Start
e=>end
op1=>operation: My Operation
sub1=>subroutine: My Subroutine
cond=>condition: Yes or No?
io=>inputoutput: catch something...
para=>parallel: parallel tasks

st->op1->cond
cond(yes)->io->e
cond(no)->para
para(path1, bottom)->sub1(right)->op1
para(path2, top)->op1
```
