---
title: "System"
description: "System"
url: system2
---

# System



```bash

Basic


PATH
echo PATH=$PATH:\$PWD >> ~/.bashrc
source ~/.bashrc

PATH
echo PATH=$PATH:\$PWD >> /etc/profile
source /etc/profile

apt-cache search readline

抽出整列  awk '{print $1}' filename 整列打印
awk 'NR=='${fn}'{print}' counts.TMM_normalized.FPKM | awk '{print $2}'

合并成一个文件，两列排列 paste -d "\t" eng.txt chi.txt
Sed
sed -i '1,5d' ${fn}.meg
sed 'y/#/>/' ${fn}.meg
sed
's/原字符串/替换字符串/'

数字大小排序：sort -n  test.txt | while read num ;do echo $num ; sum=`expr $sum + $num 2> /dev/null`; echo $sum > /tmp/sum.tmp ;done ; echo -n "sum is :" ;cat /tmp/sum.tmp
 sort -n C.txt >T.txt

tail
实例3：从第5行开始显示文件
命令：
tail -n +5 log2014.log

　二、去掉所有重复的数据行
cat data1.txt | sort | uniq

./faSomeRecords db.fasta id.txt query.fasta
echo
echo -e "\033[41;36m something here \033[0m"
echo -e "\033[40;37m red \033[0m"
echo -e "\033[41;37m blue \033[0m"
echo -e "\033[42;37m green \033[0m"
echo -e "\033[43;37m 黄底白字 \033[0m"
echo -e "\033[44;37m 蓝底白字 \033[0m"
echo -e "\033[45;37m 紫底白字 \033[0m"
echo -e "\033[46;37m 天蓝底白字 \033[0m"
echo -e "\033[47;30m 白底黑字 \033[0m"

#去除颜色
#http://www.commandlinefu.com/com ... characters-with-sed
sed -r "s:\x1B\[[0-9;]*[mK]::g"



R
Local 装包 R CMD INSTALL limma.tar.gz
install.packages("rJava")
Trinity
Run Trinity
Version 2013.
./../Trinity --seqType fq --max_memory 2G --left reads.left.fq --right reads.right.fq --SS_lib_type FR   -CPU 4


IDSS
~/soft/trinityrnaseq_r20131110/Trinity.pl --seqType fq --max_memory 2G --single ALL.fastaq  --SS_lib_type F   -CPU 4     



RSEM


Ttinity mode:

~/trinityrnaseq-Trinity-v2.4.0/util/align_and_estimate_abundance.pl --transcripts Trinity.fasta --seqType fq --left reads_1.fq --right reads_2.fq --est_method RSEM --aln_method bowtie --trinity_mode --prep_reference --output_dir counts



~/trinityrnaseq-Trinity-v2.4.0/util/align_and_estimate_abundance.pl --transcripts gene_MAP.fasta --seqType fq --single ERR1698194_1.fastq.gz --est_method RSEM --aln_method bowtie2 --trinity_mode --prep_reference --output_dir counts

IDSS

nohup ~/T2-Trinity-v2.5.1/util/align_and_estimate_abundance.pl --transcripts Trinity.fasta --seqType fq --single SRR771602.fastq  --est_method RSEM --prep_reference --aln_method bowtie --trinity_mode --output_dir 0dpe &

Nontrinity mod:
~/trinityrnaseq-Trinity-v2.5.1/Analysis/DifferentialExpression/run_DE_analysis.pl --matrix counts --method edgeR --dispersion 0.1 / --samples filename

~/trinityrnaseq-Trinity-v2.4.0/util/align_and_estimate_abundance.pl --transcripts gene_MAP.fasta --seqType fq --single ERR1698194_1.fastq.gz --est_method RSEM --aln_method bowtie2 --prep_reference --output_dir counts


Differantiation
nohup   &

~/trinityrnaseq-Trinity-v2.5.1/Analysis/DifferentialExpression/analyze_diff_expr.pl --matrix ../RSEM.isoform.TMM.EXPR.matrix -P 1e-3 -C 2

Blast+

makeblastdb -in db.fasta -dbtype prot/nucl -parse_seqids -out dbname

~/ncbi-blast-2.7.1+/bin/blastx -query GP10000.fasta -out blast.out -db ~/data/swissport/uniprot_sprot -outfmt "6 qacc sacc evalue stitle sblastname" -evalue 1e-5 -max_target_seqs 1 -num_threads 8 -max_hsps 1






#1.如何写一般的邮件：

mail test@126.com  Cc 编辑抄送对象，Subject:邮件主题,输入回车，邮件正文后，按Ctrl-D结束

#2.快速发送方式：
echo "邮件正文" | mail -s 邮件主题 591465908@qq.com

#3.以文件内容作为邮件正文来发送：
 mail -s test test@126.com < test.txt

#4.发送带附件的邮件：
uuencode 附件名称 附件显示名称 | mail -s 邮件主题 发送地址

#例如： uuencode test.txt test.txt | mail -s Test test@126.com

## Release Cached RAM
echo 1 > /proc/sys/vm/drop_caches

## for GPU

lspci| grep -i vga  # Check the GPU at prsent



## systen monitor ##
sudo s-tui

## system monitor on window
gnome-system-monitor

byzanz-record -d 40 -x 0 -y 0 -w 400 -h 320 byzanz-demo.gif

其中：

    -d 40 为录制的时长为 40 秒
    -x 0 录制区域的横坐标
    -y 0 录制区域的纵坐标，记住：屏幕右上角为原点（0,0）
    -w 400 录制区域的宽度
    -h 320 录制区域的高度

byzanz-demo.gif 保存的文件名

###snap shout

xwd -silent -root | convert xwd:- -crop 800x600+0+76 test.png

## for fun
banner
figlet
toilet

#scrcpy connect
adb tcpip 5555
adb connect 192.168.3.2:5555



#Case

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

#参数选择：
#-A  ：各程序树之间以 ASCII 字元來連接；
#-p  ：同时列出每个 process 的 PID；
#-u  ：同时列出每个 process 的所屬账户名称。
```


<a name="8BgJE"></a>
# Time


```bash
#https://www.cnblogs.com/janezhao/p/9732157.html
time1=$(date)
echo $time1

time2=$(date "+%Y%m%d%H%M%S")
echo $time2
#20180930155515
```


<a name="ZneEZ"></a>
# Font
reference: [某某某的账号](https://blog.csdn.net/u013214671)
```bash
#查看所有字体：
fc-list

#查看中文字体
fc-list :lang=zh
```
<a name="zracp"></a>
# 查看硬件
<a name="IPgOq"></a>
## CPU
```bash
lscpu

# 网卡
lspci | grep -i 'eth'
```

# SCP

```bash
# Download files from server
scp -P 8022 root@192.168.3.6:~/test.md .

# Upload files to server
scp -P 8022 test.md root@192.168.3.6:~/
```



---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
