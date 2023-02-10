---
title: "github"
description: "github"
url: github2
date: 2020/06/23
toc: true
excerpt: "Basic commands for synchrony the local and cloud github repository."
tags: [Linux, GitHub, bash]
category: [Linux, GitHub]
cover: 'https://cn.bing.com/th?id=AMMS_c45f125b765170342ef8efd07cb7a55f&w=410&h=110'
thumbnail: 'https://cn.bing.com/th?id=AMMS_c45f125b765170342ef8efd07cb7a55f&w=110&h=110'
priority: 10000
---

## github


Github 本地上更新库
```bash
## Initialize your directory
git init

## 关联
git remote add IO https://github.com/Karobben/Karobben.github.io

##添加
git add .

##注释
git commit -m "注释"

git pull --rebase IO master
git push -u IO master
```


## Avoid password everytime

[Click me](https://luanlengli.github.io/2019/04/07/git-pull%E5%85%8D%E5%AF%86%E7%A0%81%E9%85%8D%E7%BD%AE.html)


## when uploading file is to big

```bash
git config http.postBuffer 524288000
```


## Delete large files

[© Daniel Andrei Mincă; 2015](https://stackoverflow.com/questions/33360043/git-error-need-to-remove-large-file)
```bash
$ git rm --cached giant_file
# Stage our giant file for removal, but leave it on disk

git commit --amend -CHEAD
# Amend the previous commit with your change
# Simply making a new commit won't work, as you need
# to remove the file from the unpushed history as well

git push
# Push our rewritten, smaller commit
``` 

## Git push with ssh

Documentation: [Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)

Follow the instructions from Github to generate a ssh public key first.
Be sure about add the email for config the user

Exp:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519
```

After that, copy the key into github.

You may still find that Username is needed for push.
According [2240](https://stackoverflow.com/questions/6565357/git-push-requires-username-and-password), we need to change the type or remote link.

Enter your github repository page and select the ssh link to configure the local repository as follow and the problem shell be solved.

![](https://s1.ax1x.com/2023/02/11/pSh4zNT.png)

```bash
git remote set-url origin git@github.com:username/repo.git
```
