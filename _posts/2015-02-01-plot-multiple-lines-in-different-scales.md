---
title: 不同比例尺曲线的画法
date: 2015-02-01
author: SeisMan
categories: GMT
tags: [GMT技巧]
mathjax: true
---

本文由 Joe Wang（cjmuqiao@163.com）投稿。

## 目标效果图

![](/images/2015020101.png)

<!--more-->

## 问题的提出

在地磁场中 X、Y、Z 三分量幅值两两之间通常相差一两个数量级。如果直接将其画到相同比例尺的一个
坐标系下，幅值小的通常就成了一条直线。此时需要将大幅值适当缩小，或者小幅值适当放大，即在一张图
中绘制不同比例尺的曲线。在丁鉴海、卢振业、余素荣编著的《地震地磁学概论》中经常会看到不同比例
尺的图。

使用 GMT 的 `-Jx` 选项，绘图时 X 坐标或Ｙ坐标就会根据数据的范围进行缩放，但这种放大或
缩小的显示方式，会带来一个刻度值显示的问题。即：

1.  若将数据点用线连起来，由于数据点连线的时候不支持 `-N` 选项，则 `-R` 的范围必须包括
    整个 Y 轴的取值范围，Y 轴的刻度会完全显示，这样有点啰嗦；
2.  若使用 `-S` 选项，将数据点用某种符号显示，此时再加上 `-N` 选项，则可以只显示部分比例尺，
    同时又可以把数据完整地表示出来，但是这样的散点图看起来断断续续的，无法连接起来；

## 解决思路

1.  使用 `psxy` 将数据点用线连起来，此时不绘制刻度；
2.  选择要绘制的刻度的范围，并使用 `psbasemap` 绘制部分数据的 Y 轴刻度，在此之前需要
    仔细计算坐标原点在 Y 轴的偏移量。

## 脚本

-   软件环境：GMT5 windows 版，gawk
-   使用命令：`psxy`, `psbasemap`, `gmtmath`, `gawk` 等

``` batch
set sta=CHL
set day=20120101
set ps=%sta%%day%.ps
set Rhour=0/24/0/5
set Rsec=0/86400/0/5
set Jhour=x0.72/0.1
set Jsec=x0.0002/0.1

REM preparing the input data
REM 1. calculate mean value
REM 2. subtract mean value from original data
REM 3. output line number and data
gmt gmtmath CHL2_20120101Hx.dat CHL2_20120101Hx.dat MEAN SUB = | gawk "{print NR, $1}" > x.dat
gmt gmtmath CHL2_20120101Hy.dat CHL2_20120101Hy.dat MEAN SUB = | gawk "{print NR, $1}" > y.dat
gmt gmtmath CHL2_20120101Z.dat CHL2_20120101Z.dat MEAN SUB = | gawk "{print NR, $1}" > z.dat

gmt psxy -R%Rhour% -J%Jhour% -T -K -P >%ps%

REM plot x-axis
gmt psbasemap -R%Rhour% -J%Jhour% -Bxa2f1+lTime/hour -Bya5 -BS -K -O >>%ps%
gmt psbasemap -R%Rsec% -J%Jsec% -Bxa7200f3600+lTime/s -Bya5 -BS -Y2c -O -K >>%ps%

REM plot Z
gmt psxy z.dat -R0/86400/-20/15 -Jx0.0002/0.1 -O -K>>%ps%
REM plot scale of z data
gmt psbasemap -R0/86400/0/5 -J -Y2c -Bya5 -BW+t"@%%12%%\104@%%6%%Z" -K -O >>%ps%

REM plot Hy
gmt psxy y.dat -R0/86400/-400/400 -Jx0.0002/0.005 -Wblue -O -K >>%ps%
gmt psbasemap -R0/86400/100/200 -J -Y2.5c -Bya100+l"nT" -BW+t"@;blue;@%%12%%\104@%%6%%Y" --FONT=blue --MAP_DEFAULT_PEN=+blue --MAP_TITLE_OFFSET=0p -O -K >>%ps%

REM plot Hx
gmt psxy x.dat -R0/86400/-55/30 -Jx0.0002/0.05 -Wred -O -K >>%ps%
gmt psbasemap -R0/86400/10/20 -J -Y3.25c -Bya10 -BW+t"@;red;@%%12%%\104@%%6%%X" --MAP_TITLE_OFFSET=0p --FONT=red --MAP_DEFAULT_PEN=+blue -O -K >>%ps%

gmt psxy -R%Rhour% -J%Jhour% -T -O >>%ps%

del x.dat y.dat z.dat
del gmt.history
```

一些说明：

-   `gmtmath` 命令实现是一个逆波兰式的计算器，此处其作用在于先计算数据的均值，然后从原始数据中减去，并将计算得到的结果通过管道传送给 `gawk`；
-   绘制每个数据时，分别使用了两个命令，其中 `psxy` 用于绘制数据，而 `psbasemap` 用于绘制比例尺；
-   脚本中的参数的选择是有技巧，也是有规律的，下面会说明；
-   脚本中大部分数值都是可以从数据中自动计算得到的，因而将脚本改一改就可以实现完全的自动化；本文的脚本中没有对此进一步实现，如数据范围，移动距离等都是硬编码在脚本中；
-   命令中使用了一些额外的选项，来达到更好的绘图效果；

该脚本中某些参数的选取是很有技巧的，以 Z 分量数据为例：

-   psxy 命令中 `-R0/86400/-20/15` 是 Z 数据的范围，其值可以通过 `gmtinfo` 命令自动获得；
-   psxy 命令中 `-Jx0.0002/0.1`，即对于 Y 轴而言，数据的 1，在图上是 0.1 厘米，则 Z 数据的 35 的范围，对应于图上 3.5 厘米；
-   为了在 Y 轴的 0 到 5 处绘制一个比例尺，需要使用 psbasemap 命令，该命令有两个需要注意的地方：
    -   `-R0/86400/0/5` 设定了 Y 轴范围为 0 到 5；
    -   为了在真正的 0 处绘制比例尺，需要移动坐标系原点，此处的移动距离为 $(0-(-20))*0.1=2cm$，即 `-Y2c` 选项；

## 修订历史

-   2015-02-01：Joe Wang 投稿；
-   2015-02-01：SeisMan 整理语句、优化脚本；
-   2015-02-02：使用 FONT 和 MAP\_DEFAULT\_PEN 代替其他参数；
