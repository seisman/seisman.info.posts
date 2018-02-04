---
title: 全球数字高程数据：ASTER GDEM
date: 2014-01-12
author: SeisMan
categories:
  - 地球物理相关资源
tags:
  - 地形
  - 数据
  - 格式转换
  - GMT
  - 高程
slug: aster-gdem
---

## 简介

ASTER GDEM，即先进星载热发射和反射辐射仪全球数字高程模型，与 SRTM 一样为数字高程 DEM，
其全球空间分辨率为 30 米。该数据是根据 NASA 的新一代对地观测卫星 Terra 的详尽观测结果
制作完成的。其数据覆盖范围为北纬 83° 到南纬 83° 之间的所有陆地区域，达到了地球陆地表面的
99%。号称是 “迄今最完整的全球地形数据”。

数据下载地址：

- [NASA Reverb](http://reverb.echo.nasa.gov/reverb/)
- [LP DAAC Global Data Explorer](http://gdem.ersdac.jspacesystems.or.jp)

<!--more-->

## 基本信息

空间分辨率：1 弧度秒 （约 30 米）

精度：垂直精度 20 米，水平精度 30 米

更多信息： <http://www.gscloud.cn/userfiles/file/gdem3.pdf>

## 其他信息

-   网站需要注册，即可免费下载数据；
-   点击 “Search” 即可进入数据选择界面；
-   数据被划分为 1 度 \*1 度的区块，每个区块文件名以区块左下角的经纬度值来命名；
-   数据选择界面有四种方式用来选择区块，界面的设计不太习惯，注意看英文；
-   数据可以单独下载，也可以批量下载；批量下载貌似需要处理一段时间；
-   下载的文件为 zip 压缩文件，包含了两个文件：dem 和 num，二者均为 GeoTiff 格式；
-   dem 数据即为数字高程数据；
-   num 数据也称为 QA 文件，即质量评估文件，其包含了每一点的高程数据的来源等信息，一般用不到；

## 格式转换

使用 GDAL 提供的工具将其转换为 GMT 可识别的 netCDF 格式:

    gdal_translate -of GMT ASTGTM2_N36E111_dem.tif ASTGTM2_N36E111_dem.nc

关于 GDAL，见 [GDAL/OGR: 地理空间数据格式转换神器](http://gmt-china.org/blog/gdal-ogr/) 一文。

## 与 SRTM 的区别

-   SRTM 数据的纬度覆盖范围是 [-60,60]，ASTER GDEM 数据的纬度覆盖范围为 [-83,83]；
-   SRTM 的空间分辨率一般为 90m，只有美国境内存在空间分辨率为 30m 的数据；ASTER GDEM 的空间分辨率为 30m；

## 数据合并

可以使用 GMT 自带的 `grdpaster` 命令将两个相邻的网格文件合并起来。

-   GMT 4.5.13 的 `grdpaste` 有问题，会出现 “Grids do not share command edge.” 的错误；
-   GMT 5.1.2 的 `grdpaste` 没有问题；
