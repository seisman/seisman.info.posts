---
title: 绘制波形对比图
date: 2013-09-15
author: SeisMan
categories:
  - GMT
tags:
  - GMT技巧
  - pssac
slug: waveform-comparison-plot
---

波形对比图，经常出现在如下场合：

1.  发展新的计算理论地震图的方法，与前人的结果做 Benchmark；
2.  理论地震图与实际数据做对比，比如反演；
3.  展示多个波形的相关性；如 doublet；

如下图所示，红色的三个 trace 是某差分程序计算出的地震图，黑色的三个 trace 是 fk 计算出的地震图，也就是上面的第一种情况：

![](/images/2013091501.jpg)

<!--more-->

画地震波形肯定是要用 pssac 的，当初的做法是先用 psbasemap 绘制整体的边框，然后用六个 pssac 命令分别绘制
每个 trace，并使用 - Y 选项分别微调每个 trace 的垂直位置，这显然是一种非常笨的方法，尤其是在有很多个 trace 的情况下。

更好的绘图脚本如下：

``` bash
#!/bin/bash
J="X6i/4i"
B="0.2/1WeSn"
R="0.4/2.0/0/4"
PS="traces.ps"

pssac -J$J -R$R -B$B -W1p/red -M1 -Ent-3 syn.* -K > $PS
pssac -J$J -R$R -W1p/black -M1 -Ent-3 homo.* -O -Y0.1i >> $PS
```

这个脚本调用了两次 pssac 命令，第一个 pssac 绘制了三条红色的 trace，同时绘制了底图和边框；第二个 pssac
命令绘制了三条黑色的 trace，使用 - Y 选项实现垂直方位偏离。

第二个 pssac 命令中另一个特殊的地方在于没有使用 - B 选项。若有 - B 选项，则会出现两个边框，看上去是两张图的重叠与交错；
而没有 - B 选项，两张图重叠在一起，看上去却是一张图，实现了波形对比的效果。这里充分利用了 - B 选项功能。
