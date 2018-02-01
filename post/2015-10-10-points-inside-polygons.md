---
title: 判断点在多边形内
date: 2015-10-10
author: SeisMan
categories:
  - GMT
tags:
  - GMT技巧
slug: points-inside-polygons
---

在处理数据或绘图时，有时会需要判断点是否在一个封闭多边形内。比如想要筛选出某个多边形区域内的所有地震事件。GMT 的 `gmtselect` 命令可以实现这一需求。

<!--more-->

假设有一个多边形文件 `polygon.xy` ，其内容为:

    2 2
    7 5
    5 8
    4 7
    2 5

构成了一个不规则的多边形。

有一个数据点文件 `points.xy` ，其内容为:

    1 1
    3 3
    5 5
    7 7
    4 6
    6 8
    6 2

现在想要筛选出位于多边形内的所有数据点，可以使用 `gmtselect` 命令:

    $ gmt gmtselect points.xy -Fpolygon.xy
    3 3
    5 5
    4 6

画图验证一下：

``` bash
#!/bin/bash

J=X10c/10c
R=0/10/0/10
PS=test.ps

gmt psbasemap -J$J -R$R -B1 -K > $PS

# 绘制多边形
gmt psxy polygon.xy -J$J -R$R -W2p -L -K -O >> $PS
# 绘制所有数据点：红色圆圈
gmt psxy points.xy -J$J -R$R -Sc0.2c -Gred -K -O >> $PS
# 绘制多边形内的数据点：蓝色三角
gmt gmtselect points.xy -Fpolygon.xy | gmt psxy -J$J -R$R -St0.8c -W2p,blue -K -O >> $PS

gmt psxy -J$J -R$R -T -O >> $PS
```

上面的命令中， `gmtselect` 筛选出了 `points.xy` 的所有数据点中位于多边形
`polygon.xy` 中的点，通过管道传递给 `psxy` 命令。

![](/images/2015101001.png)

当然，也可以筛选出不在多边形内的点:

    $ gmt gmtselect points.xy -Fpolygon.xy -If
    1 1
    7 7
    6 8
    6 2

更多的选项及功能，参考 `gmtselect` 命令的语法说明。
