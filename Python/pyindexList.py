#!/usr/bin/env python3

import requests

'''
import Cookies and headers
'''
import sys
sys.path.append("../..")
import Cookis

def Str2Dic(List):
    List  = List.replace('\n ','\n')
    List = List.split('\n')[:-1]
    Dic = {}
    for i in List:
        i = i.split(': ')
        Dic.update({i[0]:i[1]})
    return Dic

def Get_Stat(ID):
    path = "https://www.yuque.com/liuwenkan/python/"
    ID = str(ID)
    url = "https://www.yuque.com/api/v2/repos/714085/docs/"+ID
    headers = {
        "authority":"www.yuque.com",
        "method": "GET",
        "path": "/api/books/"+ID+"/statistics?",
        "scheme": "https",
        "accept":"application/json",
        'accept-encoding':"gzip, deflate, br",
        "accept-language":"en-US,en;q=0.9",
        "cache-type":"application/json",
        "cookie": "lang=en-us; _yuque_session=0IcG7IcOmXq74z2jfuT3yJmjTSlrgLToswhBiI4ohDBqBts5-8WJfteRjqw88wpJQ3XStA38MULdxsFTr1ppbg==; UM_distinctid=17049c8f43fc40-0ad8aa98fd5065-1a201708-1fa400-17049c8f440c9a; __wpkreporterwid_=7c863911-550a-4b1b-933c-bee21834b911; ctoken=-WMVHRBmIhF4MxjTVZJiGEGp; CNZZDATA1272061571=561998253-1581783353-https%253A%252F%252Fwww.yuque.com%252F%7C1582205025; _TRACERT_COOKIE__SESSION=15e83d89-8aaa-4226-b69c-e5da5765906a; tree=a385%016bcaa0d8-c8e0-4d59-a3b1-dc2d6f69d87b%0114",
        #"referer":"https://www.yuque.com/r/liuwenkan/rr/statistics",
        "user-agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
        #"x-csrf-token": "-WMVHRBmIhF4MxjTVZJiGEGp",
        "X-Auth-Token":"SboLOMTuWC8yvdryxbzj0xvDPjFwOKZhNGYSfxZZ",
        "x-requested-with": "XMLHttpRequest"
        }
    #
    res     = requests.get(url, headers=headers, timeout=30)
    Data    = res.json()
    Slug    = str(Data['data']['slug'])
    Title   = str(Data['data']['title'])
    Like    = str(Data['data']['likes_count'])
    C_des   = str(Data['data']['custom_description'])
    S_des   = str(Data['data']['description'][:20])
    Words   = str(Data['data']['word_count'])
    Creat   = str(Data['data']['created_at'].split('T')[0])
    Updat   = str(Data['data']['updated_at'].split('T')[0])
    Href = path + Slug
    if C_des == "None":
        C_des = S_des
    Result = '<p class="Docs" ><a href="'+Href+'">'+Title+'</a><count>Like:'+Like+'; creat:'+Creat+'</count></p><p class="Docs_count">'+C_des+'<data>words:'+Words+'; update:'+Updat+'</data></p>'
    return Result

PAGE_HEAD = "#########pyscript start##########"
PAGE_TAIL = "#########pyscript end##########"
headers = Cookis.Yuque_X_Auth_Token

url = "https://www.yuque.com/api/v2/repos/liuwenkan/python"
Data = requests.get(url,headers=headers).json()

Result = Data['data']['toc_yml']
Result_L = Result.split('- ')[2:]

Result = []
for i in Result_L:
    Result += [Str2Dic(i)]

Page = ""
for i in Result:
    if i['type'] == 'TITLE':
        Page += "<h1>"+i[' title']+"</h1>"
    else:
        Page +=Get_Stat(i[' id'])

Page = Page

F = open('P-index.html','r').read()
Test = F[:(F.find(PAGE_HEAD)+len(PAGE_HEAD))]+"\n"+Page+"\n"+F[F.find(PAGE_TAIL):]
F = open('P-index.html','w')
F.write(Test)
F.close()
