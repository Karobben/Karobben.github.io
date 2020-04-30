---
url: kn1oxx
---

# Sort a uniq List

'''<br />
Base <- data.frame(Nodes =c("P1", "P1", "P1", "P2"), Targets=c("P2","P3","P4","P1"))<br />
List <- c("P1", "P2", "P3")<br />
Base <- read.table("DataBase/Mybase/AB_List")<br />
List <- read.table("")[[1]]<br />
'''

'''<br />
Result without Annotation<br />
'''<br />
library(tidyr)<br />
library(dplyr)

A <- Base<br />
A <- A[which(match(A[[1]],List)!="NA"),]<br />
A <- A[which(match(A[[2]],List)!="NA"),]<br />
A![](https://g.yuque.com/gr/latex?VAB%20%3D%20paste(A%5B%5B1%5D%5D%2C%22_%22%2CA%5B%5B2%5D%5D%2Csep%3D'')%0AA#card=math&code=VAB%20%3D%20paste%28A%5B%5B1%5D%5D%2C%22_%22%2CA%5B%5B2%5D%5D%2Csep%3D%27%27%29%0AA)VBA = paste(A[[2]],"_",A[[1]],sep='')

List = c(A![](https://g.yuque.com/gr/latex?VAB%2C%20A#card=math&code=VAB%2C%20A)VBA)<br />
List = data.frame(X=List[duplicated(List)])<br />
List = List %>% separate(X, c("A", "B"),'_')<br />
List![](https://g.yuque.com/gr/latex?VAB%20%3D%20paste(List%5B%5B1%5D%5D%2C%22_%22%2CList%5B%5B2%5D%5D%2Csep%3D'')%0AList#card=math&code=VAB%20%3D%20paste%28List%5B%5B1%5D%5D%2C%22_%22%2CList%5B%5B2%5D%5D%2Csep%3D%27%27%29%0AList)VBA = paste(List[[2]],"_",List[[1]],sep='')

<a name="95de5268"></a>
# remove Lift == right

List = List[-which(match(List![](https://g.yuque.com/gr/latex?VAB%2CList#card=math&code=VAB%2CList)VBA)-c(1: nrow(List))==0),]<br />
List = List[match(List![](https://g.yuque.com/gr/latex?VAB%2CList#card=math&code=VAB%2CList)VBA)-c(1: nrow(List))>0,]<br />
A = A[-na.omit(match(List![](https://g.yuque.com/gr/latex?VAB%2CA#card=math&code=VAB%2CA)VAB)),]

write.table(data.frame(A[1:2]),"Output",sep='\t',quote=F,col.names=F,row.names=F)

'''<br />
for delete duplicates and combind rest of colums<br />
'''

RM_du <-function(A){<br />
A![](https://g.yuque.com/gr/latex?VAB%20%3D%20paste(A%5B%5B1%5D%5D%2C%22_%22%2CA%5B%5B2%5D%5D%2Csep%3D'')%0A%20%20%20%20%20%20%20%20A#card=math&code=VAB%20%3D%20paste%28A%5B%5B1%5D%5D%2C%22_%22%2CA%5B%5B2%5D%5D%2Csep%3D%27%27%29%0A%20%20%20%20%20%20%20%20A)VBA = paste(A[[2]],"_",A[[1]],sep='')<br />
#<br />
Num=0<br />
Num= Num+1<br />
# Get the Duplicate list<br />
i = unique(A![](https://g.yuque.com/gr/latex?VAB)%5B1%5D%0A%20%20%20%20%20%20%20%20List1%20%3D%20which(A#card=math&code=VAB%29%5B1%5D%0A%20%20%20%20%20%20%20%20List1%20%3D%20which%28A)VAB == A![](https://g.yuque.com/gr/latex?VAB%5B1%5D)%0A%20%20%20%20%20%20%20%20List1%20%3D%20c(List1%2Cwhich(A#card=math&code=VAB%5B1%5D%29%0A%20%20%20%20%20%20%20%20List1%20%3D%20c%28List1%2Cwhich%28A)VBA == A![](https://g.yuque.com/gr/latex?VAB%5B1%5D))%0A%20%20%20%20%20%20%20%20TMP%20%3D%20A%5BList1%2C%5D%0A%20%20%20%20%20%20%20%20TMP_R%20%3D%20data.frame(TMP%5B1%2C1%3A2%5D%2CV3%20%3D%20paste(unique(as.character(TMP%5B%2C3%5D))%2C%20collapse%3D'%7C'))%0A%20%20%20%20%20%20%20%20Result%20%3D%20TMP_R%0A%20%20%20%20%20%20%20%20A%20%3D%20A%5B-List1%2C%5D%0A%20%20%20%20%20%20%20%20print(Num)%0A%20%20%20%20%20%20%20%20%23%0A%20%20%20%20%20%20%20%20for(%20i%20in%20unique(A#card=math&code=VAB%5B1%5D%29%29%0A%20%20%20%20%20%20%20%20TMP%20%3D%20A%5BList1%2C%5D%0A%20%20%20%20%20%20%20%20TMP_R%20%3D%20data.frame%28TMP%5B1%2C1%3A2%5D%2CV3%20%3D%20paste%28unique%28as.character%28TMP%5B%2C3%5D%29%29%2C%20collapse%3D%27%7C%27%29%29%0A%20%20%20%20%20%20%20%20Result%20%3D%20TMP_R%0A%20%20%20%20%20%20%20%20A%20%3D%20A%5B-List1%2C%5D%0A%20%20%20%20%20%20%20%20print%28Num%29%0A%20%20%20%20%20%20%20%20%23%0A%20%20%20%20%20%20%20%20for%28%20i%20in%20unique%28A)VAB)[-1]){<br />
Num= Num+1<br />
# Get the Duplicate list<br />
List1 = which(A![](https://g.yuque.com/gr/latex?VAB%20%3D%3D%20A#card=math&code=VAB%20%3D%3D%20A)VAB[1])<br />
List1 = c(List1,which(A![](https://g.yuque.com/gr/latex?VBA%20%3D%3D%20A#card=math&code=VBA%20%3D%3D%20A)VAB[1]))<br />
TMP = A[List1,]<br />
TMP_R = data.frame(TMP[1,1:2],V3 = paste(unique(as.character(TMP[,3])), collapse='|'))<br />
Result = rbind(Result,TMP_R)<br />
A = A[-List1,]<br />
print(Num)<br />
}<br />
return(Result)<br />
}
