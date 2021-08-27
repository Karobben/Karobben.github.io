---
title: "用Python接收邮件和附件"
description: "用Python接收邮件和附件"
url: tdg6bo
date: 2020/10/25
toc: true
excerpt: "用Python接收邮件和附件"
tags: [Python]
category: [Python]
cover: 'https://th.bing.com/th/id/R3d9a78ed6fe62aa5ee6e9fd61c092cca?rik=I7LX8qXniM2YLQ&riu=http%3a%2f%2fgetcodify.com%2fwp-content%2fuploads%2f2016%2f10%2fPython_logo.jpg&w=680'
covercopy: '© getcodify.com'
thumbnail: 'https://tse4-mm.cn.bing.net/th/id/OIP.uTOM2B_iUkko5GTxOa3c-wAAAA'
priority: 10000
---

## 用Python接收邮件和附件

接收邮件的服务又好几种， 这里主要用到pop3 协议， 关于开通和，请看百度经验，获取授权码，[点击这里](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256)<br />基础脚本：[https://www.yuque.com/liuwenkan/pwh0c8/qqmail_r](https://www.yuque.com/liuwenkan/pwh0c8/qqmail_r)

加入删除和查看上一封功能：

<a name="26K7T"></a>
## 添加了一些小functions   
```python
## 从List中寻找匹配
def grep(Str,List):
    for i in List:
        if Str in str(i):
            break
    return i

## 汉字解码
def Decode(STR):
    head = "=?gb2312?b?"
    tail = "?="
    if head in STR:
        H = STR.find(head) + len(head)
        T = STR.find(tail)
        Result = base64.b64decode(STR[H:T]).decode("GBK")
        STR = STR[:H- len(head)] + Result + STR[T+ len(tail):]
    return STR

## 读取邮件
def M_read(index):
    resp, lines, octets = server.retr(index)
    try:
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        print_info(msg)
        print('\n\n'+Date)
    except:
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        From= Decode(str(grep("b'From:",lines)).replace("b'",''))
        To= Decode(str(grep("b'To:",lines)).replace("b'",''))
        Subject= Decode(str(grep("b'Subject:",lines)).replace("b'",''))
        print("",From,To,"\n",Subject,'\n\n',"this mail are purely composed by img or html",sep='\n')
        print('\n\n'+Date)


## 按键对应事件
def Action(Press):
    global index
    global Num_mail
    if Press == "q":
        server.quit()
    if Press == "7":
        server.dele(index)
        index -=1
        Num_mail -=1
    elif Press == "8":
        index -=1
    elif Press == "5":
        index +=1
    if index < 0:
        index =0
    elif index > Num_mail:
        index -= 1
    if index == 0:
        print("No more new e-mails")
    else:
        M_read(index)

```

<a name="xR66z"></a>
## 主逻辑
def M_read(index):<br />   resp, lines, octets = server.retr(index)<br />   try:<br />       Date= str(grep("b'Date:",lines)).replace("b'",'')<br />       msg_content = b'\r\n'.join(lines).decode('utf-8')<br />       msg = Parser().parsestr(msg_content)<br />       print_info(msg)<br />       print('\n\n'+Date)<br />   except:<br />       Date= str(grep("b'Date:",lines)).replace("b'",'')<br />       From= Decode(str(grep("b'From:",lines)).replace("b'",''))<br />       To= Decode(str(grep("b'To:",lines)).replace("b'",''))<br />       Subject= Decode(str(grep("b'Subject:",lines)).replace("b'",''))<br />       print("",From,To,"\n",Subject,'\n\n',"this mail are purely composed by img or html",sep='\n')<br />       print('\n\n'+Date)
```python
while True:
    Press = input()
    os.system('clear')
    if Press == "q":
        break
    if Num_mail == 0:
        print("No New E-mails")
    else:
        Action(Press)
        print("index=",index,"; all=",Num_mail)
```

案件说明：<br />8：上一封<br />5：下一封<br />7：删除此封<br />q：退出<br />注： 只有正常退出，才能够同时删除邮箱中的邮件。删除后在垃圾箱中，不会永久删除。

<a name="ROIgN"></a>
## 下载附件

function： [Source](https://www.jb51.net/article/142236.htm)
```python
def get_email_content(byte_lines, savepath):
    str_lines = []
    for x in byte_lines:
        str_lines.append(x.decode())
    # 拼接邮件内容
    msg_content = '\n'.join(str_lines)
    # 把邮件内容解析为Message对象
    message = Parser().parsestr(msg_content)
    attachments = []
    for part in message.walk():
        filename = part.get_filename()
        #附件名字
        if filename:
            print(filename)
            filename = decode_str(filename)
            data = part.get_payload(decode=True)
            abs_filename = os.path.join(savepath, filename)
            attach = open(abs_filename, 'wb')
            attachments.append(filename)
            attach.write(data)
            attach.close()
    return attachments

```

添加入action，按9下载：

```python
    elif Press == "9":        
        attach = get_email_content(M_read(index), '.')
```

加个获取附件名称， 发现中文乱码问题， 加个decode

```python
def get_attach_name(byte_lines):
    str_lines = []
    for x in byte_lines:
        str_lines.append(x.decode())
    # 拼接邮件内容
    msg_content = '\n'.join(str_lines)
    # 把邮件内容解析为Message对象
    message = Parser().parsestr(msg_content)
    attachments = []
    for part in message.walk():
        filename = part.get_filename()
        #附件名字
        if filename:
            if "=?UTF-8?" in filename:
                filename = base64.b64decode(filename[9:-2]).decode("utf8")
            attachments.append(filename)
    return attachments


def M_read(index):
    resp, lines, octets = server.retr(index)
    try:
        Attachment = get_attach_name(lines)
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        print_info(msg)
        print('\n\n'+Date)
        print("Attachment:",Attachment)
##    try:
    except:
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        From= Decode(str(grep("b'From:",lines)).replace("b'",''))
        To= Decode(str(grep("b'To:",lines)).replace("b'",''))
        Subject= Decode(str(grep("b'Subject:",lines)).replace("b'",''))
        print("",From,To,"\n",Subject,'\n\n',"this mail are purely composed by img or html",sep='\n')
        print('\n\n'+Date)
    return lines
```


完整版：

```python
##!/usr/bin/env python3.7

import poplib
import os, sys, base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()[:-1]
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def grep(Str,List):
    for i in List:
        if Str in str(i):
            break
    return i

def get_attach_name(byte_lines):
    str_lines = []
    for x in byte_lines:
        str_lines.append(x.decode())
    # 拼接邮件内容
    msg_content = '\n'.join(str_lines)
    # 把邮件内容解析为Message对象
    message = Parser().parsestr(msg_content)
    attachments = []
    for part in message.walk():
        filename = part.get_filename()
        #附件名字
        if filename:
            if "=?UTF-8?" in filename:
                filename = base64.b64decode(filename[9:-2]).decode("utf8")
            attachments.append(filename)
    return attachments

def M_read(index):
    resp, lines, octets = server.retr(index)
    try:
        Attachment = get_attach_name(lines)
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        print_info(msg)
        print('\n\n'+Date)
        print("Attachment:",Attachment)
##    try:
    except:
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        From= Decode(str(grep("b'From:",lines)).replace("b'",''))
        To= Decode(str(grep("b'To:",lines)).replace("b'",''))
        Subject= Decode(str(grep("b'Subject:",lines)).replace("b'",''))
        print("",From,To,"\n",Subject,'\n\n',"this mail are purely composed by img or html",sep='\n')
        print('\n\n'+Date)
    return lines

def Action(Press):
    attach =""
    global index
    global Num_mail
    if Press == "q":
        server.quit()
    elif Press == "7":
        server.dele(index)
        index -=1
        Num_mail -=1
    elif Press == "9":
        attach = get_email_content(M_read(index), '.')
    elif Press == "8":
        index -=1
    elif Press == "5":
        index +=1
    if index < 0:
        index =0
    elif index > Num_mail:
        index -= 1
    if index == 0:
        print("No more new e-mails")
    else:
        M_read(index)
    return attach

def Decode(STR):
    head = "=?gb2312?b?"
    tail = "?="
    if head in STR:
        H = STR.find(head) + len(head)
        T = STR.find(tail)
        Result = base64.b64decode(STR[H:T]).decode("GBK")
        STR = STR[:H- len(head)] + Result + STR[T+ len(tail):]
    return STR

def get_email_content(byte_lines, savepath):
    str_lines = []
    for x in byte_lines:
        str_lines.append(x.decode())
    # 拼接邮件内容
    msg_content = '\n'.join(str_lines)
    # 把邮件内容解析为Message对象
    message = Parser().parsestr(msg_content)
    attachments = []
    for part in message.walk():
        filename = part.get_filename()
        if filename:
            print(filename)
            filename = decode_str(filename)
            data = part.get_payload(decode=True)
            abs_filename = os.path.join(savepath, filename)
            attach = open(abs_filename, 'wb')
            attachments.append(filename)
            attach.write(data)
            attach.close()
    return attachments


## 输入邮件地址, 口令和POP3服务器地址:
email = '591465908@qq.com'
password = ''
pop3_server = 'pop.qq.com'
port = 995


## 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server, port)
server.user(email)
server.pass_(password)

## stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
## list()返回所有邮件的编号:
resp, mails, octets = server.list()
## 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
Num_mail = len(mails)

## 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)

##M_read(index)

while True:
    Press = input()
    os.system('clear')
    if Press == "q":
        break
    if Num_mail == 0:
        print("No New E-mails")
    else:
        Action(Press)
        print("index=",index,"; all=",Num_mail)

## lines存储了邮件的原始文本的每一行,

## 可以根据邮件索引号直接从服务器删除邮件:
## server.dele(index)
## 关闭连接:
server.quit()
```

效果：

![NrxxGd.gif](https://s1.ax1x.com/2020/06/26/NrxxGd.gif)


<a name="g4iaJ"></a>
## 删除邮件后保存并刷新
经过几次测试，我发现， 被删除的index并不会重拍，而是就空载那里了， 再次返回查看邮件的时候， 就会出现错误。 因此，最保险的方法，自然是保存和刷新了。同理，如果不保存，只刷新，那么就可以“撤销” 以删除的邮件。

开始想Action那里加上一个，退出，再重连就好～ <br />但是server套在函数里面刷新的时候会报错， = =这样就麻烦了， 所以直接都在mainloop了- -反正 - -以后应该不会debug什么的了。
```python
if Press == "s":
    print("ReFreshing...")
    server.quit()
    server, resp, mails, octets, Num_mail = Refresh()
```
删除以后保存

完整代码

```python
##!/usr/bin/env python3.7

import poplib
import os, sys, base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import signal

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()[:-1]
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def grep(Str,List):
    for i in List:
        if Str in str(i):
            break
    return i

def get_attach_name(byte_lines):
    str_lines = []
    for x in byte_lines:
        str_lines.append(x.decode())
    # 拼接邮件内容
    msg_content = '\n'.join(str_lines)
    # 把邮件内容解析为Message对象
    message = Parser().parsestr(msg_content)
    attachments = []
    for part in message.walk():
        filename = part.get_filename()
        #附件名字
        if filename:
            if "=?UTF-8?" in filename:
                filename = base64.b64decode(filename[9:-2]).decode("utf8")
            attachments.append(filename)
    return attachments

def M_read(index):
    resp, lines, octets = server.retr(index)
    try:
        Attachment = get_attach_name(lines)
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        print_info(msg)
        print('\n\n'+Date)
        print("Attachment:",Attachment)
##    try:
    except:
        Date= str(grep("b'Date:",lines)).replace("b'",'')
        From= Decode(str(grep("b'From:",lines)).replace("b'",''))
        To= Decode(str(grep("b'To:",lines)).replace("b'",''))
        Subject= Decode(str(grep("b'Subject:",lines)).replace("b'",''))
        print("",From,To,"\n",Subject,'\n\n',"this mail are purely composed by img or html",sep='\n')
        print('\n\n'+Date)
    return lines

def Action(Press,server):
    attach =""
    global index
    global Num_mail
    if Press == "q":
        server.quit()
    elif Press == "7":
        server.dele(index)
        index -=1
        Num_mail -=1
    elif Press == "9":
        attach = get_email_content(M_read(index), '.')
    elif Press == "8":
        index -=1
    elif Press == "5":
        index +=1
    if index < 0:
        index =0
    elif index > Num_mail:
        index -= 1
    if index == 0:
        print("No more new e-mails")
    else:
        M_read(index)
    return attach

def Decode(STR):
    head = "=?gb2312?b?"
    tail = "?="
    if head in STR:
        H = STR.find(head) + len(head)
        T = STR.find(tail)
        Result = base64.b64decode(STR[H:T]).decode("GBK")
        STR = STR[:H- len(head)] + Result + STR[T+ len(tail):]
    return STR

def get_email_content(byte_lines, savepath):
    str_lines = []
    for x in byte_lines:
        str_lines.append(x.decode())
    # 拼接邮件内容
    msg_content = '\n'.join(str_lines)
    # 把邮件内容解析为Message对象
    message = Parser().parsestr(msg_content)
    attachments = []
    for part in message.walk():
        filename = part.get_filename()
        if filename:
            print(filename)
            filename = decode_str(filename)
            data = part.get_payload(decode=True)
            abs_filename = os.path.join(savepath, filename)
            attach = open(abs_filename, 'wb')
            attachments.append(filename)
            attach.write(data)
            attach.close()
    return attachments

def Refresh():
    server = poplib.POP3_SSL(pop3_server, port)
    server.user(email)
    server.pass_(password)
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    Num_mail = len(mails)
    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    return server, resp, mails, octets, Num_mail

def INPUT_delay():
  class InputTimeoutError(Exception):
    pass
  def interrupted(signum, frame):
    raise InputTimeoutError
  signal.signal(signal.SIGALRM, interrupted)
  signal.alarm(60)
  try:
    BB = input()
    signal.alarm(0)  # 读到输入的话重置信号
  except InputTimeoutError:
    BB = 'Fresh'
  return BB


## 输入邮件地址, 口令和POP3服务器地址:
email = '591465908@qq.com'
password = ''
pop3_server = 'pop.qq.com'
port = 995


## 连接到POP3服务器:
server = poplib.POP3_SSL(pop3_server, port)
server.user(email)
server.pass_(password)

## stat()返回邮件数量和占用空间:
print('Messages: %s. Size: %s' % server.stat())
## list()返回所有邮件的编号:
resp, mails, octets = server.list()
## 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
Num_mail = len(mails)

## 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)

##M_read(index)

while True:
    Press = INPUT_delay()
    if Press == "q":
        break
    if Press == "Fresh" or Press == "f":
        print("ReFreshing...")
        server, resp, mails, octets, Num_mail = Refresh()
    if Press == "s":
        print("Save & ReFreshing...")
        server.quit()
        server, resp, mails, octets, Num_mail = Refresh()
    if Num_mail == 0:
        os.system('clear')
        print("No New E-mails")
    else:
        os.system('clear')
        Action(Press,server)
        print("index=",index,"; all=",Num_mail)

## lines存储了邮件的原始文本的每一行,

## 可以根据邮件索引号直接从服务器删除邮件:
## server.dele(index)
## 关闭连接:
server.quit()

```

Gitub 链接： [https://github.com/Karobben/Karobben-Work-Station/blob/master/QQmail_recive.py](https://github.com/Karobben/Karobben-Work-Station/blob/master/QQmail_recive.py)






