---
title: "用python寫一個B站彈幕聊天機器人腳本"
description: "用python寫一個B站彈幕聊天機器人腳本"
url: hr6xgc
date: 2020/10/25
toc: true
excerpt: "How to Using Python to Acquire Websites' Responding Time"
tags: [Python, Crawler, BiliBili]
category: [Python, Scripting, Practice]
cover: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
thumbnail: 'https://s1.ax1x.com/2020/05/22/YLZMxf.png'
priority: 10000
---

## 用python寫一個B站彈幕聊天機器人腳本

<a name="HeSJr"></a>
## 1 回覆B站彈幕基本框架:
(當時bing出來抄人家的, 能用- -但是忘記表明出處了, 實在是抱歉- -)

```python
##!/usr/bin/env python3.7

import requests, sys  #网络请求

##Cookies = "LIVE_BUVID=AUTO3715382739921424; buvid3=71AC02C7-EF25-46A5-9A2F-DB1CB10744F71607infoc; rpdid=oopmqlpqkmdoskqimpwww; stardustvideo=1; CURRENT_FNVAL=16; dssid=8aabde0ff0f7f1621; dsess=BAh7CkkiD3Nlc3Npb25faWQGOgZFVEkiFWRlMGZmMGY3ZjE2MjE3MWMGOwBG%0ASSIJY3NyZgY7AEZJIiUxYTM3YTg4MTY2NzZhNWZkNjYyODAyOWQwODk1NTlh%0AMgY7AEZJIg10cmFja2luZwY7AEZ7B0kiFEhUVFBfVVNFUl9BR0VOVAY7AFRJ%0AIi1lZjFkZjRjZTdiMWE2Y2JkZmQyZjRkMzA2OGYyMGI0NzhjYjU1OGEzBjsA%0ARkkiGUhUVFBfQUNDRVBUX0xBTkdVQUdFBjsAVEkiLWRkMDY1ZWQyNjNjNjdk%0ANzk5Zjk0M2FiNmMzOWI1NWM1ZTAwOGNiYjUGOwBGSSIKY3RpbWUGOwBGbCsH%0Aj3a9W0kiCGNpcAY7AEYiEjY4LjEwNy4xMjQuNTM%3D%0A--b5b62086b230a085ae65aee9304d7f14ca8a07ad; fts=1539143396; CURRENT_QUALITY=64; _uuid=547F11BE-9B64-40CC-37DE-6B95B010429C05405infoc; INTVER=1; sid=9onpe38s; DedeUserID=393056819; DedeUserID__ckMd5=43771d91224c7285; SESSDATA=d1486084%2C1576633926%2Ca277c9b1; bili_jct=b29db4670b4f9967fb2921a0fc878950; UM_distinctid=16e7c3622401e-01fbe0ab154c45-76256753-1fa400-16e7c362241181; laboratory=1-1"

def B_send(MSG):
    Cookies =  "LIVE_BUVID=AUTO5015807896693605; _uuid=58C69C39-C741-47C7-0E98-A379326816DE70318infoc; buvid3=3B00857F-A757-4982-9792-4B46DEC0BB12155821infoc; sid=bejf3qns; LIVE_ROOM_ADMIN_UP_TIP=1; CURRENT_FNVAL=16; rpdid=|(k|k)k|))Y)0J'ul)|~mYmk|; im_notify_type_393056819=0; _ga=GA1.2.517604625.1581950019; dy_spec_agreed=1; GIFT_BLOCK_COOKIE=GIFT_BLOCK_COOKIE; INTVER=1; stardustpgcv=0606; DedeUserID=393056819; DedeUserID__ckMd5=43771d91224c7285; SESSDATA=bb15b3a2%2C1598937340%2C37fab*31; bili_jct=e8377d560fe3434ffd36531d323df842; CURRENT_QUALITY=80; bp_t_offset_393056819=365856292215780322; _dfcaptcha=08c1c131463a58b5c74c50f3d9eaed6d; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1583825216,1583853309,1583925148,1584087368; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1584087368; PVID=15"
    cookie = {'Cookie': Cookies}
    data = {
    'color':'16777215',
    'fontsize':'25',
    'mode':'1',
    'msg':MSG,
    'rnd':'1584087359',
    'roomid':'21154895',
    'bubble':'0',
    'aid':'56737027',
    'csrf_token':'e8377d560fe3434ffd36531d323df842',
    'csrf':'e8377d560fe3434ffd36531d323df842'
    }
    requests.post('https://api.live.bilibili.com/msg/send', cookies=cookie, data=data)
##senddanmu.sendDM(data) #<Response [200]> 200是状态码 表示pass
```

獲取cookies 方法見視屏:....[還沒上傳]

<a name="POfJs"></a>
## 2 獲取彈幕的方法:

用github的項目吧, [xfgryujk](https://github.com/xfgryujk)/[blivedm](https://github.com/xfgryujk/blivedm)<br />這是我已知的, 最好的彈幕獲取項目

```bash
git clone https://github.com/xfgryujk/blivedm.git
```


<a name="uztyh"></a>
## 3 聊天模塊
用: [https://blog.csdn.net/qq_29129381/article/details/82865617](https://blog.csdn.net/qq_29129381/article/details/82865617)<br />這個是最簡單的<br />抄來的代碼~, 感謝[青云客智能聊天机器人](http://api.qingyunke.com/)的奉獻~
```python
class airoot(object):
    #This function is original from:https://blog.csdn.net/qq_29129381/article/details/82865617
    def __init__(self):
        self.url = r'http://api.qingyunke.com/api.php?%s'
        self.data = {
            'key':'free',
            'appid':0,
            'msg':''
        }
    def getword(self, word=''):
        self.data['msg'] = word
        if self.data['msg'] == '':
            self.data['msg'] = '你不说话, 我来撩你吧'
        self.params = urllib.parse.urlencode(self.data)
        self.url = self.url % self.params
        self.page = urllib.request.urlopen(self.url,timeout=15).read()
        self.res = json.loads(self.page)
        self.res['content'] = self.res['content'].replace('{br}',' ')
        return self.res
```

<a name="iu4Rt"></a>
## 4 在blivedm裏面, 加入聊天機器人的代碼
<a name="pt8sn"></a>
### 修改`sample.py`
把client ID改成要回覆彈幕的ID
![NrxI2R.png](https://s1.ax1x.com/2020/06/26/NrxI2R.png)


```python
    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        print(f'{danmaku.uname}：{danmaku.msg}')
```
這兩行是彈幕, 直接用後面的{danmaku.msg}就好,<br />這裏, 我們改成

```python
    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        print(f'{danmaku.uname}：{danmaku.msg}')
        if f'{danmaku.uname}' != "史上最不正經的生物狗":#這裏是我的名字, 不把自己排除, 會自己套娃, 無限自嗨的= =
            B_send(airoot().getword(str(f'{danmaku.msg}'))['content'])
```

<a name="TL6fr"></a>
### 彈幕分割
因爲普通人員, 一個彈幕只能發20個字節, 字數多了, 會自動忽略, 所以需要分割分佈發送

```python
def B_Slice(MSG):
    for i in range((len(MSG)//20)+1):
        B_send(MSG[i*20:(i+1)*20])
```

把分割套進去
```python
    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        print(f'{danmaku.uname}：{danmaku.msg}')
        if f'{danmaku.uname}' != "史上最不正經的生物狗":
            B_Slice(airoot().getword(str(f'{danmaku.msg}'))['content'])
```

<a name="Lp4df"></a>
### 鏈接超時
發現經常連接超時, 然後卡在了那裏. 我設置了一個timeout=15, 在前面, 已更新<br />後面老地方, 加一個try

```python
    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        print(f'{danmaku.uname}：{danmaku.msg}')
        if f'{danmaku.uname}' != "史上最不正經的生物狗":
            try:
                MSG = airoot().getword(str(f'{danmaku.msg}'))['content']
            except:
                MSG = "鏈接超時了 = =(自動回覆)"
            B_Slice(MSG)
```

<a name="CiMm7"></a>
### 发送太快而被吞
加一个1s延迟,发送弹幕过多的时候
```python
def B_Slice(MSG):
    for i in range((len(MSG)//20)+1):
        B_send(MSG[i*20:(i+1)*20])
        time.sleep(1)
```

娛樂而已, 應該不會載更新了, /摔板凳

<a name="BB8A3"></a>
## `Sample.py`

```python
## -*- coding: utf-8 -*-

import asyncio,requests, sys, time
import urllib.request
import urllib.parse
import json

import blivedm


class MyBLiveClient(blivedm.BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def __on_vip_enter(self, command):
        print(command)
    _COMMAND_HANDLERS['WELCOME'] = __on_vip_enter  # 老爷入场

    async def _on_receive_popularity(self, popularity: int):
        #print(f'当前人气值：{popularity}')
        AAAAAAAA = 1
    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        print(f'{danmaku.uname}：{danmaku.msg}')
        if f'{danmaku.uname}' != "史上最不正經的生物狗":
            try:
                MSG = airoot().getword(str(f'{danmaku.msg}'))['content']
            except:
                MSG = "鏈接超時了 = =(自動回覆)"
            B_Slice(MSG)

    async def _on_receive_gift(self, gift: blivedm.GiftMessage):
        print(f'{gift.uname} 赠送{gift.gift_name}x{gift.num} （{gift.coin_type}币x{gift.total_coin}）')

    async def _on_buy_guard(self, message: blivedm.GuardBuyMessage):
        print(f'{message.username} 购买{message.gift_name}')

    async def _on_super_chat(self, message: blivedm.SuperChatMessage):
        print(f'醒目留言 ¥{message.price} {message.uname}：{message.message}')

class airoot(object):
    #This function is original from:https://blog.csdn.net/qq_29129381/article/details/82865617
    def __init__(self):
        self.url = r'http://api.qingyunke.com/api.php?%s'
        self.data = {
            'key':'free',
            'appid':0,
            'msg':''
        }
    def getword(self, word=''):
        self.data['msg'] = word
        if self.data['msg'] == '':
            self.data['msg'] = '你不说话, 我来撩你吧'
        self.params = urllib.parse.urlencode(self.data)
        self.url = self.url % self.params
        self.page = urllib.request.urlopen(self.url,timeout=15).read()
        self.res = json.loads(self.page)
        self.res['content'] = self.res['content'].replace('{br}',' ')
        return self.res

def B_send(MSG):
    Cookies =  ""#自己的
    cookie = {'Cookie': Cookies}
    data = {
    'color':'16777215',
    'fontsize':'25',
    'mode':'1',
    'msg':MSG,
    'rnd':'1584087359',
    'roomid':'21154895',
    'bubble':'0',
    'aid':'56737027',
    'csrf_token':'e8377d560fe3434ffd36531d323df842',
    'csrf':'e8377d560fe3434ffd36531d323df842'
    }
    requests.post('https://api.live.bilibili.com/msg/send', cookies=cookie, data=data)
##senddanmu.sendDM(data) #<Response [200]> 200是状态码 表示pass

def B_Slice(MSG):
    for i in range((len(MSG)//20)+1):
        B_send(MSG[i*20:(i+1)*20])
        time.sleep(1)

async def main():
    # 参数1是直播间ID
    # 如果SSL验证失败就把ssl设为False
    client = MyBLiveClient(21154895, ssl=True)
    future = client.start()
    try:
        # 5秒后停止，测试用
        # await asyncio.sleep(5)
        # future = client.stop()
        # 或者
        # future.cancel()
        await future
    finally:
        await client.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

```


<a name="UqplL"></a>
## 用戶自主開啓關閉機器人

有時候機器人實在是太煩了, 簡直煩到想取關<br />這裏, 我們可以添加一個屏蔽名單, 並用簡單的命令判斷,讓發彈幕的人, 自主選擇, 打開或者關閉機器人回答<br />爲了長久有效, 我們最好是, 把這個名單存入本地文件. 這裏, 取名IgnoreList,我直接把他放進同樣的路徑, 方便讀取.

```python
def IgnoreList(USER,MSG):
    Ignore_List = open(sys.path[0]+"/IgnoreList",'r').read().split("\n")[:-1]
    # 設定屏蔽規則
    if str(MSG) == "菲菲辛苦啦~":
        B_Slice("好的,菲菲先行告退了,愛你呦,木木噠~")
        Ignore_List += [USER]
    elif str(MSG) == "菲菲快回來~":
        try:
            Ignore_List.remove(USER)
        except:
            B_Slice("你一直都在菲菲心里哟~")
    Update = "\n".join(Ignore_List)+"\n"
    F = open(sys.path[0]+"/IgnoreList",'w')
    F.write(Update)
    F.close()
    return Ignore_List
```
![Nrxox1.png](https://s1.ax1x.com/2020/06/26/Nrxox1.png)

<a name="l8uBi"></a>
## 防沉迷程序
爲了防止惡意刷屏,或者過於小盆友沉迷而耽誤學習, 因此在學習/工作時間內, 限制每分鐘內響應次數. 若超過, 則忽視多少分鐘<br />時間設定在早上9點,到晚上9點之間
```python
Bubling_List = {}
Bubling_ban = {}

def ToBubling_detect(User,Bubling_List,Bubling_ban,Times,TimeOut):
    Times -=1
    if User != '史上最不正經的生物狗' and User not in Bubling_ban.keys():
        if User not in Bubling_List.keys():
            Bubling_List.update({User:{'Time': time.time(), 'Num': 1}})
        else:
            Time_endur = time.time() - Bubling_List[User]['Time']
            if Time_endur < 60 and Bubling_List[User]['Num'] > Times:
                Bubling_ban.update({User:time.time()})
                B_Slice(User+" 因調戲菲菲過於頻繁,而被選擇性忽略5min, 略略略~")
                Bubling_List[User]['Num'] = 0
                Bubling_List[User]['Time'] = time.time()
            elif Time_endur < 60 and Bubling_List[User]['Num'] <= Times:
                Bubling_List[User]['Num'] +=1
            else:
                Bubling_List[User]['Num'] =1
                Bubling_List[User]['Time'] = time.time()
        try:
            if time.time() - Bubling_ban[User] > TimeOut*60:
                Bubling_ban.pop(User)
        except Exception as e:
            Bubling_ban = Bubling_ban
    return Bubling_List, Bubling_ban
```



到此, 全程序爲: (自己加cookies)

```python
## -*- coding: utf-8 -*-

import asyncio,requests, sys, time
import urllib.request
import urllib.parse
import json

import blivedm



class MyBLiveClient(blivedm.BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def __on_vip_enter(self, command):
        print(command)
    _COMMAND_HANDLERS['WELCOME'] = __on_vip_enter  # 老爷入场

    async def _on_receive_popularity(self, popularity: int):
        #print(f'当前人气值：{popularity}')
        AAAAAAAA = 1
    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        global Bubling_List, Bubling_ban
        print(f'{danmaku.uname}：{danmaku.msg}')
        # Bubuling test
        Bubling_List, Bubling_ban = ToBubling_detect(f'{danmaku.uname}',Bubling_List,Bubling_ban,10,5)
        # IgnoreList
        Ignore_List = IgnoreList(f'{danmaku.uname}',f'{danmaku.msg}')
        Ignore_List += list(Bubling_ban.keys())
        #print(Ignore_List)
        #print(Bubling_List)
        if f'{danmaku.uname}' not in Ignore_List:
            try:
                MSG = airoot().getword(str(f'{danmaku.msg}'))['content']
            except:
                MSG = "鏈接超時了 = =(自動回覆)"
            B_Slice(MSG)

    async def _on_receive_gift(self, gift: blivedm.GiftMessage):
        print(f'{gift.uname} 赠送{gift.gift_name}x{gift.num} （{gift.coin_type}币x{gift.total_coin}）')
        B_Slice(str(f'谢谢{gift.uname} 赠送的{gift.gift_name}'))
    async def _on_buy_guard(self, message: blivedm.GuardBuyMessage):
        print(f'{message.username} 购买{message.gift_name}')

    async def _on_super_chat(self, message: blivedm.SuperChatMessage):
        print(f'醒目留言 ¥{message.price} {message.uname}：{message.message}')

class airoot(object):
    #This function is original from:https://blog.csdn.net/qq_29129381/article/details/82865617
    def __init__(self):
        self.url = r'http://api.qingyunke.com/api.php?%s'
        self.data = {
            'key':'free',
            'appid':0,
            'msg':''
        }
    def getword(self, word=''):
        self.data['msg'] = word
        if self.data['msg'] == '':
            self.data['msg'] = '你不说话, 我来撩你吧'
        self.params = urllib.parse.urlencode(self.data)
        self.url = self.url % self.params
        self.page = urllib.request.urlopen(self.url,timeout=20).read()
        self.res = json.loads(self.page)
        self.res['content'] = self.res['content'].replace('{br}',' ')
        return self.res

def IgnoreList(USER,MSG):
    Ignore_List = open(sys.path[0]+"/IgnoreList",'r').read().split("\n")[:-1]
    # 設定屏蔽規則
    if str(MSG) == "菲菲辛苦啦~":
        B_Slice("好的,菲菲先行告退了,愛你呦,木木噠~")
        Ignore_List += [USER]
    elif str(MSG) == "菲菲快回來~":
        try:
            Ignore_List.remove(USER)
        except:
            B_Slice("你一直都在菲菲心里哟~")
    Update = "\n".join(Ignore_List)+"\n"
    F = open(sys.path[0]+"/IgnoreList",'w')
    F.write(Update)
    F.close()
    return Ignore_List

def B_send(MSG):
    Cookies =  ""
    cookie = {'Cookie': Cookies}
    data = {
    'color':'16777215',
    'fontsize':'25',
    'mode':'1',
    'msg':MSG,
    'rnd':'1584087359',
    'roomid': str(ROOM_ID),
    'bubble':'0',
    'aid':'56737027',
    'csrf_token':'e8377d560fe3434ffd36531d323df842',
    'csrf':'e8377d560fe3434ffd36531d323df842'
    }
    requests.post('https://api.live.bilibili.com/msg/send', cookies=cookie, data=data)
##senddanmu.sendDM(data) #<Response [200]> 200是状态码 表示pass

Bubling_List = {}
Bubling_ban = {}
def ToBubling_detect(User,Bubling_List,Bubling_ban,Times,TimeOut):
    Times -=1
    if User != '史上最不正經的生物狗' and User not in Bubling_ban.keys():
        if User not in Bubling_List.keys():
            Bubling_List.update({User:{'Time': time.time(), 'Num': 1}})
        else:
            Time_endur = time.time() - Bubling_List[User]['Time']
            if Time_endur < 60 and Bubling_List[User]['Num'] > Times:
                Bubling_ban.update({User:time.time()})
                B_Slice(User+" 因調戲菲菲過於頻繁,而被選擇性忽略5min, 略略略~")
                Bubling_List[User]['Num'] = 0
                Bubling_List[User]['Time'] = time.time()
            elif Time_endur < 60 and Bubling_List[User]['Num'] <= Times:
                Bubling_List[User]['Num'] +=1
            else:
                Bubling_List[User]['Num'] =1
                Bubling_List[User]['Time'] = time.time()
        try:
            if time.time() - Bubling_ban[User] > TimeOut*60:
                Bubling_ban.pop(User)
        except Exception as e:
            Bubling_ban = Bubling_ban
    return Bubling_List, Bubling_ban




ROOM_ID = 21154895
def B_Slice(MSG):
    for i in range((len(MSG)//20)+1):
        B_send(MSG[i*20:(i+1)*20])
        time.sleep(1)

async def main():
    # 参数1是直播间ID
    # 如果SSL验证失败就把ssl设为False
    client = MyBLiveClient(ROOM_ID, ssl=True)
    future = client.start()
    try:
        # 5秒后停止，测试用
        # await asyncio.sleep(5)
        # future = client.stop()
        # 或者
        # future.cancel()
        await future
    finally:
        await client.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
```
