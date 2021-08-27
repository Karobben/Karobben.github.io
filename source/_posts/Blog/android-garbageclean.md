---
toc: true
url: android_garbageclean
covercopy: <a href="https://descargarparapc.club/termux/">© Descargar Termux para PC</a>
priority: 10000
date: 2021-06-10 16:14:20
title: "Android garbage clean by termux"
ytitle: "轻松删除安卓垃圾文件"
description: "Deleted android garbage files without hurting your data (with termux)"
excerpt: "Deleted android garbage files without hurting your data (with termux)"
tags: [Termux, Android]
category: [others, Android]
cover: 'https://descargarparapc.club/wp-content/uploads/2020/06/termux.jpg'
thumbnail: 'https://descargarparapc.club/wp-content/uploads/2020/06/termux.jpg'
---

## An example of Time:
In termux, the files for time is stord at `storage/shared/Android/data/com.tencent.tim/`

```bash
du -sh storage/shared/Android/data/com.tencent.tim/*
```
<pre>
1.7G	storage/shared/Android/data/com.tencent.tim/Tencent
73K	storage/shared/Android/data/com.tencent.tim/cache
70M	storage/shared/Android/data/com.tencent.tim/files
92K	storage/shared/Android/data/com.tencent.tim/photo
94K	storage/shared/Android/data/com.tencent.tim/qq
86M	storage/shared/Android/data/com.tencent.tim/qzone
</pre>


By checking the directory `Tim`, we can see that most garbage is chatting pictures.

```bash
du -sh storage/shared/Android/data/com.tencent.tim/Tencent/Tim/*
```
<pre>
733K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/591465908
9.0M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/DoutuRes
7.0K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/NoRename#H6s8amH6x
861M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/chatpic
424K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/diskcache
308K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/doodle_template
523K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/dov_doodle_template
276K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/dov_ptv_template_dov
2.0M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/emoji
7.5K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/funcall
3.5K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/head
4.6M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/newpoke
5.6M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/pddata
24M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/photo
3.8M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/portrait
140K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/ppt
114K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/qav
9.2M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/qbosssplahAD
327K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/rbt
142M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/shortvideo
470K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/system_background
2.8M	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/tencent
4.0K	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/thumb
~ $ du -sh storage/shared/Android/data/com.tencent.tim/Tencent/Tim/
1.1G	storage/shared/Android/data/com.tencent.tim/Tencent/Tim/
~ $ ls storage/shared/Android/data/com.tencent.tim/Tencent/Tim/chatpic
</pre>
## Garbage file lists

```bash
# 我也不知道有什么用，反正我删了
Noidea=$(echo "storage/shared/tencent
storage/shared/MideaHome/
storage/shared/Huawei/Themes/themecache/
")
for i in $Noidea:
do rm -rf $i
done
########
# Tim
########

# 可删

## 没啥影响， 就是聊天记录和图片都需要重新加载。 往上滑就能重新加载回来。 但是删掉可以空出好几个G
Tim=$(echo "storage/shared/Android/data/com.tencent.tim/Tencent/Tim
storage/shared/Android/data/com.tencent.tim/Tencent/MobileQQ
storage/shared/Android/data/com.tencent.tim/Tencent/Tim_Images
storage/shared/Android/data/com.tencent.tim/Tencent/QQ_business
storage/shared/Android/data/com.tencent.tim/Tencent/mini
storage/shared/Android/data/com.tencent.tim/Tencent/qzonebackup
storage/shared/Android/data/com.tencent.tim/Tencent/Qzone
storage/shared/Android/data/com.tencent.tim/Tencent/Qzone
storage/shared/Android/data/com.tencent.tim/qzone
")

## Tim_Images: 自己编辑过的图

## 不知道是啥， 我先删为敬了: QQ_business, mini, qzonebackup, Qzone

# 可选
# rm -r storage/shared/Android/data/com.tencent.tim/Tencent/TIMfile_recv
# rm -r storage/shared/Android/data/com.tencent.tim/Tencent/QQ_Favorite

for i in $Tim;
do rm -rf $i;
done
## 自己收藏的图片
# rm -r storage/shared/Android/data/com.tencent.tim/Tencent/TIM_Favorite
# rm -r storage/shared/Android/data/com.tencent.tim/Tencent/QQ_Collection
# rm -r storage/shared/Android/data/com.tencent.tim/Tencent/QQ_Favorite

# 先不删
# 不知道是啥， 所以先不删， 反正占地不大
# rm -r storage/shared/Android/data/com.tencent.tim/Tencent/TMAssistantSDK


######
# QQ
######
# QQ 我还没看。 估计和tim是一个样子的 过段时间再来更新
Phone_QQ=$(echo "storage/shared/Android/data/com.tencent.mobileqq/qzone
storage/shared/Android/data/com.tencent.mobileqq/Tencent/MobileQQ
")
for i in $Phone_QQ;
  do rm -r $i
done

#######
# 微信
#######

mm=$(echo "storage/shared/Android/data/com.tencent.mm/MicroMsg/6eae3a15b247f7e822ed8dbc12c884e5
storage/shared/Android/data/com.tencent.mm/MicroMsg/CheckResUpdate
storage/shared/Android/data/com.tencent.mm/MicroMsg/SQLTrace
storage/shared/Android/data/com.tencent.mm/MicroMsg/ThumbVideoCache
storage/shared/Android/data/com.tencent.mm/MicroMsg/WebNetFile
storage/shared/Android/data/com.tencent.mm/MicroMsg/b2b233ad21176b0661427b78a381faf3
storage/shared/Android/data/com.tencent.mm/MicroMsg/card
storage/shared/Android/data/com.tencent.mm/MicroMsg/crash
storage/shared/Android/data/com.tencent.mm/MicroMsg/facedir
storage/shared/Android/data/com.tencent.mm/MicroMsg/hilive
storage/shared/Android/data/com.tencent.mm/MicroMsg/mapsdk
storage/shared/Android/data/com.tencent.mm/MicroMsg/recovery
storage/shared/Android/data/com.tencent.mm/MicroMsg/switchAccountBg
storage/shared/Android/data/com.tencent.mm/MicroMsg/vusericon
storage/shared/Android/data/com.tencent.mm/MicroMsg/wagamefiles
storage/shared/Android/data/com.tencent.mm/MicroMsg/wallet
storage/shared/Android/data/com.tencent.mm/MicroMsg/wallet_images
storage/shared/Android/data/com.tencent.mm/MicroMsg/wxafiles
storage/shared/Android/data/com.tencent.mm/MicroMsg/wxanewfiles
storage/shared/Android/data/com.tencent.mm/MicroMsg/xlog
storage/shared/Android/data/com.tencent.mm/cache/
"
)


for i in $mm;
  do rm -r $i;
done

# 已知删除项：
# 语音
# 保留项
# 图片， 聊天记录， 转帐记录

# 可选
mm_config=$(echo "storage/shared/Android/data/com.tencent.mm/MicroMsg/Download #下载的文件
"
)

########
# 淘宝
########

rm -rf storage/shared/Android/data/com.taobao.taobao/cache/

########
# 华为垃圾
########

storage/shared/Android/data/com.huawei.meetime/files/

########
# 优酷
########

rm -rf storage/shared/Android/data/com.youku.phone/files/###################
# 一些垃圾图片的位置
##################
rm -rf storage/shared/com*

#???
rm -rf storage/shared/Android/obb
```
