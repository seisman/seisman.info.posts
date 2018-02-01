---
title: 全球数字高程模型 GTOPO30
date: 2013-08-11
author: SeisMan
categories:
  - 地球物理相关资源
tags:
  - GMT
  - 地形
  - 数据
  - 网格
  - 高程
slug: global-digital-elevation-model-gtopo30
---

GTOPO30 是 USGS 公布的全球数字高程模型，其采样间隔为 30 弧秒。

<!--more-->

## 下载

批量下载所有数据文件:

    wget -r -c -np -nd ftp://edcftp.cr.usgs.gov/data/gtopo30/global/

## 解压

    for i in *.tar.gz;
    do
        tar -zxvf $i;
    done

## 说明

在 README 里有详细说明，重点归纳如下

-   将全球分为 33 个区块，如下图所示，北纬 90 度到南纬 60 度分为 3 份，每份纬向 50 度，经向 40 度，共计 3\*9=27 个
    区块；南极附近为南纬 60 度到 90 度，经向 60 度，计 6 个区块，共计 33 个区块。

    ![](/images/2013081101.png)

-   采样间隔 30 弧秒，即 0.008333333333333 度，全球分为 21600 行、43200 列。
-   坐标参考为 WGS84；
-   其值为垂直方向高出海平面的距离，即海拔，单位为 m；
-   海拔范围 -407 到 8752，这里不包含海洋深度信息，负值应该是大陆架的海拔；
-   海洋处海拔标记为 -9999，海岸线以为大陆海拔至少为 1；
-   小于 1 平方千米的岛不考虑；
-   文件以该区块的左上角坐标为文件名；
-   文件后缀：DEM 为数据高程模型；其他的文件都是一些辅助信息；
-   纬度 50 度 \* 经度 40 度文件大小：57600000 bytes
-   纬度 30 度 \* 经度 60 度文件大小：28800000 bytes

## 复制

将所有 DEM 文件拷贝至 `$GMTHOME/share/dbase`

## 修改 grdraster.info

    # GTOPO30 N90-N40
    11 "GTOPO30 W180N90"            "m"     -R-180/-140/40/90       -I0.5m          PG i 1           0    -9999      W180N90.DEM B
    12 "GTOPO30 W140N90"            "m"     -R-140/-100/40/90       -I0.5m          PG i 1           0    -9999      W140N90.DEM B
    13 "GTOPO30 W100N90"            "m"     -R-100/-60/40/90        -I0.5m          PG i 1           0    -9999      W100N90.DEM B
    14 "GTOPO30 W060N90"            "m"     -R-60/-20/40/90         -I0.5m          PG i 1           0    -9999      W060N90.DEM B
    15 "GTOPO30 W020N90"            "m"     -R-20/20/40/90          -I0.5m          PG i 1           0    -9999      W020N90.DEM B
    16 "GTOPO30 E020N90"            "m"     -R20/60/40/90           -I0.5m          PG i 1           0    -9999      E020N90.DEM B
    17 "GTOPO30 E060N90"            "m"     -R60/100/40/90          -I0.5m          PG i 1           0    -9999      E060N90.DEM B
    18 "GTOPO30 E100N90"            "m"     -R100/140/40/90         -I0.5m          PG i 1           0    -9999      E100N90.DEM B
    19 "GTOPO30 E140N90"            "m"     -R140/180/40/90         -I0.5m          PG i 1           0    -9999      E140N90.DEM B

    # GTOPO30 N40-S10
    20 "GTOPO30 W180N40"            "m"     -R-180/-140/-10/40      -I0.5m          PG i 1           0    -9999      W180N40.DEM B
    21 "GTOPO30 W140N40"            "m"     -R-140/-100/-10/40      -I0.5m          PG i 1           0    -9999      W140N40.DEM B
    22 "GTOPO30 W100N40"            "m"     -R-100/-60/-10/40       -I0.5m          PG i 1           0    -9999      W100N40.DEM B
    23 "GTOPO30 W060N40"            "m"     -R-60/-20/-10/40        -I0.5m          PG i 1           0    -9999      W060N40.DEM B
    24 "GTOPO30 W020N40"            "m"     -R-20/20/-10/40         -I0.5m          PG i 1           0    -9999      W020N40.DEM B
    25 "GTOPO30 E020N40"            "m"     -R20/60/-10/40          -I0.5m          PG i 1           0    -9999      E020N40.DEM B
    26 "GTOPO30 E060N40"            "m"     -R60/100/-10/40         -I0.5m          PG i 1           0    -9999      E060N40.DEM B
    27 "GTOPO30 E100N40"            "m"     -R100/140/-10/40        -I0.5m          PG i 1           0    -9999      E100N40.DEM B
    28 "GTOPO30 E140N40"            "m"     -R140/180/-10/40        -I0.5m          PG i 1           0    -9999      E140N40.DEM B

    # GTOPO30 S10-S60
    29 "GTOPO30 W180S10"            "m"     -R-180/-140/-60/-10     -I0.5m          PG i 1           0    -9999      W180S10.DEM B
    30 "GTOPO30 W140S10"            "m"     -R-140/-100/-60/-10     -I0.5m          PG i 1           0    -9999      W140S10.DEM B
    31 "GTOPO30 W100S10"            "m"     -R-100/-60/-60/-10      -I0.5m          PG i 1           0    -9999      W100S10.DEM B
    32 "GTOPO30 W060S10"            "m"     -R-60/-20/-60/-10       -I0.5m          PG i 1           0    -9999      W060S10.DEM B
    33 "GTOPO30 W020S10"            "m"     -R-20/20/-60/-10        -I0.5m          PG i 1           0    -9999      W020S10.DEM B
    34 "GTOPO30 E020S10"            "m"     -R20/60/-60/-10         -I0.5m          PG i 1           0    -9999      E020S10.DEM B
    35 "GTOPO30 E060S10"            "m"     -R60/100/-60/-10        -I0.5m          PG i 1           0    -9999      E060S10.DEM B
    36 "GTOPO30 E100S10"            "m"     -R100/140/-60/-10       -I0.5m          PG i 1           0    -9999      E100S10.DEM B
    37 "GTOPO30 E140S10"            "m"     -R140/180/-60/-10       -I0.5m          PG i 1           0    -9999      E140S10.DEM B

    # GTOPO30 S60-S90
    38 "GTOPO30 W180S60"            "m"     -R-180/-120/-90/-60     -I0.5m          PG i 1           0    -9999      W180S60.DEM B
    39 "GTOPO30 W120S60"            "m"     -R-120/-60/-90/-60      -I0.5m          PG i 1           0    -9999      W120S60.DEM B
    40 "GTOPO30 W060S60"            "m"     -R-60/0/-90/-60         -I0.5m          PG i 1           0    -9999      W060S60.DEM B
    41 "GTOPO30 W000S60"            "m"     -R0/60/-90/-60          -I0.5m          PG i 1           0    -9999      W000S60.DEM B
    42 "GTOPO30 E060S60"            "m"     -R60/120/-90/-60        -I0.5m          PG i 1           0    -9999      E060S60.DEM B
    43 "GTOPO30 E120S60"            "m"     -R120/180/-90/-60       -I0.5m          PG i 1           0    -9999      E120S60.DEM B

## 其他说明

-   这些 DEM 文件为 Pixel Registration 格式
-   数据值存储为有符号 16 位整型
-   这些数据都是 Big-endian 的

## 绘图测试

``` bash
#!/bin/bash

ID=11
Range=-180/-140/40/90
B=a10g10
Inc=0.5m
PS=${ID}.ps

gmt grdraster $ID -R$Range -I$Inc -Gout.grd
gmt makecpt -Ctopo -T1/8000/1000 -Z > colors.cpt
gmt grdimage out.grd -B$B -R$Range -JQ15c -Ccolors.cpt > $PS

rm out.grd colors.cpt gmt.*
```

这里只绘制一个第一个区块的地形，若需要同时绘制多个区块，需要多次调用 `grdraster` 从不同的网格文件中提取网格，
然后用 `grdpaste` 粘贴成一个网格再绘图。

## 南极区域

在南极区域还有一个特殊的高程数据 `ANTARCPS.DEM`，其包含了 S60-S90 区域的六个区块的数据，但是是经过极坐标
方位立体投影的。因而横坐标范围为（-2700，2700），纵坐标范围为（-2700，2700）。这个处理起来要麻烦一点。
