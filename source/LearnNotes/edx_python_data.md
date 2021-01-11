---
title: "Python for Data Science"
date: "2020/12/28"
description: "Class Notes of Python for Data Science from Edx"
url: edx_python_data
---

# Python for Data Science

**Insight**:

Data + Analysis & Question -> Insight
build model, solving problems

Exp: Amazon recommendation new books to customers by their reading records

Prediction: take actions by the weather forecast.

Why data science arise recently:
  - big Data
  - High performance of circulates

Megabytes -> Gigabytes -> Terabytes -> Petabytes ->  Exabytes -> Zettabyte

# Week 1

## Why is python
- Easy-to-read and learn
- Vibrant community
- Growing and evolving set of libraries
  - Data management
  - Analytical processing
  - Visualization
- Applicable to each step in the data science process
- Notebooks


## Exp 1, Soccer Data Analysis: Feature Selection

Five steps of Data processing:
Acquire:
  - Import raw data into your platform
Prepare:
  - Explore & Visualization
Analysis:
  - Feature Selection
  - Model
  - Analyze the results
report:
  - Resent your findings
Act:
  - Use then


## Acquire
Database
|Text File|Online data|Data Cleaning|
|--|--|--|
|- Relational<br>- Non-relational|- Twitter<br>- Sensor|- Missing<br>- Garbage<br>- NULLs|


**Data Visualization**:
  - Catch your attention and convey your message in a minimal time


## Prepare
<table>
<tr><th>Exploring Data</th><th>Visualization</th><th>Pre-processing</th><th>Getting data in shape</th></tr>
<tr><td>

  - correlation; general trends, Outliers
  - Statistic
</td>
<td>

  - heatmap: Distribution;
  - Histogram: trends;
  - boxplot: trends
  - Line Graphs: Time serial;
  - Scatter plots: Correlation;
</td>
<td>

  - Clean & Transform
  - remove; merge; estimate
  - remove outliers
</td>
<td>

  - scaling: (normalization)
    - aggregation
  - feature selection
  - Dimension reduction
  - Data Manipulation
</td>
</tr>
</table>

## Analyze Data
- Classification: Predict category
- Regression: Predict numeric value
- Clustering: Organize similar items or groups (Target marketing)
- Graph Analytics: find connections between entities (social networks)
- Association Analysis: capture associations between items (Customers' purchase behavior)

Select technique -> Build model -> validate model

### Evaluation of Results
Predicted *vs* Correct

## Reporting
What to present:
Main results; Value; Model leading to Act


Visualization tools:
R; Python;
JS: D3; Developers; Tableau; Timeline

## Action
Turning Insight into Action

# Week2
Python is dynamic typing:
Object means it could easily turn int to float.
