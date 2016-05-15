---
title: 绘制事件与台站间的连线
date: 2015-11-18
author: SeisMan
categories: GMT
tags: [GMT技巧]
---

地震学中，经常需要绘制事件到台站的连线或台站与台站之间的连线。连线沿着大圆路径，理论上用 `psxy` 命令即可实现，实际绘图时要更复杂一些。

<!--more-->

## 单事件多台站的连线

假定单个事件的位置保存在文件 `event.loc` 中:

    4.5 5

多个台站的位置保存到 `station.loc` 中:

    2 1
    5 8
    7 4
    9 6

### 旧方法

GMT 4.x 以及 GMT 5.1.x，要实现单事件与多台站之间的连线，只有一种方法，即构建多段数据。

多段数据中，每段数据包含两个点，分别是事件位置和台站位置， `psxy` 命令会将多段数据中每段里的两个点连起来。在本例中，多段数据 `raypath.xy` 的内容如下:

    >
    4.5 5
    2 1
    >
    4.5 5
    5 8
    >
    4.5 5
    7 4
    >
    4.5 5
    9 6

使用如下命令即可绘制单地震到多台站的连线：

``` bash
#!/bin/bash
#
# GMT 5.1.2
#
J=X10c/10c
R=0/10/0/10
PS=map.ps
gmt psbasemap -J$J -R$R -B1 -K > $PS

# 台站和事件位置
gmt psxy station.loc -J$J -R$R -St0.4c -Gblack -K -O >> $PS
gmt psxy event.loc -J$J -R$R -Sa0.8c -Gred -K -O >> $PS
# 连线
gmt psxy raypath.xy -J$J -R$R -W1p,blue -K -O >> $PS

gmt psxy -J$J -R$R -T -O >> $PS
```

绘图效果如下图：

![](/images/2015111901.png)

本方法的优点在于通用，缺点在于需要手动或写脚本，根据 `event.loc` 和 `station.loc` 的内容构建多段数据文件。

如何写脚本从 `station.loc` 和 `event.loc` 自动得到如上格式的文件，这是另外一个问题了，不在本文的讨论范围内。

### 新方法

GMT 5.2.1 增加了 `-F` 选项，可以更方便地实现事件与台站之间的连线。

``` bash
#!/bin/bash
#
# GMT 5.2.1
#
J=X10c/10c
R=0/10/0/10
PS=map.ps
gmt psbasemap -J$J -R$R -B1 -K > $PS

gmt psxy station.loc -J$J -R$R -St0.4c -Gblack -K -O >> $PS
gmt psxy event.loc -J$J -R$R -Sa0.8c -Gred -K -O >> $PS

gmt psxy station.loc -J$J -R$R -Fr4.5/5 -W1p,blue -K -O >> $PS

gmt psxy -J$J -R$R -T -O >> $PS
```

此处关键在于 `-Fr4.5/5` 选项，即以 `4.5/5` 作为参考点，将 `station.loc`
中的所有点与参考点做连线。

## 多事件多台站的连线

对于多事件多台站的连线，旧方法同理。新方法中，需要对事件进行循环，提取事件的位置信息，并多次使用 `psxy -Fr<evlo>/<evla>` 语法。

对 Bash 不了解，这个例子用 Perl 来实现。 `event.loc` 中包含了多个事件的位置:

    4.5 5
    5.5 5

``` perl
#!/usr/bin/env perl
#
# GMT 5.2.1
#

my $J  = "X10c/10c";
my $R  = "0/10/0/10";
my $PS = "map.ps";

system "gmt psbasemap -J$J -R$R -B1 -K> $PS";

system "gmt psxy station.loc -J$J -R$R -St0.4c -Gblack -K -O>> $PS";
system "gmt psxy event.loc -J$J -R$R -Sa0.8c -Gred -K -O>> $PS";

open(IN,"<event.loc");
foreach my $line (<IN>) {
    my ($evlo, $evla) = split " ", $line;
    system "gmt psxy station.loc -J$J -R$R -Fr$evlo/$evla -W1p,blue -K -O>> $PS";
}

system "gmt psxy -J$J -R$R -T -O>> $PS";
```

效果图：

![](/images/2015111902.png)

## 台站间相互连线

在做噪声成像之类的研究时，没有地震事件的概念，需要将台站之间互相连线，此时用 `-Fna` 选项即可。

``` bash
#!/bin/bash
#
# GMT 5.2.1
#
J=X10c/10c
R=0/10/0/10
PS=map.ps
gmt psbasemap -J$J -R$R -Bx60 -By30 -K > $PS

gmt psxy station.loc -J$J -R$R -St0.4c -Gblack -K -O >> $PS
gmt psxy station.loc -J$J -R$R -Fna -W1p,blue -K -O >> $PS

gmt psxy -J$J -R$R -T -O >> $PS
```

绘图效果如下图：

![](/images/2015111903.png)

## 说明

1.  构建多段数据是最通用的方法
2.  `-F` 选项的用法很丰富，详情见官方文档
