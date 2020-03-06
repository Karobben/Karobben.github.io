#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
'''
import Cookies and headers
'''
import sys
sys.path.append("..")
import Cookis



def Substitude(Sider_H,Sider_T,Content):
    Target = open("index.html",'r').read()
    Target = Target[:Target.find(Sider_H)+len(Sider_H)] +Content+ Target[Target.find(Sider_T):]
    #
    F = open("index.html",'w')
    F.write(Target)
    F.close()

'''
Update widgets
'''
url = "https://github.com/Karobben/Karobben.github.io/commits/master"

GET  = requests.get(url,headers=Cookis.Git_commit_header)
soup = BeautifulSoup(GET.text, features='lxml')
TXT = soup.find('div',{'class':"commits-listing commits-listing-padded js-navigation-container js-active-navigation-container"}).get_text()

List = TXT.split('\n\n')
Result = ""
for i in List:
    if i != "" and '\n      ' in i: # i == Date
        Result += "\n"+i.replace('      ','')
    elif i != "" :
        i = i.replace('\n    ','--')
        Result += i +"\n"

Substitude("<code>","</code>",Result)

'''
Reading Count
'''
Baidu_TJ = Cookis.Tongji(Cookis.Baidu_TOKEN)
Bai_Name = Baidu_TJ[0].split('\n')[:-1]
Bai_View = Baidu_TJ[1].split('\n')[:-1]



#R
List = ['R Home',  'gggit','PCA','R-Normalization']
Stat_R = Cookis.Get_Stat('rr')
R_Count = int(Stat_R[0])
for i in List:
    R_Count +=int(Bai_View[Bai_Name.index(i)].split('+')[0])
Substitude("<R_veiw>","</R_veiw>",str(R_Count))
Substitude("<R_doc>","</R_doc>",Stat_R[1])

#Python
List = ['P-index','urwid']
Stat_Python = Cookis.Get_Stat('python')
Stat_Pythons = Cookis.Get_Stat('pythons')
Python_Count = int(Stat_Python[0]) + int(int(Stat_Pythons[0]))
Doc_Python = int(Stat_Python[1]) + int(int(Stat_Pythons[1])) +len(List)
for i in List:
    Python_Count +=int(Bai_View[Bai_Name.index(i)].split('+')[0])
Substitude("<Python_veiw>","</Python_veiw>",str(Python_Count))
Substitude("<Python_doc>","</Python_doc>",str(Doc_Python))

# Blog
List = ['scrcpy',   'Whyblog',    'Epidemic', 'CutSocial', 'Blog index']
Stat_Blog = Cookis.Get_Stat('blog')
Blog_Count = int(Stat_Blog[0])
Doc_Blog = int(Stat_Blog[1]) +len(List)
for i in List:
    Blog_Count +=int(Bai_View[Bai_Name.index(i)].split('+')[0])
Substitude("<Others_veiw>","</Others_veiw>",str(Blog_Count))
Substitude("<Others_doc>","</Others_doc>",  str(Doc_Blog))

# Notes
List = ['EngS']
Stat_Notes = Cookis.Get_Stat('notes')
Notes_Count = int(Stat_Notes[0])
Doc_Notes   = int(Stat_Notes[1]) +len(List)
for i in List:
    Notes_Count +=int(Bai_View[Bai_Name.index(i)].split('+')[0])
Substitude("<Notes_veiw>","</Notes_veiw>",str(Notes_Count))
Substitude("<Notes_doc>","</Notes_doc>",str(Doc_Notes))

# Protacols
#List = ['EngS']
Stat_Protacols = Cookis.Get_Stat('bioinf')
Protacols_Count = int(Stat_Protacols[0])
Doc_Protacols   = int(Stat_Protacols[1]) #+len(List)
#for i in List:
#    Notes_Count +=int(Bai_View[Bai_Name.index(i)].split('+')[0])
Substitude("<Protocols_veiw>","</Protocols_veiw>",str(Protacols_Count ))
Substitude("<Protocols_doc>","</Protocols_doc>",str(Doc_Protacols))

# Bash
# Notes
#List = ['EngS']
Stat_Bash = Cookis.Get_Stat('linux')
Bash_Count = int(Stat_Bash[0])
Doc_Bash   = int(Stat_Bash[1]) #+len(List)
#for i in List:
#    Notes_Count +=int(Bai_View[Bai_Name.index(i)].split('+')[0])
Substitude("<Bash_veiw>","</Bash_veiw>",str(Bash_Count ))
Substitude("<Bash_doc>","</Bash_doc>",str(Doc_Bash))
