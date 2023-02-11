---
title: "语雀AIP 配置和简单使用"
description: "语雀AIP 配置和简单使用"
url: fl7dmh
date: 2020/06/26
toc: true
excerpt: "语雀AIP 配置和简单使用"
tags: [Hexo, Yuque, Waque, MarkDown]
category: [others, Blog, Yuque]
cover: 'https://s1.ax1x.com/2020/06/26/NsAkdI.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NsAkdI.png'
priority: 10000
---

## 语雀AIP 配置和简单使用

<a name="wC8XQ"></a>
## 1. 设置 TOKEN号
进入[个人设置](https://www.yuque.com/settings) , <br />
![NsAkdI.png](https://s1.ax1x.com/2020/06/26/NsAkdI.png)
<br />Terminal 内 输入  
```bash
curl -H "X-Auth-Token: 你的token " https://www.yuque.com/api/v2/hello
```

```python
import requests
url = "https://www.yuque.com/api/v2/repos/646554/docs/"
header = {"X-Auth-Token":""}

## Read the list of the repos
Result = requests.get(url, headers = header).json()

## post a passage in this repos

requests.post(url, headers = header).json()
```
返回:

```bash
{"data":{"message":"Hello Karroben"}}
```

<a name="IwjFB"></a>
## 2. 获取用户信息:
`https://www.yuque.com/yuque/developer/user`

官方例子:

```bash
GET /users/:login
## 或
GET /users/:id
```
说明: GET = curl -H "X-Auth-Token: 你的token " `https://www.yuque.com/api/v2`  这一串

**使用方法**:
把`https://www.yuque.com/api/v2/hello` 的 hello 去掉
加上users/, 再加上你的ID 
```bash
curl -H "X-Auth-Token: 你的token " https://www.yuque.com/api/v2/users/liuwenkan
```

返回:
```bash
{"data":
  {"id":691897,
    "type":"User",
    "space_id":0,
    "account_id":494138,
    "login":"liuwenkan",
    "name":"Karroben",
    "avatar_url":"https://cdn.nlark.com/yuque/0/2019/jpeg/anonymous/1576914522864-5dabd37e-9a90-4ee4-96b4-a1973dbcede4.jpeg",
    "books_count":8,
    "public_books_count":8,
    "followers_count":1,
    "following_count":2,
    "public":1,
    "description":"R 语言作图索引:https://karobben.github.io/R/R-index.html",
    "created_at":"2019-12-21T07:49:03.000Z","updated_at":"2020-02-14T02:57:36.000Z",
    "_serializer":"v2.user_detail"
  }
}
```

<a name="PPUvP"></a>
## 3. 获取repository信息
[https://www.yuque.com/yuque/developer/repo](https://www.yuque.com/yuque/developer/repo)

```bash
## for User
GET /users/:login/repos
## for Group
GET /groups/:login/repos

## 或
GET /users/:id/repos
GET /groups/:id/repos
```

一样, Get = 前面一大串

例子:

```bash
curl -H "X-Auth-Token: 你的token " https://www.yuque.com/api/v2/repos/liuwenkan/python
```

返回太多, 不在这里赘述


## Post a passage

Example for post a Non-title passage
```bash
curl -v -X POST test.md -H "${Your Token}" https://www.yuque.com/api/v2/repos/646554/docs/
```
