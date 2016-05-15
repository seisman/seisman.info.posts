---
title: 等震中距线的绘制
date: 2014-05-21 14:30
updated: 2015-11-03
author: SeisMan
categories: GMT
tags: [GMT, GMT技巧]
---

这里给出两个绘制等震中距线的方法，两种方法各有利弊，按需选取。

<!--more-->

## 等值线法

``` bash
#!/bin/bash
#
# This script works for GMT 4.5.13 only!
# You need to modify it if you use other versions of GMT.
# You should read notes below before you go.
#
R=g
J=H25c
B=60/30
PS=map.ps
evlo=160
evla=20

psxy -R$R -J$J -T -K > $PS
# 绘制底图
pscoast -J$J -R$R -B$B -Dc -A10000 -Glightblue -K -O >> $PS
# 绘制震中位置
echo $evlo $evla | psxy -J$J -R$R -Sa1c -Gred -K -O >> $PS

# 计算全球每点到震中的距离
gmtset ELLIPSOID Sphere
grdmath -R$R -I1 $evlo $evla SDIST KM2DEG = dist.nc
# 绘制等值线
grdcontour dist.nc -J$J -A15 -L0/60 -K -O >> $PS

psxy -J$J -R$R -T -O >> $PS

rm dist.nc
```

grdmath 命令首先将全球（`-Rg`）划分为间隔为 1 度（`-I1`）的网格，并计算每个网格点到固定
点 `evlo`、`evla` 的距离（单位为 km），然后将 KM 转换为度。则最终生成的 `dist.nc` 中
包含了每个网格点到固定点的距离。最好使用 `grdcontour` 命令绘制等值线，即等震中距线。
`grdcontour` 命令的众多选项可以对具体的等值线效果做微调。

对 `grdmath` 的若干说明：

1.  GMT 4.5.11 及之前的版本中，`SDIST` 的返回值单位为度；
2.  GMT 4.5.12 及之后的版本中，`SDIST` 的返回值单位为 km；
3.  GMT 5 中，`SDIST` 的返回值单位为 km；
4.  从 GMT 4.5.12 开始，新增了 `KM2DEG` 操作，但 4.5.12 版本的 `KM2DEG` 有问题；
5.  KM2DEG 操作仅适用于球状地球，因而要设置 `ELLIPSOID` 为 `Sphere`；
6.  KM2DEG 近似等效于 `111.19 DIV`；

![](/images/2014052101.jpg)

## 椭圆法

``` bash
#!/bin/bash
R=g
J=H25c
B=60/30
PS=map2.ps
evlo=160
evla=20

psxy -R$R -J$J -T -K > $PS
pscoast -J$J -R$R -B$B -Dc -A10000 -Glightblue -K -O >> $PS
echo $evlo $evla | psxy -J$J -R$R -Sa1c -Gred -K -O >> $PS

# 15 度等值线
echo $evlo $evla 0 3335.8 3335.8 | psxy -J$J -R$R -SE -K -O -W1p,red >> $PS
# 37.5 度等值线
echo $evlo $evla 0 8339.6 8339.6 | psxy -J$J -R$R -SE -K -O -W1p,blue >> $PS

psxy -J$J -R$R -T -O >> $PS
```

该方法使用了 `psxy` 的 `-SE` 选项。-SE 本是用于绘制椭圆的，这里被用来绘制圆以表示等震中距线。

该命令需要的输入数据有 5 个，分别是椭圆的中心经度、中心纬度、短轴的方位角、短轴长度（km）、长轴长度（km）。此处另短轴长度与长轴长度相等，即得到特殊的椭圆 -- 圆。

想要绘制一条震中距为 15 度的等震中距线，需要注意如下几点：

-   对于圆来说，其长轴 = 短轴 = 直径 = 30 度；
-   长轴和短轴的单位是 km，因而需要将震中距乘以 111.19 转换为 km。

![](/images/2014052102.jpg)

对于 GMT5，其提供了更简单的方法来绘制一个以千米为直径单位的圆，即 `-SE-` 选项，该选项需要 3 个参数：` 经度　纬度　圆直径 (km)` ，因而示例中的两条等值线命令在 GMT5 中可以简化成:

    # 15 度等值线
    echo $evlo $evla 3335.8 | gmt psxy -J$J -R$R -SE- -K -O -W1p,red >> $PS
    # 37.5 度等值线
    echo $evlo $evla 8339.6 | gmt psxy -J$J -R$R -SE- -K -O -W1p,blue >> $PS

## 修订历史

-   2014-05-21：初稿
-   2015-02-26： `grdmath` 在不同 GMT 版本下表现不同
-   2015-11-03：GMT5 中提供了 `-SE-` 选项，可以绘制以千米为直径单位的圆
