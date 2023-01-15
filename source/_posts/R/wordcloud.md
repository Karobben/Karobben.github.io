---
title: "worldcloud"
description: "worldcloud"
url: worldcloud2
date: 2020/06/10
toc: true
excerpt: "Plot a Words Cloud "
tags: [R, WordCloud]
category: [R, Data]
cover: 'https://s1.ax1x.com/2022/05/02/OPKa36.png'
thumbnail: 'https://s1.ax1x.com/2022/05/02/OPKa36.png'
priority: 10000
---

## worldcloud


There are some online service you can use (last check: 2022/05/01):
- [wordclouds.com](https://www.wordclouds.com/)
- [monkeylearn.com](https://monkeylearn.com/word-cloud/)
- [mentimeter.com](https://www.mentimeter.com/features/word-cloud)

Codes for Word Clouds:
- [wordcloud2 documentation](https://cran.r-project.org/web/packages/wordcloud2/vignettes/wordcloud.html)

Word Clouds or tag clouds are graphic presentations that could present the frequency of the words in a photo. Basically, the size of the word has connected to the frequency of the word. The color was randomly assigned for giving a clear boundary for each word. It could be used as a graphic abstract of a single paper, or present the recent frequent-talked topics in a shocking way.

In R, we can use split the words by space. But for other languages like Chinese, we can use library jiebaR to do the segmentation. In English, we’d also clean the results by deleting some “none-sense” words like “am”, “is”, and “are”.

PS: for some reason, I can’t change the shape of the word cloud based on the image I was given. The example from the documentation also failed, too. So, I’ll try to achieve the result by using python. ([The codes for python(https://karobben.github.io/2020/06/23/Python/wordcloud/))

## Talk is cheap, show me the code

Reference: [Céline Van den Rul; 2019](https://towardsdatascience.com/create-a-word-cloud-with-r-bde3e7422e8a)

```r
library(RColorBrewer)
library(tm)
library(wordcloud2)
library(tidyr)

## Read from file
# text <- readLines("")

text <- c("Word Clouds or tag clouds are graphic presentation which could present the frequency of the words in a photo. Basically, the size of the word is connected the frequency of the word. Color was random assigned for given a clear boundary of each word. It could be used as a graphic abstract of single paper, or present the recent frequent-talked topics in a shock way.
In R, we can use split the words by space. But for other language like Chinese, we can use library `jiebaR` to do the segmentation. In English, we'd also clean the results by delete some 'none-sense' words like 'am', 'is', 'are'.")  # past whatever you want in here

# Create the doc for texts
docs <- Corpus(VectorSource(text))
docs <- docs %>%
  tm_map(removeNumbers) %>%
  tm_map(removePunctuation) %>%
  tm_map(stripWhitespace)
docs <- tm_map(docs, content_transformer(tolower))
docs <- tm_map(docs, removeWords, stopwords("english"))

# Create the matrix
dtm <- TermDocumentMatrix(docs)
matrix <- as.matrix(dtm)
words <- sort(rowSums(matrix),decreasing=TRUE)
df <- data.frame(word = names(words),freq=words)

set.seed(1234) # for reproducibility
wordcloud2(df,color="random-light",backgroundColor = 'black')
```

## More Ancient codes

Those codes are recorded before 2020. So, they may not works very well.

```r
library(SnowballC)
library(Rwordseg)
library(wordcloud2)
library(tm)

A <- c("Large scale gene expression profiling during intestine and body wall regeneration in the sea cucumber Apostichopus japonicus")  # past whatever you want in here

##读入分词文件
word = lapply(X = A, FUN = strsplit, "\\s")
word <- wordStem(word[[1]])
word1=unlist(word)


##'''统计词频'''
df=table(word1)
df=sort(df,decreasing = T)

df1 = data.frame(word = names(df), freq = df)
df2 = data.frame(word = names(df), freq = df)

Dele_list = c("al.,", "#", "was", "a", "The", "et", "were", "that", "is", "on", "are", "this", "as", "in","been", "have", "has", "the", "and", "of", "to", "for", "with")
df2[-which(df2$word == "has"),] -> df2
wordcloud2(df2,color="random-light",backgroundColor = 'black')


####For multy English files

library(wordcloud2)
library(tm)

##packageDescription('tm')
txt <- system.file("texts/txt",package="tm")
##导入动态coporus
myData <- Corpus(DirSource(txt),readerControl=list(language="en"))
myData <- tm_map(myData,removePunctuation)
myData <- tm_map(myData,function(x)removeWords(x,stopwords()))
tdm <- TermDocumentMatrix(myData)
m <- as.matrix(tdm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word=names(v),freq=v)
wordcloud(d$word,d$freq,random.order=FALSE,color=brewer.pal(8,"Dark2"))
wordcloud2(d,color="random-light",backgroundColor = 'black',size=0.7)


####For Chinese files

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



## save as Html
library(htmlwidgets)
saveWidget(WC,"1.html",selfcontained = F)

```

```r


A <- readLines('test.txt')

Result = ""
for(i in A){
        Result = paste(Result,i,sep=" ")}

## Remove punctuations＆Numbers 去标点&数字
Result = gsub("[[:punct:]]|[[:digit:]]|^http:\\/\\/.*|^https:\\/\\/.*"," ",Result)

word = lapply(X = Result, FUN = strsplit, "\\s")
word1=word[[1]][[1]]

df=table(word1)
df=sort(df,decreasing = T)

TB = data.frame(t(t(df)))[c(1,3)]
head(TB)                                                                                                  
##  word1 Freq
##1        243
##2   the   67
##3     I   51
##4    to   42
##5   and   38
##6    my   32

wordcloud2(TB,color="random-light",backgroundColor = 'black')
```

![image.png](https://s1.ax1x.com/2022/05/02/OPKa36.png)
