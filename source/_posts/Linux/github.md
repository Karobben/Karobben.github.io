---
title: "github"
description: "github"
url: github2
date: 2020/06/23
toc: true
excerpt: "Basic commands for synchrony the local and cloud github repository."
tags: [Linux, GitHub, bash]
category: [Linux, GitHub]
cover: 'https://kinsta.com/wp-content/uploads/2018/04/what-is-github-1-1-1024x512.png'
thumbnail: 'https://cn.bing.com/th?id=AMMS_c45f125b765170342ef8efd07cb7a55f&w=110&h=110'
priority: 10000
covercopy: <a href="https://kinsta.com/knowledgebase/what-is-github">© kinsta</a>
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



## Errors

### fatal: in unpopulated submodule '.deploy_git'

<pre>
fatal: in unpopulated submodule '.deploy_git'
FATAL { err:
   { Error: Spawn failed
       at ChildProcess.task.on.code (/mnt/8A26661926660713/Github/Notes_BK/node_modules/hexo-util/lib/spawn.js:51:21)
       at ChildProcess.emit (events.js:198:13)
       at Process.ChildProcess._handle.onexit (internal/child_process.js:248:12) code: 128 } } 'Something\'s wrong. Maybe you can find the solution here: %s' '\u001b[4mhttps://hexo.io/docs/troubleshooting.html\u001b[24m'
</pre>


> According to ChatGPT (this is a super genius! I can't find this result anywhere!) The error message you provided is related to Hexo, a static site generator. It seems that there was an issue with a submodule named '.deploy_git' in the Git repository you were working with.
>
> This error occurs when there's a problem with the Git submodule in your Hexo project, and it's not able to be cloned. To resolve this issue, try the following steps:

```bash
# Remove the problematic submodule:
git rm --cached .deploy_git
# Commit the changes:
git commit -m "Removed problematic submodule"
# Re-add the submodule:
# Replace <repo> with the URL of the Git repository for the submodule.
git submodule add -b master <repo> .deploy_git
# Initialize the submodule:
git submodule init
# Update the submodule:
git submodule update
```

> These steps should resolve the issue with the Git submodule and allow you to continue using Hexo to generate your static site. If the issue persists, you may need to refer to the Hexo troubleshooting guide (https://hexo.io/docs/troubleshooting.html) for further assistance.





<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
