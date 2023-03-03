---
title: "百度统计 API"
description: "百度统计 API"
url: egavw6
date: 2020/07/28
toc: true
excerpt: "百度统计是百度公司推出的网站分析工具，可以帮助网站管理员深入了解网站的流量、访问者行为、来源和趋势等数据。用户可以通过在网站中添加代码，收集并分析访问数据，从而优化网站运营和提高用户体验。百度统计提供了丰富的分析工具和数据可视化功能，让用户轻松地获取并理解网站数据。"
tags: [API, Web, Python]
category: [Python, API]
cover: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/030ce942338c4772b4edd8ec75957488~tplv-k3u1fbpfcp-zoom-crop-mark:892:892:892:502.awebp?'
covercopy: '© 百度统计'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## 百度统计 API

详细介绍:<br />[https://tongji.baidu.com/api/manual/Chapter2/openapi.html](https://tongji.baidu.com/api/manual/Chapter2/openapi.html)

<a name="WjQRg"></a>
## 1. 登录[百度开发者中心控制台](http://developer.baidu.com/console#app/project),获取code
将
```html
http://openapi.baidu.com/oauth/2.0/authorize?response_type=code&
  client_id={CLIENT_ID}&
  redirect_uri={REDIRECT_URI}&
  scope=basic&display=popup
```

按照对应关系

```bash
设置信息       对应参数
API Key      {CLIENT_ID}
Secret Key   {CLIENT_SECRET}
回调URI       {REDIRECT_URI}
```

填入对应信息

注意:     1."{}" **不能保留, 直接删掉**. 我之前卡了好久, 就是因为没有删去中括号.<br />2.REDIRECT_URI 建议使用活网站, 不然跳转的时候, 会等很久很久.<br />然后直接黏贴在浏览器里,便可<br />Example:
```html
http://openapi.baidu.com/oauth/2.0/authorize?response_type=code&
  client_id=m2OY4t4oBs59XG2Sasdads&
  redirect_uri=https://www.baidu.com&
  scope=basic&display=popup
```

第一次会显示登录的信息, 登陆后,会跳转到你的REDIRECT_URI. 死网站则会是空白页面. 这时候, 查看地址![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1582598175959-edffed6e-c5a6-4017-a43a-067c2dc14558.png#align=left&display=inline&height=167&name=image.png&originHeight=167&originWidth=527&size=20227&status=done&style=none&width=527)<br />后面会多出一个 ?code=XXXXXX<br />**这个code很重要**.<br />

<a name="Fzaon"></a>
## 2. 获取 token

```html
http://openapi.baidu.com/oauth/2.0/token?grant_type=authorization_code&
  code={CODE}&
  client_id={CLIENT_ID}&
  client_secret={CLIENT_SECRET}&
  redirect_uri={REDIRECT_URI}
```

这一步, code 填上 刚刚获取的code, 然后下面三个和之前一样. 黏贴如浏览器<br />这样就可以获得access_token 了, 有的access_token, 就可以为所欲为了~<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/691897/1582598956253-eacb2fce-d2f3-4218-b235-368b3077839e.png#align=left&display=inline&height=466&name=image.png&originHeight=466&originWidth=1914&size=80628&status=done&style=none&width=1914)
<a name="JTEqX"></a>
## 3. API 使用
获取url 地址:[https://tongji.baidu.com/api/debug/#](https://tongji.baidu.com/api/debug/#)

<a name="NOjVF"></a>
### 3.1 获取设置网站的 ID:

```html
https://openapi.baidu.com/rest/2.0/tongji/config/getSiteList?
  access_token={you_token}
```
![123.jpg](https://cdn.nlark.com/yuque/0/2020/jpeg/691897/1582599246003-9ee8bf4c-1716-4ef3-a189-89c313b445d7.jpeg#align=left&display=inline&height=141&name=123.jpg&originHeight=141&originWidth=400&size=23063&status=done&style=none&width=400)<br />
<br />

<a name="5L5v1"></a>
## 4. 打包成Python函數
python API 打包函數:

```python
import time, requests
TOKEN = ""

def Tongji(TOKEN):
    TIME =time.strftime("%Y%m%d", time.localtime())

    def Get_UV(TOKEN,ID,TIME):
        #Aquiring PV and UV inform mation by ID (History and today)
        A = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token=" + TOKEN
        B = "&site_id="+str(ID)
        C = "&start_date=20200120&end_date="+TIME
        D = "&metrics=pv_count%2Cvisitor_count&method=overview%2FgetTimeTrendRpt"
        url = A+B+C+D
        Data = requests.get(url).json()
        UVPV_list = Data['result']['items'][1]
        PV_T = UVPV_list[-1][0]
        if PV_T =="--":
            PV_T = 0
        UV_T = UVPV_list[-1][1]
        if UV_T =="--":
            UV_T = 0
        #
        PV = []
        UV = []
        for i in UVPV_list:
            if i[0] != "--":
                PV+=[i[0]]
            if i[1] != "--":
                UV+=[i[1]]
        #
        PV = str(sum(PV))+"+"+str(PV_T)
        UV = str(sum(UV))+"+"+str(UV_T)
        return PV,UV

    def Location_Get(TOKEN, TIME):
        # aquiring location-distribution information by province today
      url1 = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token="
      url2 = TOKEN +"&site_id=14350939&start_date="
      url3 = TIME + "&end_date="+TIME+"&metrics=pv_count&method=overview%2FgetDistrictRpt"
      url = url1+url2+url3
      Data = requests.get(url).json()
      Location = ""
      for i in Data['result']['items'][0]:
        Location += i[0] +'\n'
      Location_N = ""
      for i in Data['result']['items'][1]:
        Location_N += str(i[0]) +'\n'
      return Location,Location_N

    def Location_Get_C(TOKEN, TIME):
        # Aquring location-distribution information by Country today
      url1 = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token="
      url2 = TOKEN +"&site_id=14350939&start_date="
      url3 = TIME + "&end_date="+TIME+"&metrics=pv_count&method=visit%2Fworld%2Fa"
      url = url1+url2+url3
      Data = requests.get(url).json()
      Location = ""
      for i in Data['result']['items'][0]:
        Location += i[0]['name'] +'\n'
      Location_N = ""
      for i in Data['result']['items'][1]:
        Location_N += str(i[0]) +'\n'
      return Location,Location_N

    def New_Visitor_Get(TOKEN, TIME):
        # Aquring the ratio of the new visiter today
      url1 = "https://openapi.baidu.com/rest/2.0/tongji/report/getData?access_token="
      url2 = TOKEN + "&site_id=14350939&start_date="
      url3 = TIME + "&end_date=" + TIME + "&metrics=new_visitor_ratio&method=source%2Fall%2Fa"
      url = url1 + url2 +url3
      Data = requests.get(url).json()
      #
      return "新訪客比例 "+str(Data['result']['sum'][0][0])+"%"

    def main():
        # Aquiring Domains' Name and ID
        url1= "https://openapi.baidu.com/rest/2.0/tongji/config/getSiteList?access_token="+TOKEN
        List = requests.get(url1).json()
        Domain = List['list'][0]['domain']
        Domain_ID = List['list'][0]['site_id']
        Sub_domain = [[Domain,Domain_ID]]
        Sub_List = List['list'][0]['sub_dir_list']
        for i in Sub_List:
            Sub_domain += [[i['name'],i['sub_dir_id']]]
        Result = {}
        for i in Sub_domain:
            PV,UV = Get_UV(TOKEN,i[1],TIME)
            Result.update({i[0]:{"PV":PV,"UV":UV}})
        Name = ""
        PV   = ""
        UV   = ""
        for  i  in Result:
            Name += i + "\n"
            PV   += Result[i]['PV']+"\n"
            UV   += Result[i]['UV']+"\n"
        New_Vis_N = New_Visitor_Get(TOKEN, TIME)
        Location,Location_N = Location_Get(TOKEN, TIME)
        Location_C,Location_C_N = Location_Get_C(TOKEN, TIME)
        return Name,PV,UV,Location,Location_N,Location_C,Location_C_N,New_Vis_N


Name,PV,UV,Location,Location_N,Location_C,Location_C_N,New_Vis_N = Tongji(TOKEN)
```
![NrTVwn.jpg](https://s1.ax1x.com/2020/06/26/NrTVwn.jpg)



