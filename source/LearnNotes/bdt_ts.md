---
title: Thermal Fisher BigDye v3.1 中文翻譯
url: bdt_ts
date: 2020/09/22
---

# Question and Answer
[Link](https://www.thermofisher.com/search/results?query=4337458&persona=DocSupport&type=Product+FAQs&resultPage=1&resultsPerPage=60)

1. 多久做一次 pGEM 质控呢?
    <details  >
    <summary> 答案 </summary>
    pGEM 和 M13 (试剂盒自带). pGEM 和 M13 是用来做问题排查的.
    你可以用他来排查样本质量, 循环次数, 或者测序前清洗(沉淀)反应 的问题来优化你的实验.
    </details>

2. BDT v1.1 和 v3.1 的区别
    <details  >
    <summary> 答案 </summary>
    荧光染料不一样, dNTP 和 ddNTP 的比例也不一样.

    1.1 对短片段更有效, 它可以读取离引物更近的区域
    3.1 更擅长读取长片段
    </details>

3. 上哪儿可以获取更多的DNA测序知识?
    <details  >
    <summary> 答案 </summary>
    ThermoFisher 的网站已经提供了很多测序知识.
    此外, 你还可以在:

    - Sanger Sequencing Overview (https://www.thermofisher.com/us/en/home/life-science/sequencing/sanger-sequencing/applications.html)    
    - DNA Sequencing by Capillary Electrophoresis Guide (http://tools.thermofisher.com/content/sfs/manuals/cms_041003.pdf)
    - Seq It Out Video Series (https://www.thermofisher.com/us/en/home/life-science/sequencing/sequencing-education/seq-it-out.html)
    - For additional resources, please see the Guides and Tools section on this page (http://www.thermofisher.com/us/en/home/technical-resources/technical-reference-library/capillary-electrophoresis-applications-support-center/sanger-sequencing-support.html).
    </details>

4. 有什么辅助引物设计的软件吗?
    <details  >
    <summary> 答案 </summary>
    ThermoFisher 推出了 Primer Designer™ 工具. 这是一款免费的在线工具.

    [链接](http://www.thermofisher.com/us/en/home/life-science/sequencing/sanger-sequencing/pre-designed-primers-pcr-sanger-sequencing.html?CID=primerdesigner)
    </details>

5. 我可以稀释我的 BDT 反应嘛?
    <details  >
    <summary> 答案 </summary>
    我们提供了  BigDye™ Terminator v1.1 & v3.1 5X Buffer 来稀释 BDT. 但是稀释可能减弱测序的质量. 我们无法保证稀释后的测序质量.
    </details>

6.  BDT 反应中应该加多少的引物?
    <details  >
    <summary> 答案 </summary>
    引物的浓度应该保持在 3.2 pmoles.
    如果反应体系被稀释了, 应该重新寻找最适引物浓度
    </details>

7. 我应该在什么时候使用 BigDye&#153 Terminator v3.1 Cycle Sequencing Kit?
    <details  >
    <summary> 答案 </summary>
    如果您需要测序长片段
    </details>
8. 试剂盒带的pGEM 和 M13 的阳性对照 的浓度是多少?
    <details  >
    <summary> 答案 </summary>

    - pGEM 浓度是 200ng/uL;
    - M13 的浓度是 0.8 pmol/uL
    </details>
9. 我该如何选择 1.1 还是 3.1?
    <details  >
    <summary> 答案 </summary>
    1.1 更适合片段在700-750 左右的序列, 并且读取的区域更靠近引物.
    3.1 在首端30-50bp的序列质量较低. 在最优的效率下, 可读取 1,200bp 的序列.
    </detail>

10. GC-rich 的片段测序失败了, 有什么办法嘛?
    <details  >
    <summary> 答案 </summary>
    当测序高 GC 序列的时候, 你可以试试下面的操作:

    - 用 1x 或者 0.5x BDT 去做. 过多稀释BDT会降低长GC片段测序的成功率.
    - 98℃ 到 99℃预变性5min
    - 用 5% 的 DMSO 或者新鲜的甜菜碱 添加入反应中
    - 使用 dGTP BigDye Terminator Cycle Sequencing 试剂盒.
    当存在 ddGTP 存在的时候, G峰会被减弱. 但是对于长GC富集片段, 它的成功率比普通的BDT要高. (Cat. No. 4305080, Rev. C)

11. 我可以直接测序 RNA 嘛?
    <details  >
    <summary> 答案 </summary>
    不能. 反转录吧
    </details>
12. 我可以购买pGEM标准品嘛?
    <details  >
    <summary> 答案 </summary>
    不卖~
    </details>

13. BDT mix 里面有啥呀?
    <details  >
    <summary> 答案 </summary>
    dNTP, 荧光标记的ddNTP, 缓冲液, 和其他东西. 特殊的成分是我们的专利
    </details>

14. 当我上传数据到 Genetic Analysis Technical Support, 那些是必须的?
    <details  >
    <summary> 答案 </summary>

    - 机器型号和序列号;
    - 使用软件的版本号
    - Application and/or 试剂盒的信息
    - 试剂盒的编号 (lot number)
    - 毛细管或组的运行号
    - 胶的类型和编号
    - Buffer 的编号
    - .... 啥呀- - 感觉没用, 不翻译了
    </details>

15. 个期样本的保存时间和温度?
    <details  >
    <summary> 答案 </summary>

    - 测序之后, 样本可以保存在4℃过夜, 或者 -15℃/-25℃ 长期保存.

    - 在用 Centri-Sep™ 或者 以纯纯化后, 干燥样本, 用 MicroAmp™ Clear Adhesive Film 封住,避光保存 4℃ 过夜, 或者 -20℃ 知道使用.

    - 在 BigDye™ Xterminator 纯化后, 最多保存10天,用 MicroAmp™ Clear Adhesive Film 封好, 4℃ 短期或者 -20 长期. BDX 板可在室温存放 48 小时.
    </detials>
16. 
