# tar

#reference:[https://man.linuxde.net/tar](https://man.linuxde.net/tar)
<a name="U4VCl"></a>
# press


```bash
tar -cvf log.tar log2012.log    仅打包，不压缩！ 
tar -zcvf log.tar.gz log2012.log   打包后，以 gzip 压缩 
tar -jcvf log.tar.bz2 log2012.log  打包后，以 bzip2 压缩 
```


<a name="7DBLz"></a>
# unpress


```bash
tar -ztvf log.tar.gz
```


