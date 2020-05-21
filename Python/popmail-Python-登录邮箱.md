---
url: popmail2
---

# popmail-Python 登录邮箱


<a name="LwItF"></a>
# 登录

以ＱＱ邮箱为例
```python
import poplib

# 输入邮件地址, 口令和POP3服务器地址:
email = '591465908@qq.com'
password = input('Password: ') #这里是授权码，必须去申请
pop3_server = 'pop.qq.com'

# 连接到POP3服务器:
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息:
server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

# 身份认证:
server.user(email)
server.pass_(password)
```

授权码申请：[https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=1001256)

```python
server.set_debuglevel(1)
# debug 信息， 会打印出账号和密码， 不建议使用


server.apop(            server.noop(            server.stat(
server.capa(            server.pass_(           server.stls(
server.close(           server.port             server.timestamp
server.dele(            server.quit(            server.top(
server.encoding         server.retr(            server.uidl(
server.file             server.rpop(            server.user(
server.getwelcome(      server.rset(            server.utf8(
server.host             server.set_debuglevel(  server.welcome
server.list(            server.sock             

```
