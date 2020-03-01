#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def Substitude(Content):
    Sider_H = "<code>"
    Sider_T = "</code>"
    #
    Target = open("index.html",'r').read()
    Target = Target[:Target.find(Sider_H)+len(Sider_H)] +Content+ Target[Target.find(Sider_T):]
    #
    F = open("index.html",'w')
    F.write(Target)
    F.close()

url = "https://github.com/Karobben/Karobben.github.io/commits/master"
header = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': '_octo=GH1.1.1014544621.1577848239; _ga=GA1.2.827504913.1577848244; _device_id=ed11c4f75773d5fc016e406e9c214086; user_session=CM8ddn4Nrj0NYAH4n4b5_F_8qN80PPjwgo_YQkd6rMaIOXCb; __Host-user_session_same_site=CM8ddn4Nrj0NYAH4n4b5_F_8qN80PPjwgo_YQkd6rMaIOXCb; logged_in=yes; dotcom_user=Karobben; has_recent_activity=1; _gh_sess=JTCjGiI3tkiIBHt5XpRRADqgXqILD6coZlDWh7vnjcv%2FpmbdJBvDOABm7iFrgoB%2BP3QsO1AHnl8jV53yz1RVyeVNYaVCB8T2mUSASkjEEiCSXQOLyeFdarqX1hfRbpWbBvvhAgh4WetapZn3J%2FYVWHhz5mU%2B5HN3QnDI2AfTZ2o%3D--a8%2FYRz2QEIEF4BKU--%2Bszj1nezUu5mKVhZtyUVdg%3D%3D',
'Host': 'github.com',
'If-None-Match': 'W/"48afb061ad41629d71d8941d0c739581"',
'Referer': 'https://github.com/Karobben/Karobben.github.io',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

GET  = requests.get(url,headers=header)
soup = BeautifulSoup(GET.text, features='lxml')
TXT = soup.find('div',{'class':"list commit-list"}).get_text()

List = TXT.split('\n\n')
Result = ""
for i in List:
    if i != "" and '\n      ' in i: # i == Date
        Result += "\n"+i.replace('      ','')
    elif i != "" :
        i = i.replace('\n    ','--')
        Result += i +"\n"

Substitude(Result)
