---
title: "tmux2"
description: "tmux2"
url: tmux2
date: 2020/06/26
toc: true
excerpt: "Termux Termux is an Android terminal emulator and Linux environment app that works directly with no rooting or setup required. A minimal base system is installed automatically - additional packages are available using the APT package manager. Read the wiki to learn more..."
tags: [Linux, CLI Tools]
category: [Linux, others]
cover: 'https://s1.ax1x.com/2020/06/26/NsmGxf.png'
thumbnail: 'https://s1.ax1x.com/2020/06/26/NsmGxf.png'
priority: 10000
---
## tmux2

![NsmGxf.png](https://s1.ax1x.com/2020/06/26/NsmGxf.png)

tmux is a very powerful interact-able bash interpreter. Once you familiarized with the hot keys, it would be an inextricable programs of you.

Copy and Past:

^b [ (ctrl+b [) : move the mouse;<br />^blanck: start to selecte; (hold this at less for a second)<br /> ^w: copy

Now, the selected words are in your copy list. You can using the favorite way to copy it in terminal, or Word, Atom, etc.<br />A typical way to past in tmux is:<br />^b ].


Or you can:<br />^B [;<br />Using mouse the select a target;<br />^w;

It works on turmx, but not on my laptop since when ever I typing ^+blank, the stupid Sugou Input will pop out and interrupt the processor...

Panes: Each window could split into small panes which is the key feature for tmux.

| Moves    | Keys     |
| :------------- | :------------- |
| Split Window horizontal | `ctrl`-`b` + `"` |
| Split Window Vertical| `ctrl`-`b` + `%` |
| Resize the width of the Panes | `ctrl`-`b` + `ctrl`-`→` |

Tips:
1. Panes resize:
    After you executed `ctrl`-`b`, you can hold `ctrl` and press the up, down, left, or right as many as you can until it fits you the best.