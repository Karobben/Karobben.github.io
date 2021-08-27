---
title: "Machine Learning (out of date)"
description: "Machine Learning (out of date)"
url: ml
date: 2020/08/20
toc: true
excerpt: "Some machine learning codes for R"
tags: [R, Machine Learning]
category: [R, Data, Machine Learning]
cover: 'https://s1.ax1x.com/2020/08/21/dYctdf.png'
thumbnail: 'https://s1.ax1x.com/2020/08/21/dYctdf.png'
priority: 10000
---

## Machine Learning (out of date)


```r

library(tidyverse)
library(rpart)
library(randomForest)
a <- read_csv("../input/melb_data.csv")

## train a decision tree based on our dataset
fit <- rpart(Price ~ Rooms + Bathroom + Landsize + BuildingArea + YearBuilt + Lattitude + Longtitude, data = a)

plot(fit, uniform=TRUE) +text(fit, cex=1.6)
print(head(melbourne_data))
print(predict(fit, head(melbourne_data)))
print(head(melbourne_data$Price))

##### Train and Test

library(modelr)
mae(model = fit, data = a)

splitData <- resample_partition(a, c(test = 0.3, train = 0.7))
lapply(splitData, dim)

fit2 <- rpart(Price ~ Rooms + Bathroom + Landsize + BuildingArea + YearBuilt + Lattitude + Longtitude, data = splitData$train)

mae(model = fit2, data = splitData$test)

#####Built function
get_mae <- function(maxdepth, target, predictors, training_data, testing_data)
{
predictors <- paste(predictors, collapse="+")
formula <- as.formula(paste(target,"~",predictors,sep = ""))
model <- rpart(formula, data = training_data,control = rpart.control(maxdepth = maxdepth))
mae <- mae(model, testing_data)
return(mae)
}

target <- "Price"
predictors <-  c("Rooms","Bathroom","Landsize","BuildingArea","YearBuilt","Lattitude","Longtitude")

for(i in 1:10)
{
   mae <- get_mae(maxdepth = i, target = target, predictors = predictors, training_data = splitData$train, testing_data = splitData$test)
   print(glue::glue("Maxdepth: ",i,"\t MAE: ",mae))
}



#####MODEL with training and repair
model <- rpart(formula, data = splitData$train ,control = rpart.control(maxdepth = 5))

```
