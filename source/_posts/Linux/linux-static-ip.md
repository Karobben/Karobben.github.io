---
toc: true
url: linux_static_ip
covercopy: © Karobben
priority: 10000
date: 2023-01-31 10:40:12
title: "How to set a static IP address for Linux"
ytitle: "How to set a static IP address for Linux"
description: "How to set a static IP address for Linux"
excerpt: "A PC's IP address should be kept from changing to avoid connectivity issues and prevent access problems with devices and services that are configured to communicate with it. This can be especially critical when specific IP addresses are required for security and access control systems. <a title='ChatGPT'>Who sad this?</a>"
tags: [Linux]
category: [Linux, System]
cover: "https://s1.ax1x.com/2023/02/01/pS0LD5n.png"
thumbnail: "https://s1.ax1x.com/2023/02/01/pS0L62V.png"
---



## How to set a static ip for Pop os


1. Find `Gateway` and the `DNS` for your network

![](https://s1.ax1x.com/2023/02/01/pS0LD5n.png)
Setting → Network → Check the details of your network.
Here, `Default Route` is the `Gateway`,
`DNS` is the `DNS`

2. Find the Netmask for your network by `ifconfig`

```bash
ifconfig
```

<pre>
eno1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.3.1  netmask 255.255.255.0  broadcast 192.168.3.255
.
.
.
</pre>

3. fill them in IPv4 setting

Fill the address you want and rest of other infor you jut get from above.
||![](https://s1.ax1x.com/2023/02/01/pS0L62V.png)
























































































































































<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
