TB

Result = data.frame()
for i in c(unique(TB$Lon)){
  for ii in c(unique(TB$Lat))
  tmp = TB
  tmp = TB[i:i+2*X,ii:ii+2*Y]
  Num = length(which(is.na(tmp)==T))
  R = sum(tmp)/(9-Num)
  tmp_R = data.frame(Lon=i+X, Lat = ii+Y,Avr=R)
  tmp_R = rbind(Result,tmp_R)
}
