---
title: "Covid: nCov Data by Python"
description: "Covid: nCov Data by Python"
url: ncov_python
date: 2020/07/28
toc: true
excerpt: "nCov Data visualizing by Python"
tags: [Plot, nCov, Python]
category: [Python, API]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
covercopy: '© getcodify.com'
---

## Covid: nCov Data by Python

[Websites](https://pypi.org/project/covid)
## Intsall
```bash
pip install Covid
```

Python package to get information regarding the novel corona virus provided by <span style="background:salmon">**Johns Hopkins university**</span> and <span style="background:salmon">**worldometers.info**</span>

## 1. John Hopkins University API

優點：
  有經緯度信息，方便畫地圖
缺點：
  國內鏈接速度較慢
### Get All Data
```python
from covid import Covid

covid = Covid()
covid.get_data()
```
理論上你將獲得：
```
[
    {
        'id': '53',
        'country': 'China',
        'confirmed': 81020,
        'active': 9960,
        'deaths': 3217,
        'recovered': 67843,
        'latitude': 30.5928,
        'longitude': 114.3055,
        'last_update': 1584097775000
    },
    {...
```
實際上：
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.7/site-packages/covid/john_hopkins/covid.py", line 137, in get_data
    return [CovidModel(**case["attributes"]).dict() for case in cases]
  File "/usr/local/lib/python3.7/site-packages/covid/john_hopkins/covid.py", line 137, in <listcomp>
    return [CovidModel(**case["attributes"]).dict() for case in cases]
  File "pydantic/main.py", line 338, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for CovidModel
Recovered
  none is not an allowed value (type=type_error.none.not_allowed)
```
不過並不影響你獲取單個國際或地區的數據：
### Get Data by Country

```python
italy_cases = covid.get_status_by_country_id(115)
```

```
{
    'id': '115',
    'country': 'Italy',
    'confirmed': 24747,
    'active': 20603,
    'deaths': 1809,
    'recovered': 2335,
    'latitude': 41.8719,
    'longitude': 12.5674,
    'last_update': 1584318130000
}
```
國家編號獲取：
```python
countries = covid.list_countries()
```
```
[{'id': '18', 'name': 'US'}, {'id': '22', 'name': 'Brazil'},...
```

### Other Datas
```python
##Get Total Active cases
active = covid.get_total_active_cases()
##Get Total Confirmed cases
confirmed = covid.get_total_confirmed_cases()
##Get Total Recovered cases
recovered = covid.get_total_recovered()
##Get Total Deaths
deaths = covid.get_total_deaths()
```

## 2. Worldometers.info

速度快，但是沒有經緯度信息
```python
covid = Covid(source="worldometers")
##Get Data
covid.get_data()
```
```
[{'country': 'North America', 'confirmed': 2258033, 'new_cases': 4166, 'deaths': 135128, 'rec...
```

## 畫圖

因爲種種原因- - 我放棄使用python了，
還是用R的ggplot的好。 哼哼 =  =

### 1. 數據獲取
```python
from covid import Covid

covid = Covid()
countries = covid.list_countries()
covid.get_status_by_country_id(int(countries[0]['id']))

## 多線程快速獲取
import multiprocessing as mp

def worker(i, return_dict):
  '''worker function'''
  Result = covid.get_status_by_country_id(int(countries[i]['id']))
  return_dict[Result] = Result
  print(Result)



def multicore(Pool=10):
  pool = mp.Pool(processes=Pool)
  #return_dict = manager.dict()
  for i in range(10):
    # Working function "echo" and the arg 'i'
    multi_res = [pool.apply_async(worker,(i,return_dict))]
  pool.close()
  pool.join()


if __name__ == '__main__':
  manager = mp.Manager()
  return_dict = manager.dict()
  jobs = []
  Num = 0
  for i in range(10):
    Num +=1
    print (Num)
    p = mp.Process(target=worker, args=(i,return_dict))
    jobs.append(p)
    p.start()
  for proc in jobs:
    proc.join()
```
 = =

 放棄了- - 太慢了
