---
toc: true
url: dbscan
covercopy: © Karobben
priority: 10000
date: 2021-11-06 15:48:47
title: "A quick guide for seaborn plot in python"
ytitle: "A quick guide for seaborn plot in python"
description: "A quick guide for seaborn plot in python"
excerpt: "A quick guide for seaborn plot in python"
tags: [Statistic, Plot, Python]
category: [Python, Plot]
cover: "https://www.statology.org/wp-content/uploads/2021/04/seabornTitle3-768x587.png"
thumbnail: "https://www.statology.org/wp-content/uploads/2021/04/seabornTitle3-768x587.png"
---

## Searborn

```python
import seaborn as sns
```

### Countplot

source: [seaborn.pydata.org](https://seaborn.pydata.org/generated/seaborn.countplot.html)

```python
import seaborn as sns

sns.set_theme(style="darkgrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x="class", data=titanic)

```
## Title

[](https://www.statology.org/seaborn-title/)

```python
fig, ax = plt.subplots()
ax.set(title='Points vs. Assists')

# or
ax.set_title("Title",fontsize=50)
```

|![](https://www.statology.org/wp-content/uploads/2021/04/seabornTitle3-768x587.png)|
|:-:|
|[© Zach; 2021](https://www.statology.org/seaborn-title/)|

## Axis

### Axis text rotation

```python
fig, ax = plt.subplots()
ax.set_xticklabels(ax.get_xticklabels(),rotation = 30)
```

|![](https://www.delftstack.com/img/Seaborn/seaborn%20rotate%20labels%202.png?ezimgfmt=rs:828x513/rscb5/ng:webp/ngcb5)|
|:-:|
|[© delftstack; 2021](https://www.delftstack.com/howto/seaborn/rotate-tick-labels-seaborn/)|

### Labels

Reference: [armatita; 2016](https://stackoverflow.com/questions/36220829/fine-control-over-the-font-size-in-seaborn-plots-for-academic-papers)

```python
fig, ax = plt.subplots()
ax.set_xlabel("X Label",fontsize=30)
```

|![](https://i.stack.imgur.com/8Uy45.png)|
|:-:|
|[© armatita; 2016](https://stackoverflow.com/questions/36220829/fine-control-over-the-font-size-in-seaborn-plots-for-academic-papers)|

### Limits

```python
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
```

## Ledgend

### remove

```python
# works on parts of plot
sns.scatterplot(y  = s_y, x = s_x, hue = cat, legend = False)


# using function from matplotlib
plt.legend([],[], frameon=False)
```
