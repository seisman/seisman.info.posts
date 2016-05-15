---
title: 用 psxy 绘制铁轨线
date: 2016-03-30
author: SeisMan
categories: GMT
tags: GMT技巧
---

想要绘制黑白相间的铁轨线。既然是画线，肯定要用 `psxy` 了，但是 `psxy`
命令自身是不支持画这种黑白相间的线的，因而就需要使用一些技巧。具体技巧如下例：

``` bash
#!/bin/bash
R=0/10/0/5
J=M10c
PS=test.ps

gmt psbasemap -J$J -R$R -B1 -K > $PS

# Start rail tracks
gmt psxy line.txt -J$J -R$R -K -O -W5p,black        >> test.ps
gmt psxy line.txt -J$J -R$R -K -O -W4p,white,20_20: >> test.ps
# End rail tracks

gmt psxy -J$J -R$R -T -O >> $PS
```

简单说明一下原理，其实就是每条线画两遍。第一个 `psxy` 命令绘制了一条宽度为 `5p` 的黑线。第二个
`psxy` 命令绘制了一条宽度为 `4p` 的线，这条线的线型 `20_20:` 表示线段先是长度为 `20p` 的白线，
然后是长度为 `20p` 的空白，线段的空白段由于是透明的，所以会把第一次画的黑色线段露出来。
最终就实现了铁轨线的效果。

绘图效果如下：

![](/images/2016033001.png)
