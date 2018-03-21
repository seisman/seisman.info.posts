---
title: GMT 边框发虚的原因及解决办法
author: SeisMan
date: 2014-12-09
categories:
  - GMT
tags:
  - GMT技巧
slug: blurry-frame-in-gmt
---

GMT 绘制的 PS 格式的图片一向以高精度著称。在画图的时候偶尔会遇到，PS 图片中其他地方精度都很高，唯独边框看上去有些发虚，精度比较低。

上次遇到这个问题的时候，因为着急画图，所以也没细想，直接把边框发虚的图用上了。今天再次遇到这个问题，认真的想了想，找到了原因所在，也找到了解决办法。

<!--more-->

下面的脚本生成的 PS 文件，边框会存在发虚的现象：

``` bash
PS=test.ps
J=X14c
R=0/6/0/6
B=0.5/0.5

gmt psxy -R$R -J$J -T -K > $PS
gmt psxy -R$R -J$J -B$B -Sa1c -K -O >> $PS << EOF
1 1
EOF
gmt psxy -R$R -J$J -B$B -Sb1c -K -O >> $PS << EOF
2 2
EOF
gmt psxy -R$R -J$J -B$B -Sc1c -K -O >> $PS << EOF
3 3
EOF
gmt psxy -R$R -J$J -B$B -Sd1c -K -O >> $PS << EOF
4 4
EOF
gmt psxy -R$R -J$J -B$B -Ss1c -K -O >> $PS << EOF
5 5
EOF
gmt psxy -R$R -J$J -B$B -Sh1c -K -O >> $PS << EOF
2 3
EOF
gmt psxy -R$R -J$J -T -O >> $PS
```

代码很简单，无非就是多次调用 psxy 在不同的位置绘制不同的符号。

由于多次调用了 `psxy`，且每次都使用 `-B` 选项，所以在 PS 代码中实际上会多次重复绘制边框。
理论上这些边框以及刻度应该是完全重合的，但实际上却存在或多或少的偏差，进而导致最终画出的图
出现边框发虚的现象。

解决办法也很简单，保留第一个绘图命令中的 `-B` 选项，并删除其余命令中的 `-B` 选项。
这样画出来的图，文件大小要小一些，也不会再出现边框发虚的现象。

但，有时候会需要在 for 循环中重复调用类似的绘图命令，例如:

    gmt psxy -R$R -J$J -T -K > $PS

    for xxx
    do
        gmt psxy filen -R$R -J$J -B$B -Sxxx -K -O >> $PS
    done

    gmt psxy -R$R -J$J -T -O >> $PS

此时循环中的 `psxy` 命令，每次执行时都有 `-B` 选项，这也是最容易导致边框发虚的情况。如果
把循环里的 `-B` 选项去掉，又会导致没有边框。唯一的办法是把循环中的 `-B` 去掉，然后在循环
之前或之后的某个命令中加上 `-B` 选项绘制边框，实在没有绘图命令的话就使用 `psbasemap`
专门绘制边框。
