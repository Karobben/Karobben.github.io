---
title: "Linux Commands"
description: "Linux Commands"
url: system2
date: 2020/06/26
toc: true
excerpt: "Linux commands like, sort, uniq, head, tail, echo, mail, cat..."
tags: [Linux, bash]
category: [Linux, Bash, More]
cover: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=465&h=180'
thumbnail: 'https://tse3-mm.cn.bing.net/th/id/OIP.QohK_-okTvuh7r82wJlhNAHaE9?w=180&h=180'
priority: 10000
---

## Linux Commands


## Public and private key

- Create a public and private key pair.
- Upload your public key on your remote Unix and Linux servers.
- Use ssh to login to your remote servers without using a password.
- Add your key at the end of `~/.ssh/authorized_keys` file

```bash
# generate the key for your local computer
ssh-keygen -t rsa
# upload your public key
scp ~/.ssh/id_rsa.pub username@192.168.1.100:~

# Now, login your remote server and add the public key at the end of authorize
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys

# Now you shell be logging without any problems.
```

## location of bash script

Source: [Hiks Gerganov](https://www.baeldung.com/linux/bash-get-location-within-script)

```r
# paht of the script file
echo "${BASH_SOURCE}"

# path of script's directory
echo "$(dirname -- "$(readlink -f "${BASH_SOURCE}")")"
```

## sort & uniq

```bash
##数字大小排序

sort -n  test.txt | while read num ;do echo $num ; sum=`expr $sum + $num 2> /dev/null`;echo $sum > /tmp/sum.tmp ;done ; echo -n "sum is :" ;cat /tmp/sum.tmp

sort -n C.txt >T.txt

## 二、去掉所有重复的数据行
cat data1.txt | sort | uniq
```

## head and tail
```bash
tail
实例3：从第5行开始显示文件
命令：
tail -n +5 log2014.log

```

## echo
```bash
echo AAA
echo -e "\033[41;36m something here \033[0m"
echo -e "\033[40;37m red \033[0m"
echo -e "\033[41;37m blue \033[0m"
echo -e "\033[42;37m green \033[0m"
echo -e "\033[43;37m 黄底白字 \033[0m"
echo -e "\033[44;37m 蓝底白字 \033[0m"
echo -e "\033[45;37m 紫底白字 \033[0m"
echo -e "\033[46;37m 天蓝底白字 \033[0m"
echo -e "\033[47;30m 白底黑字 \033[0m"

```

## find

```bash
# find empty files and delete them
find . -type f -empty -print -delete
```

## mail
```bash
##1.如何写一般的邮件：

mail test@126.com  Cc 编辑抄送对象，Subject:邮件主题,输入回车，邮件正文后，按Ctrl-D结束

##2.快速发送方式：
echo "邮件正文" | mail -s 邮件主题 591465908@qq.com

##3.以文件内容作为邮件正文来发送：
 mail -s test test@126.com < test.txt

##4.发送带附件的邮件：
uuencode 附件名称 附件显示名称 | mail -s 邮件主题 发送地址

##例如： uuencode test.txt test.txt | mail -s Test test@126.com
```


## Release Cached RAM

```bash
echo 1 > /proc/sys/vm/drop_caches
```

## record screen as gif

```bash
byzanz-record -d 40 -x 0 -y 0 -w 400 -h 320 byzanz-demo.gif

其中：

    -d 40 为录制的时长为 40 秒
    -x 0 录制区域的横坐标
    -y 0 录制区域的纵坐标，记住：屏幕右上角为原点（0,0）
    -w 400 录制区域的宽度
    -h 320 录制区域的高度

byzanz-demo.gif 保存的文件名

####snap shout

xwd -silent -root | convert xwd:- -crop 800x600+0+76 test.png
```


## for fun

```bash
banner
figlet
toilet
```

## case
```bash
##Case

case $Random in
1)
/media/ken/Data/Python-Voice/speak.sh "WARNNING!"
;;
2)
/media/ken/Data/Python-Voice/speak.sh "PLEASE_HELP_ME!"
;;
3)
/media/ken/Data/Python-Voice/speak.sh "WARNNING!"
/media/ken/Data/Python-Voice/speak.sh "I_DONT_WANT_TO_GO"
esac

pstree -up

##参数选择：
##-A  ：各程序树之间以 ASCII 字元來連接；
##-p  ：同时列出每个 process 的 PID；
##-u  ：同时列出每个 process 的所屬账户名称。
```


<a name="8BgJE"></a>
## Time


```bash
##https://www.cnblogs.com/janezhao/p/9732157.html
time1=$(date)
echo $time1

time2=$(date "+%Y%m%d%H%M%S")
echo $time2
##20180930155515
```


<a name="ZneEZ"></a>
## Font
reference: [某某某的账号](https://blog.csdn.net/u013214671)
```bash
##查看所有字体：
fc-list

##查看中文字体
fc-list :lang=zh
```

## stat
[海王 2011](https://www.cnblogs.com/leaven/archive/2011/09/28/2194199.html)
```bash
stat public/
```
<pre>
  File: public/
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: 802h/2050d	Inode: 348256      Links: 1
Access: (0777/drwxrwxrwx)  Uid: ( 1000/     ken)   Gid: ( 1000/     ken)
Access: 2020-07-29 23:57:44.005512600 +0800
Modify: 2020-07-29 23:57:43.560542100 +0800
Change: 2020-07-29 23:57:43.560542100 +0800
 Birth: -
</pre>

## SCP

```bash
## Download files from server
scp -P 8022 root@192.168.3.6:~/test.md .

## Upload files to server
scp -P 8022 test.md root@192.168.3.6:~/
```


## 查看硬件
<a name="IPgOq"></a>
### CPU
```bash
lscpu

### 网卡
lspci | grep -i 'eth'
```

### GPU inf

```bash
lspci| grep -i vga  # Check the GPU at prsent
```


## Mount remate file system

```bash
ssh-keygen -t rsa

sudo apt install sshfs
sudo mkdir /mnt/cypress

sudo sshfs -o allow_other,IdentityFile=~/.ssh/id_rsa wliu15@cypress.tulane.edu:/lustre/project/wdeng7/wliu15/ /mnt/cypress/
```
