---
title: 洋壳年龄数据
date: 2014-05-17
author: SeisMan
categories: 地球物理相关资源
tags: [数据, 网格, GMT]
---

## 简介

官方网站： <http://www.earthbyte.org/Resources/agegrid2008.html>

该数据集包含四类数据：洋壳年龄（age）、年龄不确定度（ageerror）、扩张速度（rate）、扩张非对称性（asym）。数据最高精度为 2 弧分。

数据下载地址：<ftp://ftp.earthbyte.org/earthbyte/agegrid/2008/Grids/>

数据文件名的命名方式为:

    数据类型. 数据版本. 数据分辨率. 数据格式. bz2

比如 `age.3.2.nc.bz2` 表示洋壳年龄数据，版本号为 3，数据精度为 2 弧分，格式为 netCDF 格式。

## 数据的使用

官方提供了三种格式的数据，img 格式、netCDF 格式以及 XYZ 格式。综合各种情况，这里只用 netCDF 格式，其它格式的使用请参考 `README.txt` 。

### netCDF 格式

-   短整型 netCDF 格式
-   年龄单位为百万年，扩展速率单位为 mm/yr。并对数据乘以 100 以使得其可以用短整型保存。
-   经度范围为 0 到 360 度，纬度范围为 - 90 到 90。
-   数据精度为 2 弧分；
-   网格线配准

### 数据解压

    bzip2 -d age.3.2.nc.bz2

### 数据转换

由于真实数据被乘以 100 以使得数据可以用短整型表示，所以在使用之前要将数据乘以因子 0.01。可以通过如下命令进行转换:

    grdmath age.3.2.nc=ns 0.01 MUL = age.3.2.nc2=nf -V

### 绘图

``` bash
#!/bin/bash
R=d
J=W20c
B=60/30
PS=age.ps
psxy -R$R -J$J -T -K > $PS
grdimage -R$R -J$J -B$B -Cage.cpt age.3.2.nc2 -K -O >> $PS
pscoast -R$R -J$J -B$B -Glightblue -K -O >> $PS
psscale -Ba20 -Cage.cpt -D10.5c/-1c/15c/.35ch -K -O >> $PS
psxy -R$R -J$J -T -O >> $PS
```

绘图效果

![](/images/2014051701.jpg)
