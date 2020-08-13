---
title: "itchat"
description: "itchat"
url: itchat
---

# itchat

wechat bot<br />微信机器人

确保你可以正常登录网页版微信

```python
import itchat

# 登录
itchat.login()
itchat.auto_login(enableCmdQR=True)
itchat.auto_login(hotReload=True)

# 发送消息
itchat.send(u'你好', 'filehelper')
# 联系人列表
F_list = itchat.get_friends(update=True)


#找到发信息的ID
for i in F_list:
  if i['RemarkName'] == 'XXX': #昵称
  print(i['UserName'])



# friends
friends = itchat.get_friends(update=True)[0:]
# aotu-return
import itchat
#自动回复
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return "本人已死，有事招魂，没事烧纸 ಠಗಠ"#+msg["Text"]
#登入
itchat.auto_login()
#保持运行
itchat.run()

```
