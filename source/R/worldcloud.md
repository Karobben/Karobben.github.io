---
title: "worldcloud"
description: "worldcloud"
url: worldcloud2
---
# worldcloud


```r
library(SnowballC)
library(Rwordseg)
library(wordcloud2)
library(tm)

A <- c("Large scale gene expression profiling during intestine and body wall regeneration in
the sea cucumber Apostichopus japonicus")  # past whatever you want in here

#读入分词文件
word = lapply(X = A, FUN = strsplit, "\\s")
word <- wordStem(word)
word1=unlist(word)


#'''统计词频'''
df=table(word1)
df=sort(df,decreasing = T)

df1 = data.frame(word = names(df), freq = df)

  df1[-which(df1$word == "al.,"),] -> df2
  df2[-which(df2$word == "#"),] -> df2
  df2[-which(df2$word == "was"),] -> df2
  df2[-which(df2$word == "a"),] -> df2
  df2[-which(df2$word == "The"),] -> df2
  df2[-which(df2$word == "et"),] -> df2
  df2[-which(df2$word == "were"),] -> df2
  df2[-which(df2$word == "that"),] -> df2
  df2[-which(df2$word == "is"),] -> df2
  df2[-which(df2$word == "on"),] -> df2
  df2[-which(df2$word == "are"),] -> df2
  df2[-which(df2$word == "this"),] -> df2
  df2[-which(df2$word == "as"),] -> df2
  df2[-which(df2$word == "in"),] -> df2
  df2[-which(df2$word == "been"),] -> df2
  df2[-which(df2$word == "have"),] -> df2
  df2[-which(df2$word == "has"),] -> df2
   df2[-which(df2$word == "the"),] -> df2
   df2[-which(df2$word == "and"),] -> df2
   df2[-which(df2$word == "of"),] -> df2
   df2[-which(df2$word == "to"),] -> df2
   df2[-which(df2$word == "for"),] -> df2
   df2[-which(df2$word == "with"),] -> df2
wordcloud2(df2,color="random-light",backgroundColor = 'black')


###For multy English files

library(wordcloud2)
library(tm)

#packageDescription('tm')
txt <- system.file("texts/txt",package="tm")
#导入动态coporus
myData <- Corpus(DirSource(txt),readerControl=list(language="en"))
myData <- tm_map(myData,removePunctuation)
myData <- tm_map(myData,function(x)removeWords(x,stopwords()))
tdm <- TermDocumentMatrix(myData)
m <- as.matrix(tdm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word=names(v),freq=v)
wordcloud(d$word,d$freq,random.order=FALSE,color=brewer.pal(8,"Dark2"))
wordcloud2(d,color="random-light",backgroundColor = 'black',size=0.7)


###For Chinese files

library(jiebaR)
f <- scan('test' ,sep='\n',what='',encoding="GBK")
seg <- qseg[f] #使用qseg类型分词，并把结果保存到对象seg中
seg <- seg[nchar(seg)>1] #去除字符长度小于2的词语
seg <- table(seg) #统计词频
seg <- seg[!grepl('[0-9]+',names(seg))] #去除数字
seg <- seg[!grepl('a-zA-Z',names(seg))] #去除字母
length(seg) #查看处理完后剩余的词数
seg <- sort(seg, decreasing = TRUE)[1:100] #降序排序，并提取出现次数最多的前100个词语
seg #查看100个词频最高的
View(seg)
data=data.frame(seg)
data
wordcloud(data$seg , data$Freq, colors = rainbow(100), random.order=F)
x11()
dev.off()



# save as Html
library(htmlwidgets)
saveWidget(WC,"1.html",selfcontained = F)

```

```r


A <- readLines('test.txt')

Result = ""
for(i in A){
        Result = paste(Result,i,sep=" ")}

# Remove punctuations＆Numbers 去标点&数字
Result = gsub("[[:punct:]]|[[:digit:]]|^http:\\/\\/.*|^https:\\/\\/.*"," ",Result)

word = lapply(X = Result, FUN = strsplit, "\\s")
word1=word[[1]][[1]]

df=table(word1)
df=sort(df,decreasing = T)

TB = data.frame(t(t(df)))[c(1,3)]
head(TB)                                                                                                  
#  word1 Freq
#1        243
#2   the   67
#3     I   51
#4    to   42
#5   and   38
#6    my   32

wordcloud2(TB,color="random-light",backgroundColor = 'black')
```

![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1582556564473-629627e2-e9e8-4985-802a-655a302a9713.png#align=left&display=inline&height=309&name=image.png&originHeight=309&originWidth=470&size=73870&status=done&style=none&width=470)



---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
