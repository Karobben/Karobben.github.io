---
toc: true
url: hexo_sitemap
priority: 10000
date: 2021-03-22 12:09:59
title: "Hexo: Sitemap| Generate and Submit your Hexo-Sitemaps to Google and Bing"
description: "The Sitemaps protocol allows a webmaster to inform search engines about URLs on a website that are available for crawling. A Sitemap is an XML file that lists the URLs for a site. It allows webmasters to include additional information about each URL: when it was last updated, how often it changes, and how important it is in relation to other URLs of the site. This allows search engines to crawl the site more efficiently and to find URLs that may be isolated from the rest of the site's content. The Sitemaps protocol is a URL inclusion protocol and complements robots.txt, a URL exclusion protocol."
excerpt: "The Sitemaps protocol allows a webmaster to inform search engines about URLs on a website that are available for crawling. A Sitemap is an XML file that lists the URLs for a site. It allows webmasters to include additional information about each URL: when it was last updated, how often it changes, and how important it is in relation to other URLs of the site. This allows search engines to crawl the site more efficiently and to find URLs that may be isolated from the rest of the site's content. The Sitemaps protocol is a URL inclusion protocol and complements robots.txt, a URL exclusion protocol."
tags: [Hexo, Hexo Plugin, MarkDown]
category: [others, Blog, Hexo]
cover: "http://static3.creately.com/images/responsive-landing/sitemap/template-3-large.jpg"
thumbnail: "https://blog.kritner.com/2019/03/19/Hexo-local-configuration/hexo-logo-avatar.png"
covercopy: © creately.com

---

## "Hexo: Sitemap"
The Sitemaps protocol allows a webmaster to inform search engines about URLs on a website that are available for crawling. A Sitemap is an XML file that lists the URLs for a site. It allows webmasters to include additional information about each URL: when it was last updated, how often it changes, and how important it is in relation to other URLs of the site. This allows search engines to crawl the site more efficiently and to find URLs that may be isolated from the rest of the site's content. The Sitemaps protocol is a URL inclusion protocol and complements robots.txt, a URL exclusion protocol.[^wiki_sitemape]
[^wiki_sitemape]: [wikipedia: Sitemaps](http://en.wikipedia.org/wiki/Sitemaps)
### install plugins[^沧沧凉凉_2020]

[^沧沧凉凉_2020]: [沧沧凉凉, 2020: Hexo进阶-生成站点地图（Sitemap）](https://zhuanlan.zhihu.com/p/150999914)
```bash
# for google
npm install hexo-generator-sitemap --save
# for baidu
npm install hexo-generator-baidu-sitemap --save
```

### Config
```bash
# URL
## If your site is put in a subdirectory,
set url as 'http://yoursite.com/child' and root as '/child/'
url: ${your domain}
root: /
permalink: :year/:month/:day/:title/
permalink_defaults:
pretty_urls:
  trailing_index: true # Set to false to remove trailing 'index.html' from permalinks
  trailing_html: true # Set to false to remove trailing '.html' from permalinks
```

## Submit to BBG[^FLUNGGG_2019]

[^FLUNGGG_2019]: [FLUNGGG, 2019: hexo搭建博客系列(六)百度，必应，谷歌收录](https://blog.csdn.net/weixin_41800884/article/details/103750683#5__183)

I am currently using GitPage. So, submitting it to Baidu is kind of useless...

Before Submitting it to Google/Bing, we need to verify the ownership of the domain. The easiest way to verify this is by adding it to your Google Analytics. Once you're down with google, you can synchronize it to Bing with Google.
