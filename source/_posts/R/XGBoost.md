---
title: "XGBoost (out of date)"
description: "XGBoost (out of date)"
url: xgboost
date: 2020/01/22
toc: true
excerpt: "XGBoost codes"
category: [R, Data, Machine Learning]
cover: 'https://www.r-project.org/Rlogo.png'
thumbnail: 'https://www.r-project.org/Rlogo.png'
priority: 10000
---

## XGBoost (out of date)


```r
library(xgboost)
library(tidyverse)
library(modelr)

 a <- read_csv("melb_data.csv")
 a <- na.omit(a)

### Data

a <- select(TR,-starts_with("Address"))
Suburb <- model.matrix(~Suburb-1,a)
Type <- model.matrix(~Type-1,a)
Method <- model.matrix(~Method-1,a)
SellerG <- model.matrix(~SellerG-1,a)
CouncilArea <- model.matrix(~CouncilArea-1,a)
Regionname <- model.matrix(~Regionname-1,a)
aa <- data.frame(a,Suburb=Suburb, Type=Type,Method=Method,SellerG=SellerG, CouncilArea=CouncilArea,Regionname=Regionname)

### Split data to tow groups
splitData <- resample_partition(aa, c(test = 0.3, train = 0.7))
 TR <- data.frame(splitData$train)
 TT <- data.frame(splitData$test)
##or
set.seed(1234)
diseaseInfo <- diseaseInfo[sample(1:nrow(diseaseInfo)), ]
##random arrage the data and grep apart of it to different groups

### RM predict target and build target list
 TR_Labels <- TR$Price
 TT_Labels <- TT$Price
 TR <-  select(TR,-starts_with("Price"))
 TT <-  select(TT,-starts_with("Price"))
 TR <- data.matrix(TR)
 TT <- data.matrix(TT)

dtrain <- xgb.DMatrix(data = TR, label= TR_Labels)
dtest <- xgb.DMatrix(data = TT, label= TT_Labels)

TB <- data.frame( mean=m)

model <- xgboost(data = dtrain,nround = 3000)

 pred <- predict(model, dtest)
 mean <- (pred-TT_Labels)/TT_Labels
 mean[which(mean<0)] <- mean[which(mean<0)]*(-1)
 m <- mean(mean)

mean(as.numeric(pred > 0.5) != TT_Labels)

predict(model,dtest)

##for(i in 1){
##  model <- xgboost(data = dtrain,nround = i)
##  pred <- predict(model, dtest)
##  mean <- (pred-TT_Labels)/TT_Labels
##  mean[which(mean<0)] <- mean[which(mean<0)]*(-1)
##  m <- mean(mean)
## TB <- rbind(TB,m)
## }


library(xgboost)
library(tidyverse)

diseaseInfo <- read_csv("Outbreak_240817.csv")
set.seed(1234)
diseaseInfo <- diseaseInfo[sample(1:nrow(diseaseInfo)), ]
head(diseaseInfo)
diseaseInfo_humansRemoved <- diseaseInfo %>%
    select(-starts_with("human"))
diseaseLabels <- diseaseInfo %>%
    select(humansAffected) %>% # get the column with the # of humans affected
    is.na() %>% # is it NA?
    magrittr::not() # switch TRUE and FALSE (using function from the magrittr package)

## check out the first few lines
head(diseaseLabels) # of our target variable
head(diseaseInfo$humansAffected) # of the original column
diseaseInfo_numeric <- diseaseInfo_humansRemoved %>%
    select(-Id) %>% # the case id shouldn't contain useful information
    select(-c(longitude, latitude)) %>% # location data is also in country data
    select_if(is.numeric) # select remaining numeric columns

## make sure that our dataframe is all numeric
str(diseaseInfo_numeric)
model.matrix(~country-1,head(diseaseInfo))
region <- model.matrix(~country-1,diseaseInfo)
head(diseaseInfo$speciesDescription)
diseaseInfo_numeric$is_domestic <- str_detect(diseaseInfo$speciesDescription, "domestic")

speciesList <- diseaseInfo$speciesDescription %>%
    str_replace("[[:punct:]]", "") %>% # remove punctuation (some rows have parentheses)
    str_extract("[a-z]*$") # extract the least word in each row

## convert our list into a dataframe...
speciesList <- tibble(species = speciesList)

## and convert to a matrix using 1 hot encoding
options(na.action='na.pass') # don't drop NA values!
species <- model.matrix(~species-1,speciesList)

diseaseInfo_numeric <- cbind(diseaseInfo_numeric, region, species)
diseaseInfo_matrix <- data.matrix(diseaseInfo_numeric)

## get the numb 70/30 training test split
numberOfTrainingSamples <- round(length(diseaseLabels) * .7)

## training data
train_data <- diseaseInfo_matrix[1:numberOfTrainingSamples,]
train_labels <- diseaseLabels[1:numberOfTrainingSamples]

## testing data
test_data <- diseaseInfo_matrix[-(1:numberOfTrainingSamples),]
test_labels <- diseaseLabels[-(1:numberOfTrainingSamples)]

dtrain <- xgb.DMatrix(data = train_data, label= train_labels)
dtest <- xgb.DMatrix(data = test_data, label= test_labels)

model <- xgboost(data = dtrain, # the data   
                 nround = 2, # max number of boosting iterations
                 objective = "binary:logistic")  # the objective function

pred <- predict(model, dtest)

## get & print the classification error
err <- mean(as.numeric(pred > 0.5) != test_labels)
print(paste("test-error=", err))

model_tuned <- xgboost(data = dtrain, # the data           
                 max.depth = 3, # the maximum depth of each decision tree
                 nround = 2, # max number of boosting iterations
                 objective = "binary:logistic") # the objective function

## generate predictions for our held-out testing data
pred <- predict(model_tuned, dtest)

## get & print the classification error
err <- mean(as.numeric(pred > 0.5) != test_labels)
print(paste("test-error=", err))


## get the number of negative & positive cases in our data
negative_cases <- sum(train_labels == FALSE)
postive_cases <- sum(train_labels == TRUE)

## train a model using our training data
model_tuned <- xgboost(data = dtrain, # the data           
                 max.depth = 3, # the maximum depth of each decision tree
                 nround = 10, # number of boosting rounds
                 early_stopping_rounds = 3, # if we dont see an improvement in this many rounds, stop
                 objective = "binary:logistic", # the objective function
                 scale_pos_weight = negative_cases/postive_cases) # control for imbalanced classes

## generate predictions for our held-out testing data
pred <- predict(model_tuned, dtest)

## get & print the classification error
err <- mean(as.numeric(pred > 0.5) != test_labels)
print(paste("test-error=", err))

## train a model using our training data
model_tuned <- xgboost(data = dtrain, # the data           
                 max.depth = 3, # the maximum depth of each decision tree
                 nround = 10, # number of boosting rounds
                 early_stopping_rounds = 3, # if we dont see an improvement in this many rounds, stop
                 objective = "binary:logistic", # the objective function
                 scale_pos_weight = negative_cases/postive_cases, # control for imbalanced classes
                 gamma = 1) # add a regularization term

## generate predictions for our held-out testing data
pred <- predict(model_tuned, dtest)

## get & print the classification error
err <- mean(as.numeric(pred > 0.5) != test_labels)
print(paste("test-error=", err))

xgb.plot.multi.trees(feature_names = names(diseaseInfo_matrix),
                     model = model)
```
