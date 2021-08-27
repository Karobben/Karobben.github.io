---
title: "Hexo: batch | Maintain you md files with batchs/scripts"
toc: true
date: 2021-03-09 10:32:34
description: "Use different kinds of batches to maintain your blog"
url: hexo_batch
excerpt: 'Use different kinds of batches to maintain your blog:<br>
<input type="checkbox" id="cbx_0" checked="true">
Change the tags/categories with batch;<br>
<input type="checkbox" id="cbx_0" checked="true">
Sort the citation of a markdown file'
tags: [Hexo, MarkDown]
category: [others, Blog, Hexo]
cover: "https://lunarscents.github.io/images/hexo.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
priority: 10000
covercopy: © lunarscents
---
## Substitute

Sometimes, we want to change the category, let's say, from [Notes, Biology, Paper] to [Notes, Paper, Biology]. It is not a good idea to rewrite them one by one. In fact, `sed` can help.

```bash BASH
strA="\[Notes,\ Biology,\ Paper\]"
strB="\[Notes,\ Paper,\ Biology\]"
## Ender your hexo blog directory
cd ${Hexo}
## searching for all posts
find source -name "*.md"
## Check the match pattern
grep  "$strA" $(find source -name "*.md")
## Select one of the file from above to test the substitute pattern
sed "s/$strA/$strB/" mtGenome.md| head
## once the substitution was successful, we can run it on all posts.
sed -i "s/$strA/$strB/" $(find source -name "*.md")
```

### Check the match pattern
With the `sed` grammar above, we shall substitute all `strA` with `strB`. But sometimes, we may go too far. To avoid replacing something unintentionally, we'd like to make sure each matching pattern is unique. We can achieve this with bash commands.

```bash
## Count the match pattern to make sure it is uniq:
grep  "$strA" $(find source -name "*.md")| awk -F":" '{print $1}'| uniq -c
```
In this case, we use `grep` to search all matching patterns in all files. By piping it to `awk`, the name of the files has remained. Finally, we calculate the files and find `Hexo_post.md` has two matches.
<pre>
1 source/_posts/Blog/hexo_lived2d_busuanzi.md
1 source/_posts/Blog/Hexo_math.md
2 source/_posts/Blog/Hexo_post.md
1 source/_posts/Blog/Hexo_search.md
</pre>

We can also achieve this with `uniq -d` and only `Hexo_post.md` will be printed out.
In this situation, we need to change our matching string to avoid mismatches.

### Final Check
Before you run `sed -i`, you can still make a final check:
```bash
sed  "s/$strA/$strB/" $(find source -name "*.md")| grep "$strB"|wc
```
by comparing the counts of result by `grep`.


## substitute Html site

Replace Sit1 with Sit2
```bash
SIT1="https://www.electronjs.org/app-img/hexo-client/hexo-client-icon-128.png"
SIT2="https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"

strA=$(echo $SIT1|sed 's=/=\\/=g')
strB=$(echo $SIT2|sed 's=/=\\/=g')
## Ender your hexo blog directory
cd ${Hexo}
## As before, you show try it before rewrite
sed -i "s/$strA/$strB/" $(find source -name "*.md")
```

## Citation

```bash
File=23.md
cp $File $File.md
Cites=$(grep "^\[" $File|sort|uniq)
sed -i '/^\[/d' $File.md
echo -e "---\n$Cites" >> $File.md
```
### Before

```md $File
- BSFL meal increased the abundance of beneficial microorganisms that contribute to the health of the host such as lactic acid[^Huyben_2019][^Terova_2019][^Rimoldi_2019]and butyrate[^Terova_2019].

[^Rimoldi_2019]: Rimoldi S, Gini E, Iannini F, Gasco L, Terova G. The effects of dietary insect meal from Hermetia illucens prepupae on autochthonous gut microbiota of rainbow trout (Oncorhynchus mykiss). Animals (2019) 9(4):143. doi: 10.3390/ani9040143
[^Liu_H_2018]: Liu H, Wang J, He T, Becker S, Zhang G, Li D, et al. Butyrate: a double-edged sword for health? Adv Nutr (2018) 9(1):21–9. doi: 10.1093/advances/nmx009

- The anti-inflammatory properties of microbe-derived butyrate in gut and its role in enhancing intestinal barrierfunction and mucosal immunity are well studied in human[^Liu_H_2018].

[^Huyben_2019]: Huyben D, Vidaković A, Hallgren SW, Langeland M. High-throughput sequencing of gut microbiota in rainbow trout (Oncorhynchus mykiss) fed larval and pre-pupae stages of black soldier fly (Hermetia illucens). Aquaculture (2019) 500:485–91. doi: 10.1016/j.aquaculture.2018.10.034

- It is also possible that the short-chain fatty acids including butyrate produced by gut microbiota might induce the expression of host defense peptides and prevent inflammation in the gut as observed in mammals and birds[^Wu_J_2020].

[^Terova_2019]: Terova G, Rimoldi S, Ascione C, Gini E, Ceccotti C, Gasco L. Rainbow trout (Oncorhynchus mykiss) gut microbiota is modulated by insect meal from Hermetia illucens prepupae in the diet. Rev Fish Biol Fish (2019) 29:465–86. doi: 10.1007/s11160-019-09558-y
```

### After
I removed blank lines by hand to make it neatly.
```md $File.md
- BSFL meal increased the abundance of beneficial microorganisms that contribute to the health of the host such as lactic acid[^Huyben_2019][^Terova_2019][^Rimoldi_2019]and butyrate[^Terova_2019].
- The anti-inflammatory properties of microbe-derived butyrate in gut and its role in enhancing intestinal barrierfunction and mucosal immunity are well studied in human[^Liu_H_2018].
- It is also possible that the short-chain fatty acids including butyrate produced by gut microbiota might induce the expression of host defense peptides and prevent inflammation in the gut as observed in mammals and birds[^Wu_J_2020].

---
[^Huyben_2019]: Huyben D, Vidaković A, Hallgren SW, Langeland M. High-throughput sequencing of gut microbiota in rainbow trout (Oncorhynchus mykiss) fed larval and pre-pupae stages of black soldier fly (Hermetia illucens). Aquaculture (2019) 500:485–91. doi: 10.1016/j.aquaculture.2018.10.034
[^Liu_H_2018]: Liu H, Wang J, He T, Becker S, Zhang G, Li D, et al. Butyrate: a double-edged sword for health? Adv Nutr (2018) 9(1):21–9. doi: 10.1093/advances/nmx009
[^Rimoldi_2019]: Rimoldi S, Gini E, Iannini F, Gasco L, Terova G. The effects of dietary insect meal from Hermetia illucens prepupae on autochthonous gut microbiota of rainbow trout (Oncorhynchus mykiss). Animals (2019) 9(4):143. doi: 10.3390/ani9040143
[^Terova_2019]: Terova G, Rimoldi S, Ascione C, Gini E, Ceccotti C, Gasco L. Rainbow trout (Oncorhynchus mykiss) gut microbiota is modulated by insect meal from Hermetia illucens prepupae in the diet. Rev Fish Biol Fish (2019) 29:465–86. doi: 10.1007/s11160-019-09558-y
```
