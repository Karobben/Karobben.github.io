#!/usr/local/bin/python3
import os

def Sheader(OUTPUT):
    Tample = open('O-index.html','r').read()
    Sider_H = "<!-- sider bar -->"
    Sider_T = "<!-- end s-header -->"
    Content = Tample[Tample.find(Sider_H):Tample.find(Sider_T)]
    #
    Target = open(OUTPUT,'r').read()
    Target = Target[:Target.find(Sider_H)] +Content+ Target[Target.find(Sider_T):]
    #
    F = open(OUTPUT,'w')
    F.write(Target)
    F.close()


List = os.popen('ls *.html').read().split('\n')[:-1]
for i in List:
    Sheader(i)
