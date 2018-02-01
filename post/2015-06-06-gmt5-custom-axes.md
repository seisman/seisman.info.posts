---
title: GMT5 自定义坐标轴
date: 2015-06-06
author: Joe Wang
categories:
  - GMT
tags:
  - GMT技巧
slug: gmt5-custom-axes
---

## 问题的提出

GMT 绘图时可以使用 `-B` 选项指定每个坐标轴的刻度、标注以及网格线。默认情况下的设置有时可能无法
满足需求，比如想要在特定位置设置刻度，比如任意格式的日期、非 log10 的刻度等，就需要自己设置了。

<!--more-->

## 解决方案

GMT5 的 `-B` 选项，使用 `-B[p|s]x|ycYourTickFileName` 语法可以自定义轴的标注及刻度。

## 示例

想要画一张中国西南地区 2008\~2013 年地震活动性的 XY 图，要求：

1.  X 坐标的 Primary 标注是 `yyyymmdd` 日期格式；
2.  Secondary 刻度位于每个季度的最后一天，比如，2008 年第一季度 20080331，第二季度 20080630，第三季度 20080930。

代码如下：

``` bash
input=chuandian_eq.txt
title="Southwest China Seismicity"
PS=chuandian_seismicity.ps
J=X6i/2i
R=1/2192/3/9

gmt psbasemap -J$J -R$R -BWSen+t"$title"  -Bya1f0.5+lMagnitude -BpxcDateTick_px.txt -P -K > $PS
gmt psbasemap -J$J -R$R -BsxcDateTick_sx.txt -K -O >> $PS
awk '{print $1, $3}' $input | gmt psxy -JX6i/2i -R1/2192/3/9 -Sc0.1c -W1p,black -O >> $PS
rm gmt.*
```

成图效果：

![](/images/2015060601.png)

代码说明：

1.  `chuandian_eq.txt` 中包含了中国西南 2008\~2013 年大于等于 4 级地震事件，文件有三列，第一列是从 20080101 为第一天起算的日期序号，第二列是日期，第三列是震级，格式如下:

        32 20080201 4.800000
        47 20080216 4.400000
        58 20080227 5.000000
        95 20080404 4.100000
        ...

2.  `DateTick_px.txt` 用于控制 Primary 标注。其内容有三列，第一列是标注的 X 坐标，第二列可以是 `a` 或 `f` 或 `g`，这里使用的是 `a`，表示当前文件控制的是标注 (annotations)，第三列是用户自定义的要显示的标注，如:

        1 a 20080101
        367 a 20090101
        732 a 20100101
        1097 a 20110101
        1462 a 20120101
        1828 a 20130101
        2192 a 20131231

3.  `DateTick_sx.txt` 用于控制 Secondary 刻度 (frame)，其内容如下:

        91  f 20080331
        182 f 20080630
        274 f 20080930
        456 f 20090331
        547 f 20090630
        639 f 20090930
        821 f 20100331
        912 f 20100630
        1004 f 20100930
        1186 f 20110331
        1277 f 20110630
        1369 f 20110930
        1552 f 20120331
        1643 f 20120630
        1735 f 20120930
        1917 f 20130331
        2008 f 20130630
        2100 f 20130930

4.  似乎一个命令中只能使用一次自定义轴语法，故而这里使用了两次 `psbasemap`，分别完成
    Primary 标注和 Secondary 刻度的绘制，然后再调用 `psxy` 绘制具体数据。

## 修订历史

1.  初稿 By Joe Wang(<cjmuqiao@163.com>)；
