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


PAGE_HEAD = "#########pyscript start##########"
PAGE_TAIL = "#########pyscript end##########"
headers = Cookis.Yuque_X_Auth_Token

def Get_list(url):
    Data = requests.get(url,headers=headers).json()
    Result = Data['data']['toc_yml']
    Book_ID = Data['data']['id']
    Result_L = Result.split('- ')[2:]
    Result = []
    for i in Result_L:
        Result += [Str2Dic(i)]
    Page = ""
    for i in Result:
        if i['type'] == 'TITLE':
            Page += "<h1>"+i[' title']+"</h1>"
        else:
            Page +=Cookis.Get_Stat_From_ID(i[' id'],url,Book_ID)
    return Page

url = "https://www.yuque.com/api/v2/repos/liuwenkan/blog"
Page = Get_list(url)



F = open('O-index.html','r').read()
Test = F[:(F.find(PAGE_HEAD)+len(PAGE_HEAD))]+"\n"+Page+"\n"+F[F.find(PAGE_TAIL):]
F = open('O-index.html','w')
F.write(Test)
F.close()
