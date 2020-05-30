---
url: wgcna2
---

# WGCNA (out of date)


```r
library(WGCNA)
fpkm <- read.table(file = "diffExpr.P1e-2_C2.matrix")
data_matrix_mv = t(fpkm[order(apply(fpkm,1,mad), decreasing = T),])




#2. ѡ����ʵķ�ֵ
powers = c(c(1:10), seq(from = 12, to=20, by=2))
# Call the network topology analysis function
sft = pickSoftThreshold(data_matrix_mv, powerVector = powers, verbose = 5)
# Plot the results:
##sizeGrWindow(9, 5)
par(mfrow = c(1,2));
cex1 = 0.9;
# Scale-free topology fit index as a function of the soft-thresholding power
plot(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],
     xlab="Soft Threshold (power)",ylab="Scale Free Topology Model Fit,signed R^2",type="n",
     main = paste("Scale independence"));
text(sft$fitIndices[,1], -sign(sft$fitIndices[,3])*sft$fitIndices[,2],
     labels=powers,cex=cex1,col="red");
# this line corresponds to using an R^2 cut-off of h
abline(h=0.90,col="red")
# Mean connectivity as a function of the soft-thresholding power
plot(sft$fitIndices[,1], sft$fitIndices[,5],
     xlab="Soft Threshold (power)",ylab="Mean Connectivity", type="n",
     main = paste("Mean connectivity"))
text(sft$fitIndices[,1], sft$fitIndices[,5], labels=powers, cex=cex1,col="red")




#3. һ�������繹����One-step network construction and module detection
net = blockwiseModules(data_matrix_mv, power = 6, maxBlockSize = 12000,
                       TOMType = "unsigned", minModuleSize = 30,
                       reassignThreshold = 0, mergeCutHeight = 0.45,
                       numericLabels = TRUE, pamRespectsDendro = FALSE,
                       saveTOMs = TRUE,
                       saveTOMFileBase = "AS-green-FPKM-TOM",
                       verbose = 3)
table(net$colors)


#4. �滭���չʾ
# open a graphics window
#sizeGrWindow(12, 9)
# Convert labels to colors for plotting
mergedColors = labels2colors(net$colors)
# Plot the dendrogram and the module colors underneath
plotDendroAndColors(net$dendrograms[[1]], mergedColors[net$blockGenes[[1]]],
                    "Module colors",
                    dendroLabels = FALSE, hang = 0.03,
                    addGuide = TRUE, guideHang = 0.05)




#5.�������
moduleLabels = net$colors
moduleColors = labels2colors(net$colors)
table(moduleColors)
MEs = net$MEs
geneTree = net$dendrograms[[1]]


#1. ���ӻ�ȫ����������
# Calculate topological overlap anew: this could be done more efficiently by saving the TOM
# calculated during module detection, but let us do it again here.
dissTOM = 1-TOMsimilarityFromExpr(data_matrix_mv, power = 12);
# Transform dissTOM with a power to make moderately strong connections more visible in the heatmap
plotTOM = dissTOM^7;
# Set diagonal to NA for a nicer plot
diag(plotTOM) = NA;
# Call the plot function
#sizeGrWindow(9,9)
TOMplot(plotTOM, geneTree, moduleColors, main = "Network heatmap plot, all genes")


TOM = TOMsimilarityFromExpr(data_matrix_mv, power = 6);
# Read in the annotation file
# annot = read.csv(file = "GeneAnnotation.csv");
# Select modules��Ҫ�޸ģ�ѡ����Ҫ������ģ����ɫ
modules = c("turquoise");
# Select module probesѡ��ģ��̽��
probes = colnames(data_matrix_mv)
inModule = is.finite(match(moduleColors, modules));
modProbes = probes[inModule];
#modGenes = annot$gene_symbol[match(modProbes, annot$substanceBXH)];
# Select the corresponding Topological Overlap
modTOM = TOM[inModule, inModule];
dimnames(modTOM) = list(modProbes, modProbes)
# Export the network into edge and node list files Cytoscape can read
cyt = exportNetworkToCytoscape(modTOM,
                               edgeFile = paste("0.77", paste(modules, collapse="-"), ".txt", sep=""),
                               nodeFile = paste("nodes-", paste(modules, collapse="-"), ".txt", sep=""),
                               weighted = TRUE,
                               threshold = 0.77,
                               nodeNames = modProbes,
                               #altNodeNames = modGenes,
                               nodeAttr = moduleColors[inModule]);


#######################################################################################################




                       #step7:����Ŀ��ӻ�
                        #��Ҫ�ο����ϣ�PDF document, R script

                         #����������л�����ͼ
 nGenes = ncol(data_matrix_mv)
 nSamples = nrow(data_matrix_mv)
 geneTree = net$dendrograms[[1]];
 dissTOM = 1-TOMsimilarityFromExpr(data_matrix_mv, power = 6);
 plotTOM = dissTOM^7;
 diag(plotTOM) = NA;
 #TOMplot(plotTOM, geneTree, moduleColors, main = 'Network heatmap plot, all genes')

                              #����ǳ����ļ�����Դ��ʱ�䣬���Խ���ѡȡ���в��ֻ�����ͼ���ɣ��Ҿ�û�л������Ҹ�������Ĵ���ѡȡ���ֻ�������ͼ��

                               #Ȼ�����ѡȡ���ֻ�����ͼ
nSelect = 4000

# For reproducibility, we set the random seed

set.seed(10);
select = sample(nGenes, size = nSelect);
selectTOM = dissTOM[select, select];

# There��s no simple way of restricting a clustering tree to a subset of genes, so we must re-cluster.

selectTree = hclust(as.dist(selectTOM), method = 'average')
selectColors = moduleColors[select];

# Open a graphical window

sizeGrWindow(9,9)

# Taking the dissimilarity to a power, say 10, makes the plot more informative by effectively changing
# the color palette; setting the diagonal to NA also improves the clarity of the plot

plotDiss = selectTOM^7;
diag(plotDiss) = NA;
TOMplot(plotDiss, selectTree, selectColors, main = 'Network heatmap plot, selected genes')






TOM = TOMsimilarityFromExpr(data_matrix_mv, power = 12);
# Read in the annotation file
# annot = read.csv(file = "GeneAnnotation.csv");
# Select modules��Ҫ�޸ģ�ѡ����Ҫ������ģ����ɫ
modules = c("turquoise");
# Select module probesѡ��ģ��̽��
probes = colnames(data_matrix_mv)
inModule = is.finite(match(moduleColors, modules));
modProbes = probes[inModule];
#modGenes = annot$gene_symbol[match(modProbes, annot$substanceBXH)];
# Select the corresponding Topological Overlap
modTOM = TOM[inModule, inModule];
dimnames(modTOM) = list(modProbes, modProbes)
# Export the network into edge and node list files Cytoscape can read
cyt = exportNetworkToCytoscape(modTOM,
                               edgeFile = paste("AS-green-FPKM-One-step-CytoscapeInput-edges-", paste(modules, collapse="-"), ".txt", sep=""),
                               nodeFile = paste("AS-green-FPKM-One-step-CytoscapeInput-nodes-", paste(modules, collapse="-"), ".txt", sep=""),
                               weighted = TRUE,
                               threshold = 0.9,
                               nodeNames = modProbes,
                               #altNodeNames = modGenes,
                               nodeAttr = moduleColors[inModule]);



Connectivity=softConnectivity(datExpr,power=12)-1
ConnectivityCut = 3600 # number of most connected genes that will be considered  # Incidentally, in the paper by Mischel et al (2005) we considered all 3600 #genes.  
ConnectivityRank = rank(-Connectivity)   
restConnectivity = ConnectivityRank <= ConnectivityCut  # thus our module detection uses the following number of genes
sum(restConnectivity)

ADJ= adjacency(datExpr[,restConnectivity],power=12)
dissTOM=TOMdist(ADJ)
hierTOM = hclust(as.dist(dissTOM),method="average");
par(mfrow=c(1,1))
plot(hierTOM,labels=F)
colorh1= cutreeStaticColor(hierTOM,cutHeight =0.94, minSize = 125)
par(mfrow=c(2,1),mar=c(2,4,1,1))
plot(hierTOM, main="Cluster Dendrogram", labels=F, xlab="", sub="");
plotColorUnderTree(hierTOM,colors=data.frame(module=colorh1))
title("Module (branch) color")
TOMplot(dissTOM,hierTOM,colorh1)





###########################################


module = 'blue'
probes = colnames(datExpr) ## �������������probe���ǻ�����
inModule = (moduleColors==module);
modProbes = probes[inModule];
modTOM = TOM[inModule, inModule];
dimnames(modTOM) = list(modProbes, modProbes)


cyt = exportNetworkToCytoscape(

      modTOM,

     edgeFile = paste('CytoscapeInput-edges-', paste(module, collapse='-'), '.txt', sep=''),

     nodeFile = paste('CytoscapeInput-nodes-', paste(module, collapse='-'), '.txt', sep=''),

     weighted = TRUE,

     threshold = 0.5,

     nodeNames = modProbes,

     nodeAttr = moduleColors[inModule])



####################################################################
show model tree

Connectivity=softConnectivity(datExpr,power=6)-1
ConnectivityCut = 3600 # number of most connected genes that will be considered
# Incidentally, in the paper by Mischel et al (2005) we considered all 3600 #genes.
ConnectivityRank = rank(-Connectivity)
restConnectivity = ConnectivityRank <= ConnectivityCut

sum(restConnectivity)
# Now we define the adjacency matrix for the 3600 most connected genes
ADJ= adjacency(datExpr[,restConnectivity],power=6)
gc()
# The following code computes the topological overlap matrix based on the
# adjacency matrix.
# TIME: This about a few minutes....
dissTOM=TOMdist(ADJ)
gc()

hierTOM = hclust(as.dist(dissTOM),method="average");
par(mfrow=c(1,1))
plot(hierTOM,labels=F)
colorh1= cutreeStaticColor(hierTOM,cutHeight = 0.94, minSize = 125)
# The above should be identical to colorh1=datSummary$color1[restConnectivity]
par(mfrow=c(2,1),mar=c(2,4,1,1))
plot(hierTOM, main="Cluster Dendrogram", labels=F, xlab="", sub="");
plotColorUnderTree(hierTOM,colors=data.frame(module=colorh1))
title("Module (branch) color")


par(mfrow=c(2,1),mar=c(2,4,1,1))
plot(hierTOM, main="Cluster Dendrogram", labels=F, xlab="", sub="");
plotColorUnderTree(hierTOM,colors=data.frame(module=colorh1))
title("Module (branch) color")
cmd1=cmdscale(as.dist(dissTOM),2)
par(mfrow=c(1,1))
plot(cmd1, col=as.character(colorh1), main="MDS plot",xlab="Scaling Dimension
1",ylab="Scaling Dimension 2")

############
############
############

 for (i in list[[1]]){
 T=datExpr[,which(dynamicColors == i)]
 write.table(T,file=paste(i,".modle",sep=''),quote=F,sep='\t')
 P= melt(T)
 p <- ggplot(P,aes(x=Var1,y=value,group=Var2))+geom_line()
 ggsave(p,file=paste(i,".png"))}

```



---
github: [https://github.com/Karobben](https://github.com/Karobben)
blog: [Karobben.github.io](http://Karobben.github.io)
R 语言画图索引: [https://karobben.github.io/R/R-index.html](https://karobben.github.io/R/R-index.html)
