---
url: grep2
---

# grep 搜索


```bash
grep
#Usage: grep [OPTION]... PATTERN [FILE]...
#Try 'grep --help' for more information.
```
**
<a name="90laC"></a>
# 1. 快速上手

```bash
# 创建测试文件
echo -e "ab\na\nb\nc\nd\ne\nf\ng\nA\nB\nC" > test.txt
# 搜索存在'a'的内容
grep a test.txt
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1576918779987-1c0d70fb-b2cb-48f9-b2f3-6a05ce54ec1b.png#align=left&display=inline&height=69&name=image.png&originHeight=69&originWidth=387&size=7223&status=done&style=none&width=387)

---


<a name="HflCw"></a>
# 2. 常用
$gr
```bash
# "."模糊匹配
grep a. test.txt

```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1576918907555-6ef43a95-30ec-425e-97ae-e83e9e3b380a.png#align=left&display=inline&height=48&name=image.png&originHeight=48&originWidth=402&size=6883&status=done&style=none&width=402)

```bash
# 显示所在行
grep -n a test.txt
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1576919022227-47a23c0c-5bad-4be4-823f-448f5f0dff49.png#align=left&display=inline&height=66&name=image.png&originHeight=66&originWidth=419&size=7478&status=done&style=none&width=419)

```bash
# 输出匹配次数(多少行)
grep -c a test.txt
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1576919069484-0afd3a35-6d65-454c-bf09-8cede1e2c1a4.png#align=left&display=inline&height=46&name=image.png&originHeight=46&originWidth=420&size=6729&status=done&style=none&width=420)

```bash
# 忽略大小写
grep -i a test.txt
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1576919125749-edce6b08-b43b-4a06-a966-e0b3113e8088.png#align=left&display=inline&height=87&name=image.png&originHeight=87&originWidth=426&size=7602&status=done&style=none&width=426)

```bash
#多项匹配: "|" 分隔开多选必配项。注意，如果我没记错的话，最多可同时匹配1000项
grep -E 'a|b' test.txt
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1576918734354-b59bc554-1600-4f95-9c2c-1f6e0bfc3e7c.png#align=left&display=inline&height=87&name=image.png&originHeight=87&originWidth=456&size=7993&status=done&style=none&width=456)

```bash
#打印匹配项的上下一行或多行
grep -nA 1 A test.txt # 等同于 grep -n -A 1  A test.txt， -n 用于显示行数
grep -nB 1  A test.txt # 显示匹配的上一行
grep -nA 1 -B 1  A test.txt # 同时显示匹配的上下两行
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1577263820071-67876b87-7f39-4b20-b620-6057d4900048.png#align=left&display=inline&height=220&name=image.png&originHeight=220&originWidth=522&size=26104&status=done&style=none&width=522)<br />**
<a name="pFQtn"></a>
# 3. 快速应用：

抓取fasta序列：<br />测试文件：[test.fa.txt](https://www.yuque.com/attachments/yuque/0/2020/txt/691897/1581071887664-9edb6585-1fc9-4bf3-b5b4-181123b53c33.txt?_lake_card=%7B%22uid%22%3A%221577264129011-0%22%2C%22src%22%3A%22https%3A%2F%2Fwww.yuque.com%2Fattachments%2Fyuque%2F0%2F2020%2Ftxt%2F691897%2F1581071887664-9edb6585-1fc9-4bf3-b5b4-181123b53c33.txt%22%2C%22name%22%3A%22test.fa.txt%22%2C%22size%22%3A6581%2C%22type%22%3A%22text%2Fplain%22%2C%22ext%22%3A%22txt%22%2C%22progress%22%3A%7B%22percent%22%3A99%7D%2C%22status%22%3A%22done%22%2C%22percent%22%3A0%2C%22id%22%3A%22FBFrY%22%2C%22card%22%3A%22file%22%7D)<br />首先，把fasta文件规整成一行ID，一行序列格式。

```bash
#通过一系列骚操作，把多行序列转换成单行
cat test.fa.txt | tr '\n' '#'| sed 's/#>/\n>/g'|sed 's/#/\n/;s/#//g' > test.fa
```

<a name="PfuOk"></a>
## 3.1，获取所有的fasta ID
```bash
grep ">" test.fa
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1577264874420-4595e805-6417-4437-b637-1ee62764e7d9.png#align=left&display=inline&height=178&name=image.png&originHeight=178&originWidth=605&size=49593&status=done&style=none&width=605)

<a name="B2a92"></a>
## 3.2，获取杠内ID
```bash
grep ">" test.fa| awk -F\| '{print $2}'
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1577264982257-2658c5f6-72fb-4d37-b92f-76141d01dd19.png#align=left&display=inline&height=148&name=image.png&originHeight=148&originWidth=635&size=19251&status=done&style=none&width=635)

<a name="frpmZ"></a>
## 3.3，通过grep 多项匹配，获取前两个ID及其序列
```bash
grep -EA 1 $(grep ">" test.fa| awk -F\| '{print $2}'|head -n 2| tr '\n' '|'|sed 's/^/"|/;s/$/"/') test.fa
#or
grep -EA 1 $(grep ">" test.fa|\
awk -F\| '{print $2}'|\
head -n 2|\
tr '\n' '|'|\
sed 's/^/"|/;s/$/"/') test.fa

'''
其中，$(grep ">" test.fa| awk -F\| '{print $2}'|head -n 2| tr '\n' '|'|sed 's/^/"|/;s/$/"/') 的结果为
的结果为：
"|Q6GZX4|Q6GZX3|"
因此可以直接被 grep -E 参数识别
'''
```
![image.png](https://cdn.nlark.com/yuque/0/2019/png/691897/1577265297328-fb1b716d-42cf-4fd0-8217-475a9e16113a.png#align=left&display=inline&height=228&name=image.png&originHeight=228&originWidth=551&size=43981&status=done&style=none&width=551)

<a name="t84Jr"></a>
# 4. 其他详细请看：
参数解释：[https://www.runoob.com/linux/linux-comm-grep.html](https://www.runoob.com/linux/linux-comm-grep.html)<br />复杂正则匹配：[https://www.cnblogs.com/keithtt/p/6820540.html](https://www.cnblogs.com/keithtt/p/6820540.html)
