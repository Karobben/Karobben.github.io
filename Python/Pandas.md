---
url: pandas
---

# Pandas


```python
import pandas as pd

##read file

TB = pd.read_csv("sentence-G",sep='\t', names=None, header=None)
TB.columns = ['频率', '', 'V2', '词义', 'V3']

#DataFrame
pd.DataFrame(index=range(40),columns=['a', 'b'])

## rsult output
TB.to_csv("table",sep='\t')

data
data[0:2]       #取前两行数据

len(data )              #求出一共多少行
data.columns.size      #求出一共多少列
data.columns        #列索引名称
data.index       #行索引名称

data.ix[1]                #取第2行数据
data.iloc[1]             #取第2行数据
data.loc['A']      #取第行索引为”A“的一行数据，
data['x']      #取列索引为x的一列数据

data.loc[:,['x','z'] ]          #表示选取所有的行以及columns为a,b的列；
data.loc[['A','B'],['x','z']]     #表示选取'A'和'B'这两行以及columns为x,z的列的并集；
data.iloc[1:3,1:3]              #数据切片操作，切连续的数据块
data.iloc[[0,2],[1,2]]              #即可以自由选取行位置，和列位置对应的数据，切零散的数据块

data[data>2]       #表示选取数据集中大于0的数据
data[data.x>5]       #表示选取数据集中x这一列大于5的所有的行
a1=data.copy()
a1[a1['y'].isin(['6','10'])]    #表显示满足条件：列y中的值包含'6','8'的所有行。

data.mean()           #默认对每一列的数据求平均值；若加上参数a.mean(1)则对每一行求平均值；
data['x'].value_counts()    #统计某一列x中各个值出现的次数：
data.describe() #对每一列数据进行统计，包括计数，均值，std，各个分位数等。
data.to_excel(r'E:\pypractice\Yun\doc\2.xls',sheet_name='Sheet1')  #数据输出至Exceldata[0:2]       #取前两行数据





## from Dictionary to DataFrame
TB = pd.Series(BB)


## DataFrame sort
TB = TB.sort_values(ascending=False)


## DataFrame merge
result = pd.concat([ Word, Sen], axis=1, sort=False)


## NaN drap

data.dropna(thresh=3) # at least 3 data we have

```

