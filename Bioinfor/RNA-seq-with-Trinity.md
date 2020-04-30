---
url: zt3n7t
---

# RNA-seq with Trinity


![](https://cdn.nlark.com/yuque/__graphviz/40abd2218c20c967c120ec0afc996133.svg#lake_card_v2=eyJjb2RlIjoiZGlncmFwaCBGIHtcbiAgICByYW5rZGlyID0gTFI7XG4gICAgZWRnZSBbc3R5bGU9c29saWRdO1xuICAgIG5vZGUgW3N0eWxlPWZpbGxlZCwgZm9udD1Db3VyaWVyXTtcblx0XHRcblxuICAgIHN1YmdyYXBoIEEge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgU3RhcnQgW2xhYmVsID0gXCJEb3dubG9hZGluZyBTZXF1ZW5jZXNcIiwgY29sb3I9Z3JleSwgc2hhcGUgPSBib3gsIGZpbGxjb2xvciA9IGNvcmFsIF07XG4gICAgICAgIEVuZCAgIFtsYWJlbCA9IFwiZGUtbm92byB0cmFuc2NyaXB0b21lKGZhc3RhKVwiLCBjb2xvcj1ncmV5LCBzaGFwZSA9IGJveCwgZmlsbGNvbG9yID0gY29yYWxdO1xuXG4gICAgICAgIENvbjEgW2xhYmVsID0gXCJTU1Itc3BsaXRcIiwgY29sb3I9Z3JleSwgc2hhcGUgPSBib3gsIGZpbGxjb2xvciA9IGNvcmFsLCBzaXplID0gM107XG4gICAgICAgIENvbjIgW2xhYmVsID0gXCJRdWFsaXRpIGNvbnRyb2wgJlxcbkxvdy1RdWFsaXR5IGZpbHRlclwiLCBcblx0XHRcdFx0XHRcdFx0Y29sb3I9Z3JleSwgc2hhcGUgPSBkaWFtb25kLCBmaWxsY29sb3IgPSBjb3JhbCwgc2l6ZSA9IDNdO1xuXHRcdFx0XHRDb24zIFtsYWJlbCA9IFwiZGUtbm92b1wiLCBjb2xvcj1ncmV5LCBzaGFwZSA9IGJveCwgZmlsbGNvbG9yID0gY29yYWwgXVxuICAgIH1cblxuICAgIHN1YmdyYXBoIEIge1xuICAgICAgICByYW5rID0gc2FtZTtcblx0XHRcdFx0SEggW2xhYmVsPVwiQWRhcHRlciByZW1vdmVcIiwgY29sb3I9Z3JleSwgc2hhcGUgPSBkaWFtb25kLCBmaWxsY29sb3IgPSB3aGl0ZSwgc2l6ZSA9IDNdXG5cdFx0fVxuXHRcdFxuICAgIHN1YmdyYXBoIEMge1xuICAgICAgICByYW5rID0gc2FtZTtcbiAgICAgICAgUzEgW2xhYmVsID0gXCJwcmVmZXRjaFwiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuICAgICAgICBTMiBbbGFiZWwgPSBcImZhc3RxLWR1bXBcIiwgc2hhcGUgPSBib3gsIGNvbG9yID0gZGVlcHNreWJsdWUxXTtcbiAgICAgICAgUzMgW2xhYmVsID0gXCJmYXN0cFwiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuICAgICAgICBTNCBbbGFiZWwgPSBcInRyaW1tb21hdGljXCIsIHNoYXBlID0gYm94LCBjb2xvciA9IGRlZXBza3libHVlMV07XG4gICAgICAgIFM1IFtsYWJlbCA9IFwiVHJpbml0eVwiLCBzaGFwZSA9IGJveCwgY29sb3IgPSBkZWVwc2t5Ymx1ZTFdO1xuICAgIH1cblx0XHRTdGFydFx0LT5cdENvbjE7XG5cdFx0Q29uMVx0LT5cdENvbjI7XG5cdFx0Q29uMlx0LT5cdENvbjMgW2xhYmVsPVwiTm8gYWRwdG9yXCJdO1xuXHRcdENvbjNcdC0-XHRFbmQ7XG5cblx0XHRDb24yXHQtPlx0SEggW2xhYmVsID0gXCJIYXMgYWRwdG9yXCJdO1xuXHRcdEhIXHRcdC0-XHRDb24zO1xuXHRcdFxuXHRcdGVkZ2Vbc3R5bGU9ZGFzaGVkO2Fycm93dGFpbD1kb3RdXG4gICAgUzEgLT5cdFN0YXJ0XHRbc3R5bGU9XCJkYXNoZWRcIiBzaGFwZT1ib3hdO1xuXHRcdFMyXHQtPlx0Q29uMTtcblx0XHRTM1x0LT5cdENvbjI7XG5cdFx0UzRcdC0-XHRISDtcblx0XHRTNVx0LT5cdENvbjM7XG59XG4iLCJ0eXBlIjoiZ3JhcGh2aXoiLCJpZCI6Im1vM3h2IiwidXJsIjoiaHR0cHM6Ly9jZG4ubmxhcmsuY29tL3l1cXVlL19fZ3JhcGh2aXovNDBhYmQyMjE4YzIwYzk2N2MxMjBlYzBhZmM5OTYxMzMuc3ZnIiwiaGVpZ2h0Ijo0NzMsImNhcmQiOiJkaWFncmFtIn0=)

```bash
#### Downloading the RNA-seq
prefetch  --ascp-path "/usr/bin/ascp|/home/ken/.aspera/connect/etc/asperaweb_id_dsa.putty" ERR025599

#### Split SSR to fastq
fastq-dump --defline-seq '@$sn[_$rn]/$ri' --split-files SRR77600*

#### cut the low quality reads
#basic command
#fastp -u 15 -w 8 -i SRR7760055_1.fastq -o cut_SRR7760055_1.fastq
for i in $(ls *.fastq);do  fastp -u 15 -w 8 -i $i -o cut_$i; mv fastp.html $i.html;done

#### Trimmomatic cut the lower grade head or tail jodged by the quality report
java -jar  trimmomatic-0.38.jar SE -threads 8 -phred33 SRR771602.fastq 2.fq ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 HEADCROP:10 CROP:87
for i in $(ls cut_SRR77600*);do
  java -jar  trimmomatic-0.38.jar SE -threads 8 -phred33 $i 2_$i ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 HEADCROP:10 CROP:87
done


#Trnity
Trinity --seqType fq --max_memory 55G --single ../cut_SRR7760072_1.fastq --CPU 8 --full_cleanup
Trinity --seqType fq --max_memory 55G --single 2_cut_SRR7760055_1.fastq --CPU 8 --full_cleanup

for i in $(ls 2_cut_SRR77600*); do
Trinity --seqType fq --max_memory 40G --single $i --CPU 8 --full_cleanup
mv trinity_out_dir.Trinity.fasta $i.fa
done
```

