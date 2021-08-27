---
title: "WGCNA - 實戰"
description: "WGCNA - 實戰"
url: wgcna2
date: 2020/06/10
toc: true
excerpt: "WGCNA in action."
tags: [R, Bioinformatics, WGCNA]
category: [R, Bio, WGCNA]
cover: 'https://i.loli.net/2020/06/08/wrpXGJj4qQOulim.png'
thumbnail: 'https://i.loli.net/2020/06/08/wrpXGJj4qQOulim.png'
priority: 10000
---

## WGCNA - 實戰

## 0. 數據結構

### 0.1 Expression matrix
Trinity script TPM result

|ID1|ID2|Liver_CK|Intest_CK|Muscle_CK|Liver_30|Intest_30|Muscle_30|Liver_75|Intest_75|Muscle_75|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|TRINITY_DN100000_c1_g1|TRINITY_DN100000_c1_g1_i1|2.1|4.3|1.32|1.04|4.49|2.85|3.59|4.27|1.7|
|TRINITY_DN100001_c0_g1|TRINITY_DN100001_c0_g1_i1|0.45|21.0|0.02|0.15|8.85|4.33|0.18|14.76|0.0|
|TRINITY_DN100002_c0_g1|TRINITY_DN100002_c0_g1_i1|8.39|2.01|1.08|11.32|3.2|1.1|7.83|6.23|2.91|

### 0.2 Traits
|ID|Group|Organ|Weight|
|:---:|:---:|:---:|:---:|
|Liver_CK|CK|Liver|33.32|
|Intest_CK|CK|Intest|33.32|
|Muscle_CK|CK|Muscle|33.32|
|Liver_30|SPC30|Liver|31.3|
|Intest_30|SPC30|Intest|31.3|
|...|...|...|...|


## 1. Data Clean

### 1.1 Load and Filter
```r
library(WGCNA)

A <- read.csv("All_isoform.TPM.matrix.anno.xls",sep='\t')

## rownames:sample; colnames: Transcripts
row.names(A) = A[[2]]
A = A[-(1:2)]
datExpr0 = t(A)


## Data filter
gsg = goodSamplesGenes(datExpr0, verbose = 3);
gsg$allOK

if (!gsg$allOK)
{
  # Optionally, print the gene and sample names that were removed:
  if (sum(!gsg$goodGenes)>0)
     printFlush(paste("Removing genes:", paste(names(datExpr0)[!gsg$goodGenes], collapse = ", ")));
  if (sum(!gsg$goodSamples)>0)
     printFlush(paste("Removing samples:", paste(rownames(datExpr0)[!gsg$goodSamples], collapse = ", ")));
  # Remove the offending genes and samples from the data:
  datExpr0 = datExpr0[gsg$goodSamples, gsg$goodGenes]
}
```
### 1.2 Clust

```r
sampleTree = hclust(dist(datExpr0), method = "average");
##png(file = "sampleClustering_T45.png",wi=300, he=300)
par(cex = 0.6);
par(mar = c(0,4,2,0))
plot(sampleTree, main = "Sample clustering to detect outliers", sub="", xlab="", cex.lab = 1.5,
     cex.axis = 1.5, cex.main = 2)
##dev.off()
```
![sampleClustering](https://i.loli.net/2020/06/10/PXY8AC1jcZiHlBQ.png)
相對來說， Liver30 異質性有點大， 不過， 根據實驗來說， 應該是正常現象，因此跳過刪除異質性項。

```r
datExpr =  datExpr0
nGenes = ncol(datExpr)
nSamples = nrow(datExpr)

```

### 1.3 Loading Traits

```r
traitData = read.csv("traits.csv")

allTraits = traitData[-c(2,3)]


Samples = rownames(datExpr);
traitRows = match(Samples, allTraits$ID);
datTraits = allTraits[traitRows, -1];
rownames(datTraits) = allTraits[traitRows, 1];

collectGarbage()

## Re-cluster samples
sampleTree2 = hclust(dist(datExpr), method = "average")
## Convert traits to a color representation: white means low, red means high, grey means missing entry
traitColors = numbers2colors(datTraits, signed = FALSE);
## Plot the sample dendrogram and the colors underneath.
## png("traits_heatmap.png")
plotDendroAndColors(sampleTree2, traitColors,
                    groupLabels = names(datTraits),
                    main = "Sample dendrogram and trait heatmap")
```
![traits_heatmap](https://i.loli.net/2020/06/10/mwHBczOjh4TVFNp.png)

ummm, 並不能看出什麼來。只是個普通的熱圖加樹衛而已

## 2. Network construction and module detection
### 2.1 Pick soft-thresdholding power
```r
powers = c(c(1:10), seq(from = 12, to=20, by=2))
## Call the network topology analysis function
sft = pickSoftThreshold(datExpr, powerVector = powers, verbose = 5)
## Plot the results:
sizeGrWindow(9, 5)
##png("sorft_Thread.png",wi=630,he=350)
## Scale-free topology fit index as a function of the soft-thresholding power
## png("T45_Soft_th.png",width=500,height=300)
cex1 = 0.9;
par(mfrow = c(1,2));
plot(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],
     xlab="Soft Threshold (power)",ylab="Scale Free Topology Model Fit,signed R^2",type="n",
     main = paste("Scale independence"));
text(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],
     labels=powers,cex=cex1,col="red");
## this line corresponds to using an R^2 cut-off of h
abline(h=0.90,col="red")
## Mean connectivity as a function of the soft-thresholding power
plot(sft$fitIndices[,1], sft$fitIndices[,5],
     xlab="Soft Threshold (power)",ylab="Mean Connectivity", type="n",
     main = paste("Mean connectivity"))
text(sft$fitIndices[,1], sft$fitIndices[,5], labels=powers, cex=cex1,col="red")
##dev.off()
```
![sorft_Thread](https://i.loli.net/2020/06/10/jh13CuI86y9Sfbg.png)

ummm... 等了半天，就這。。。這種垃圾數據的話， 還是放棄把。

## 3. 刪除不必要reads，再來做一遍

想法： 刪除低hit的reads， 減少計算量，減少垃圾數據的污染
```r
Counts <- read.csv("/media/ken/Data/Yan/RNA-seq/report/4.exprs//All_isoform.COUNT.matrix.anno.xls",sep='\t')
Counts$Sum = rowSums(Counts[-c(1:2)])
Counts_sub = Counts[which(Counts$Sum>10),]
paste(round((nrow(Counts_sub)/nrow(Counts))*100,2),"%",sep="")

A_sub <- A[match(Counts_sub[[2]],rownames(A)),]
```
然後， 重複上面步驟, 從1.1 `datExpr0 = t(A)`替換成`datExpr0 = t(A_sub)`開始
![Soft_th2](https://i.loli.net/2020/06/10/uEx8fr32wglcOIK.png)
鐺鐺鐺鐺鐺! 這次結果就好看多了把！
雖然沒有 Tutorial 那樣標緻，但是，至少給了我繼續下去的勇氣。
數據不好，就調高閾值把， 更具這條線，大概是要選9了

## 4. One-step NetWork
```r
net = blockwiseModules(datExpr, power = 9,
                       TOMType = "unsigned", minModuleSize = 30,
                       reassignThreshold = 0, mergeCutHeight = 0.25,
                       numericLabels = TRUE, pamRespectsDendro = FALSE,
                       saveTOMs = TRUE,
                       saveTOMFileBase = "femaleMouseTOM",
                       verbose = 3)
```
這一步等待時間和你電腦計算能力，基因數量成正相關

```r

moduleLabels = net$colors
moduleColors = labels2colors(net$colors)
MEs = net$MEs;
geneTree = net$dendrograms[[1]]
## open a graphics window
sizeGrWindow(12, 9)
## png('modules_tree.png',width=480, height=320)
## Convert labels to colors for plotting
mergedColors = labels2colors(net$colors)
## Plot the dendrogram and the module colors underneath
plotDendroAndColors(net$dendrograms[[1]], mergedColors[net$blockGenes[[1]]],
                    "Module colors",
                    dendroLabels = FALSE, hang = 0.03,
                    addGuide = TRUE, guideHang = 0.05)
##dev.off()
```
![modules_tree](https://i.loli.net/2020/06/10/HYXmnS3acVgPOyU.png)

ummmm... 模塊似乎有點寬， 分的不均勻- - 感覺很爛的樣子。 要不再， 篩一下？

Modules 統計
```r
library(ggplot2)
library(reshape2)
Color_TB = melt(table(labels2colors(net$colors)))
Color_TB$Var1 = factor(Color_TB$Var1, levels = Color_TB$Var1[order(Color_TB$value,decreasing = T)])
ggplot(Color_TB) + geom_bar(aes(x=Var1,y=value), stat = 'identity',fill=Color_TB$Var1)+
  theme_light() +theme(axis.text.x = element_text(angle = 90,hjust=1))
```
![123](https://i.loli.net/2020/06/11/Ks396OUztmydnu2.png)

## 5. Traits
```r
nGenes = ncol(datExpr);
nSamples = nrow(datExpr);
## Recalculate MEs with color labels
MEs0 = moduleEigengenes(datExpr, moduleColors)$eigengenes
MEs = orderMEs(MEs0)
moduleTraitCor = cor(MEs, datTraits, use = "p");
moduleTraitPvalue = corPvalueStudent(moduleTraitCor, nSamples);


sizeGrWindow(10,6)
## Will display correlations and their p-values
## png("T45_traits_heatmap.png",width=1000,height=600)
textMatrix =  paste(signif(moduleTraitCor, 2), "\n(",
                           signif(moduleTraitPvalue, 1), ")", sep = "");
dim(textMatrix) = dim(moduleTraitCor)
par(mar = c(6, 8.5, 3, 3));
## Display the correlation values within a heatmap plot
labeledHeatmap(Matrix = moduleTraitCor,
               xLabels = names(datTraits),
               yLabels = names(MEs),
               ySymbols = names(MEs),
               colorLabels = FALSE,
               colors = greenWhiteRed(50),
               textMatrix = textMatrix,
               setStdMargins = FALSE,
               cex.text = 0.5,
               zlim = c(-1,1),
               main = paste("Module-trait relationships"))
```
![traits_heatmap](https://i.loli.net/2020/06/10/6sAcpShBmkZXGyW.png)
ummm, 能看個大概就好2333.還是有點意思的

## 6. Focus on Weight

```r
weight = as.data.frame(datTraits$Weight)
modNames = substring(names(MEs), 3)

geneModuleMembership = as.data.frame(cor(datExpr, MEs, use = "p"));
MMPvalue = as.data.frame(corPvalueStudent(as.matrix(geneModuleMembership), nSamples));

names(geneModuleMembership) = paste("MM", modNames, sep="");
names(MMPvalue) = paste("p.MM", modNames, sep="");

geneTraitSignificance = as.data.frame(cor(datExpr, weight, use = "p"));
GSPvalue = as.data.frame(corPvalueStudent(as.matrix(geneTraitSignificance), nSamples));

names(geneTraitSignificance) = paste("GS.", names(weight), sep="");
names(GSPvalue) = paste("p.GS.", names(weight), sep="");


module = "grey"
column = match(module, modNames);
moduleGenes = moduleColors==module;

sizeGrWindow(7, 7);
## png("grey_weight.png")
par(mfrow = c(1,1));
verboseScatterplot(abs(geneModuleMembership[moduleGenes, column]),
                   abs(geneTraitSignificance[moduleGenes, 1]),
                   xlab = paste("Module Membership in", module, "module"),
                   ylab = "Gene significance for body weight",
                   main = paste("Module membership vs. gene significance\n"),
                   cex.main = 1.2, cex.lab = 1.2, cex.axis = 1.2, col = module)
```
![grey_weight](https://i.loli.net/2020/06/10/jWYKMUZ1o4gqQu5.png)
ummmm... 有點少， 哈哈哈， 才18個，數了一下。和tutorial 差好多呀

因爲是非模式物種，所以無法直接用tutorial給的方法做註釋。
直接調到後面的可視化把。

## 7. NetWork  Visualizing

```r
nGenes = ncol(datExpr)
nSamples = nrow(datExpr)

## Calculate topological overlap anew: this could be done more efficiently by saving the TOM
## calculated during module detection, but let us do it again here.
dissTOM = 1-TOMsimilarityFromExpr(datExpr, power = 9);
## Transform dissTOM with a power to make moderately strong connections more visible in the heatmap
plotTOM = dissTOM^7;
## Set diagonal to NA for a nicer plot
diag(plotTOM) = NA;
## Call the plot function
sizeGrWindow(9,9)
TOMplot(plotTOM, geneTree, moduleColors, main = "Network heatmap plot, all genes")

nSelect = 400
## For reproducibility, we set the random seed
set.seed(10);
select = sample(nGenes, size = nSelect);
selectTOM = dissTOM[select, select];
## There's no simple way of restricting a clustering tree to a subset of genes, so we must re-cluster.
selectTree = hclust(as.dist(selectTOM), method = "average")
selectColors = moduleColors[select];
## Open a graphical window
sizeGrWindow(9,9)
## Taking the dissimilarity to a power, say 10, makes the plot more informative by effectively changing
## the color palette; setting the diagonal to NA also improves the clarity of the plot
##png('123.png')
plotDiss = selectTOM^7;
diag(plotDiss) = NA;
TOMplot(plotDiss, selectTree, selectColors, main = "Network heatmap plot, selected genes")
```
ummm... 好像是內存爆了，直接退出。 試試不用radian看看
<span style="background:salmon">失敗了- -放棄， 跳過把</span>
參考圖：
![123](https://i.loli.net/2020/06/08/wrpXGJj4qQOulim.png)


```r
MEs = moduleEigengenes(datExpr, moduleColors)$eigengenes
## Isolate weight from the clinical traits
weight = as.data.frame(datTraits$Weight);
names(weight) = "weight"
## Add the weight to existing module eigengenes
MET = orderMEs(cbind(MEs, weight))
## Plot the relationships among the eigengenes and the trait
sizeGrWindow(5,7.5);
##png('T45_Tree_weight_module.png',width=400,height=600)
par(cex = 0.9)
plotEigengeneNetworks(MET, "", marDendro = c(0,4,1,2), marHeatmap = c(3,4,1,2), cex.lab = 0.8, xLabelsAngle = 90)
```
![tTvZu9.png](https://s1.ax1x.com/2020/06/10/tTvZu9.png)

這個圖還是可以畫的
## 8. 數據導出

```r
modules = c("darkorange2", "grey","lightcyan");
inModule = is.finite(match(moduleColors, modules));

for(color in modules){
  write.table(colnames(t(net$colors[moduleColors==color])),paste("module_",color,'.list',sep="") ,row.names=F,quote=F,col.names=F)
}

probes = names(datExpr)

## Recalculate topological overlap if needed
TOM = TOMsimilarityFromExpr(datExpr, power = 9);
## Read in the annotation file
annot = read.csv(file = "GeneAnnotation.csv");
## Select modules
## Select module probes
modProbes = probes[inModule];
modGenes = annot$gene_symbol[match(modProbes, annot$substanceBXH)];
## Select the corresponding Topological Overlap
modTOM = TOM[inModule, inModule];
dimnames(modTOM) = list(modProbes, modProbes)
## Export the network into edge and node list files Cytoscape can read
cyt = exportNetworkToCytoscape(modTOM,
  edgeFile = paste("CytoscapeInput-edges-", paste(modules, collapse="-"), ".txt", sep=""),
  nodeFile = paste("CytoscapeInput-nodes-", paste(modules, collapse="-"), ".txt", sep=""),
  weighted = TRUE,
  threshold = 0.02,
  nodeNames = modProbes,
  altNodeNames = modGenes,
  nodeAttr = moduleColors[inModule]);
```
## 9. 如果 softThread 還是取6

### Modules 分佈
```r
library(ggplot2)
library(reshape2)
library(patchwork)
Color_TB = melt(table(labels2colors(net$colors)))
Color_TB$Var1 = factor(Color_TB$Var1, levels = Color_TB$Var1[order(Color_TB$value,decreasing = T)])
p<- ggplot(Color_TB) + geom_bar(aes(x=Var1,y=value), stat = 'identity',fill=Color_TB$Var1)+
  theme_light() +theme(axis.text.x = element_text(angle = 90,hjust=1))

SplitBar(p,8500,10000,27000,0,c(1,4))  
```
<span style="background:salmon">畫圖函點擊</span>[SplitBar](https://www.yuque.com/liuwenkan/blog/ggplot_splitbar)
![123](https://i.loli.net/2020/06/11/pr5GuX3Z27dHkiz.png)

![S6_modules_tree](https://i.loli.net/2020/06/11/eLtsGyoIViqhdJ7.png)

## Optimal

### A1. Reduce Input Transcripts

這裏， 我們把閾值設定在 45(9*5)
```r
library(WGCNA)

A <- read.csv("All_isoform.TPM.matrix.anno.xls",sep='\t')
## rownames:sample; colnames: Transcripts
row.names(A) = A[[2]]
A = A[-(1:2)]

Counts <- read.csv("/media/ken/Data/Yan/RNA-seq/report/4.exprs//All_isoform.COUNT.matrix.anno.xls",sep='\t')
Counts$Sum = rowSums(Counts[-c(1:2)])
Counts_sub = Counts[which(Counts$Sum>45),]
paste(round((nrow(Counts_sub)/nrow(Counts))*100,2),"%",sep="")

A_sub <- A[match(Counts_sub[[2]],rownames(A)),]

datExpr0 = t(A_sub)

## Data filter
gsg = goodSamplesGenes(datExpr0, verbose = 3);
gsg$allOK

if (!gsg$allOK)
{
  # Optionally, print the gene and sample names that were removed:
  if (sum(!gsg$goodGenes)>0)
     printFlush(paste("Removing genes:", paste(names(datExpr0)[!gsg$goodGenes], collapse = ", ")));
  if (sum(!gsg$goodSamples)>0)
     printFlush(paste("Removing samples:", paste(rownames(datExpr0)[!gsg$goodSamples], collapse = ", ")));
  # Remove the offending genes and samples from the data:
  datExpr0 = datExpr0[gsg$goodSamples, gsg$goodGenes]
}
```
剩下了`"32.96%"`的 Transcripts

接下來退回到1.2

![T45_Soft_th](https://i.loli.net/2020/06/11/vSlio9atZdUREDe.png)
ummmm, 好像還沒之前的好看了- -，

還是取9把，soft

modules 29 個。
traits聚類：

|Cluster1|Cluster2|
|:---:|:---:|
|![T45_traits_heatmap](https://i.loli.net/2020/06/11/2zYmxMo7ARr3y9L.png)|![tHgxTs.png](https://s1.ax1x.com/2020/06/11/tHgxTs.png)|


最亮的沒有上次那麼亮，= =相關係數有點低， 不高

modules 分佈情況:

![tmp](https://i.loli.net/2020/06/11/F95UNu6cLeAD8Jb.png)


## B. Remove low-hits & Non-DEGs


```r
library(WGCNA)

A <- read.csv("All_isoform.TPM.matrix.anno.xls",sep='\t')
## rownames:sample; colnames: Transcripts
row.names(A) = A[[2]]
A = A[-(1:2)]

Counts <- read.csv("/media/ken/Data/Yan/RNA-seq/report/4.exprs//All_isoform.COUNT.matrix.anno.xls",sep='\t')
Counts$Sum = rowSums(Counts[-c(1:2)])
Counts_sub = Counts[which(Counts$Sum>9),]
paste(round((nrow(Counts_sub)/nrow(Counts))*100,2),"%",sep="")

A_sub <- A[match(Counts_sub[[2]],rownames(A)),]

DEG1 <- read.table("../edgeR_Intest/diffExpr.P1e-3_C2.matrix",head=T)
DEG2 <- read.table("../edgeR_Liver/diffExpr.P1e-3_C2.matrix",head=T)
DEG3 <- read.table("../edgeR_Muscle/diffExpr.P1e-3_C2.matrix",head=T)

List = as.character(unique(DEG1[[1]], DEG2[[1]], DEG3[[1]]))

A_DEG = na.omit(A_sub[match(row.names(A_sub), List),])

datExpr0 = t(A_DEG)

## Data filter
gsg = goodSamplesGenes(datExpr0, verbose = 3);
gsg$allOK

if (!gsg$allOK)
{
  # Optionally, print the gene and sample names that were removed:
  if (sum(!gsg$goodGenes)>0)
     printFlush(paste("Removing genes:", paste(names(datExpr0)[!gsg$goodGenes], collapse = ", ")));
  if (sum(!gsg$goodSamples)>0)
     printFlush(paste("Removing samples:", paste(rownames(datExpr0)[!gsg$goodSamples], collapse = ", ")));
  # Remove the offending genes and samples from the data:
  datExpr0 = datExpr0[gsg$goodSamples, gsg$goodGenes]
}
```
跳回 1.2
ummmm, 這麼篩完以後， 剩下了`1105`個Transcripts 。。。


|聚類|Soft圖|
|:---:|:---:|
|這次聚類結果，就很不一樣了|不過sortpower這個圖，基本還是和前文一樣沒怎麼變。取0.9以上的話， 又得取10了|
|![tbo3UU.png](https://s1.ax1x.com/2020/06/11/tbo3UU.png)|![tbo1ET.png](https://s1.ax1x.com/2020/06/11/tbo1ET.png)|

還是去9吧。 1000個，秒算完。
先看看分組頻率 和樹圖
這個圖，我就覺得，看着舒服多了- -唉
|聚類|Soft圖|
|:---:|:---:|
|![DEG_bar](https://i.loli.net/2020/06/11/hUMPXSTErxqBI9n.png)|![DEG_tree](https://i.loli.net/2020/06/11/hWnYQKlG1HpdqPU.png)|
|第一次畫出Tomplot，激動|這個聚類，相關性都不太高呀|
|![DEG_tomplot](https://i.loli.net/2020/06/11/PGng6FisKjfvJ48.png)|![DEG_Tree_weight_module](https://i.loli.net/2020/06/11/IZJjsXWo2AmlHxU.png)|
![DEG_traits_heatmap](https://i.loli.net/2020/06/11/E3GxfJa8T2VNRlk.png)

相關性確實是太低了。 我們看一下這1000基因的表達趨勢把。

```r
library(ggplotify)

A_DEG$Module = labels2colors(net$colors)
A_DEG$ID = row.names(A_DEG)

TB = melt(A_DEG,id.vars = c("ID","Module"))
TB$variable = factor(TB$variable,levels=sort(as.character(unique((TB$variable)))))

TB$ID = factor(TB$ID, levels = row.names(A_DEG)[order(A_DEG$Module)])

p2 <- ggplot( TB, aes( variable, ID)) + theme(panel.grid.major = element_blank())+
    theme(legend.key=element_blank(), axis.text.y = element_blank(),
          axis.title=element_blank(),axis.ticks.y=element_blank(),
          axis.text.x=element_text(angle=90,hjust=1))+
    geom_tile(aes(fill=log(1+value)))+
    scale_fill_gradient2(low="steelblue",mid="white",high="red",midpoint =1)

A_DEG$ID = factor(A_DEG$ID, levels = row.names(A_DEG)[order(A_DEG$Module)])
p1 <-ggplot(A_DEG[10:11], aes( x="Module", y=ID)) + theme(panel.grid.major = element_blank())+
    theme(axis.text.y = element_blank(), legend.position =  'left',
        axis.title=element_blank(),axis.ticks.y=element_blank(),
        axis.text.x=element_text(angle=90,hjust=1))+
    geom_tile(fill=A_DEG$Module)

p1+p2 +  plot_layout(design = 'ABBBBBBBBBB')
```
熱圖還是，可以的，就是配色有點麻煩- -
![co_heatmap](https://i.loli.net/2020/06/11/awg2zCr6LpblocB.png)
只管來看， 聚類效果還是OK的把。不過correlation值太低了 = = 有什麼之後再去深究把。

添加樹
打包兩個函數
```r
PLOT2 <- function(dendr){
  ggplot() +
  geom_segment(data=segment(dendr), aes(x=x, y=y, xend=xend, yend=yend)) +
  geom_text(data=label(dendr), aes(x, y, label=label, hjust=0),
           size=3) +
  coord_flip() + scale_y_reverse(expand=c(0.2, 0)) +
  theme(axis.line.y=element_blank(),
        axis.ticks.y=element_blank(),
        axis.text.y=element_blank(),
        axis.title.y=element_blank(),
        panel.background=element_rect(fill="white"),
        panel.grid=element_blank())
}

LS_judg<- function(TB){
  if (TB['x'] == TB['xend']){
    R = 'v'
  }else{
    R = 'h'
  }
  return(R)
}

TreePlot <- function(dendr, Width_tree){
  dendr$labels$x = Width_tree[dendr$labels$x]
  dendr$segments = dendr$segments[order(dendr$segments$x),]
  # 做個list
  List = c()
  for(i in c(1:length(Width_tree))){
    List = c(List, which(dendr$segments$x==i))
  }
  # 調整豎線
  for( i in c(1:length(dendr$labels$label))){
  Dif_tmp = Width_tree[i]- dendr$segments$x[List[i]]
  dendr$segments$x[List[i]:nrow(dendr$segments)] = dendr$segments$x[List[i]:nrow(dendr$segments)]+Dif_tmp
  dendr$segments$xend[List[i]:nrow(dendr$segments)] = dendr$segments$xend[List[i]:nrow(dendr$segments)]+Dif_tmp
  }
  # 刪除添加新的橫線
  dendr$segments = dendr$segments[dendr$segments$x == dendr$segments$xend,]
  Y_list = dendr$segments$y[duplicated(dendr$segments$y)]
  for(i in Y_list){  
  tmp = (dendr$segments$x[dendr$segments$y  == i])
  dendr$segments = rbind(dendr$segments, data.frame(x=tmp[1],y=i,xend=tmp[2],yend=i))
  }
  Seg = dendr$segments
  for( i in c(nrow(dendr$segments):1)){
    if(LS_judg(dendr$segments[i,]) == 'h'){
      tmpy = dendr$segments[i,]$y
      tmpTB = Seg[Seg$yend== tmpy,]
        for( ii in c(1:nrow(tmpTB))){
        if(LS_judg(tmpTB[ii,]) == 'v'){
          Num = rownames(tmpTB[1,])
          dendr$segments[match(Num, row.names(dendr$segments)),][c(1,3)] = sum(Seg[i,c('x','xend')])/2
        }
      }
    }
  }
  # 重画横线：
  dendr$segments = dendr$segments[dendr$segments$x == dendr$segments$xend,]
  Y_list = dendr$segments$y[duplicated(dendr$segments$y)]
  for(i in Y_list){  
  tmp = (dendr$segments$x[dendr$segments$y  == i])
  dendr$segments = rbind(dendr$segments, data.frame(x=tmp[1],y=i,xend=tmp[2],yend=i))
  }
 return(dendr)
}
```

#### 画图
```r
library(ggplot2)
library(ggdendro)
library(reshape2)
library(patchwork)
library(RColorBrewer)

colorRampPalette(rev(brewer.pal(n = 7,name = "RdYlBu"))) -> cc

TB_color = (data.frame(net$colors,color=labels2colors(net$colors)))
A_DEG$ID = row.names(A_DEG)
A_DEG$Module = TB_color$color[match(row.names(A_DEG), row.names(TB_color))]

## Samples dendrogram
hc <- hclust(dist(t(A_DEG[1:9])))
dendr_head <- dendro_data(hc, type="rectangle") # convert for ggplot


## Module dendrogram
hc <- hclust(dist(t(MEs)))
dendr <- dendro_data(hc, type="rectangle") # convert for ggplot

### 1. order and list
Module_list = as.character(dendr$labels$label[order(dendr$labels$x)])
Module_or = c()
for( i in strsplit(Module_list,'ME')){
  Module_or = c(Module_or, i[2])
}

### 2. Axis location
TB_mbar = data.frame(table(A_DEG$Module))
TB_mbar = TB_mbar = data.frame(table(A_DEG$Module))
TB_mbar$hei = TB_mbar$Freq[1]/2

for(i in c(2:nrow(TB_mbar))){
  TB_mbar$hei[i] =sum(TB_mbar$Freq[1:i-1])+ (TB_mbar$Freq[i]/2)
}

Width_tree = TB_mbar$hei

AA <- TreePlot(dendr, Width_tree)


## Module Bar

### acquiring module list

## order module
A_DEG$Module = factor(A_DEG$Module, levels = Module_or)
## order ID
A_DEG$ID = factor(A_DEG$ID, levels = row.names(A_DEG)[order(A_DEG$Module)])

## Transcripts Heatmap

primary_data = as.matrix(A_DEG[1:9])
##transformations
data = log2(primary_data+1)
data = as.matrix(data) # convert to matrix
## Centering rows
data = data.frame(t(scale(t(data), scale=F)))

TB = melt(cbind(data,A_DEG[c("ID","Module")]),id.vars = c("ID","Module"))
TB$ID = factor(TB$ID, levels = row.names(A_DEG)[order(A_DEG$Module)])
TB$variable = factor(TB$variable, levels =levels(dendr_head$labels$label))


p0 <- ggplot() +
      geom_segment(data=segment(AA), aes(x=x, y=y, xend=xend, yend=yend)) +
      geom_text(data=label(AA), aes(x, y, label=label, hjust=0),
               size=3) +
      coord_flip() + scale_y_reverse(expand=c(0.7, 0)) +
      theme(axis.line.y=element_blank(),
            axis.ticks.y=element_blank(),
            axis.text.y=element_blank(),
            axis.title =element_blank(),
            panel.background=element_rect(fill="white"),
            panel.grid=element_blank())

p1 <-ggplot(A_DEG[10:11], aes( x="Module", y=ID)) +
    theme(panel.grid.major = element_blank())+
    theme(axis.text.y = element_blank(), legend.position =  'left',
        axis.title=element_blank(),
        axis.ticks=element_blank(),
        panel.background=element_rect(fill="white"),
        axis.text.x=element_text(angle=90,hjust=1))+
    geom_tile(fill=A_DEG$Module)

p2 <- ggplot( TB, aes( variable, ID)) +
    theme(panel.grid.major = element_blank())+
    theme(legend.key=element_blank(), axis.text.y = element_blank(),
    axis.title=element_blank(),axis.ticks.y=element_blank(),
    axis.text.x=element_text(angle=90,hjust=1))+
    geom_tile(aes(fill=value))+
    scale_fill_gradientn(colors=cc(100))

p4 <- ggplot() +
          geom_segment(data=segment(dendr_head), aes(x=x, y=y, xend=xend, yend=yend)) +
          scale_y_reverse(expand=c(0, 0)) +
          theme(axis.line.y=element_blank(),
                axis.ticks.x=element_blank(),
                axis.text.x=element_blank(),
                axis.title=element_blank(),
                panel.background=element_rect(fill="white"),
                panel.grid=element_blank())

layout_P <- "
    AAAABCCCCCC
    AAAABCCCCCC
    AAAABCCCCCC
    AAAABCCCCCC
    AAAABCCCCCC
    AAAABCCCCCC
    #####DDDDDD
    "

p0 + p1 + p2 + p4 +  plot_layout(design = layout_P)
```
![DEG_heatmap](https://i.loli.net/2020/06/13/1COSfoY6KJGTFil.png)
