---
title: 全球地形起伏数据总结
date: 2013-09-30
author: SeisMan
categories: GMT
tags: [数据, 网格, 地形, 高程]
---

本文收集了已知的可公开下载使用的全球地形起伏数据。

<!--more-->

这里有个概念是混乱的。有些数据只有陆地部分的地形，有些数据有陆地和海洋的地形，
或许前者应该称为数字高程数据，后者称为地形起伏数据。做大地测量的应该更清楚这些
专业名词。这里统称为地形数据。

博客中提到的地形数据，按照分辨率从低到高排序如下：

-   etopo5：[GMT 网格数据之 etopo5](/global-relief-model-etopo5.html)
-   etopo2：[GMT 网格数据之 ETOPO2v2](/global-relief-model-etopo2.html)
-   etopo1：[GMT 网格数据之 ETOPO1](/global-relief-model-etopo1.html)
-   GEBCO：[GEBCO：全球水深数据](/gebco-global-bathymetry-data.html)
-   GTOPO30：[GMT 网格数据之 GTOPO30](/global-digital-elevation-model-gtopo30.html)
-   SRTM30\_PLUS：[全球地形起伏数据：SRTM30\_PLUS](/srtm30-plus.html)
-   SRTM15\_PLUS：[全球地形起伏数据：SRTM15\_PLUS](/srtm15-plus.html)
-   SRTM3：[高精度地形网格数据 SRTM](/srtm.html)
-   ASTER GDEM：[全球数字高程数据：ASTER GDEM](/aster-gdem.html)

整理如下表：

| 数据源       | 空间分辨率        | 覆盖范围      | 陆地 / 海洋 |
|:-------------|:------------------|:--------------|:------------|
| etopo5       | 5 弧分            | 全球          | 陆地 + 海洋 |
| etopo2       | 2 弧分            | 全球          | 陆地 + 海洋 |
| etopo1       | 1 弧分            | 全球          | 陆地 + 海洋 |
| GEBCO        | 1 弧分 / 30 弧秒  | 全球          | 陆地 + 海洋 |
| GTOPO30      | 30 弧秒           | 全球          | 陆地        |
| SRTM30\_PLUS | 30 弧秒 (约 1km)  | 纬度 [-81,81] | 陆地 + 海洋 |
| SRTM15\_PLUS | 15 弧秒 (约 500m) | 纬度 [-81,81] | 陆地 + 海洋 |
| SRTM         | 3 弧秒 (约 90m)   | 纬度 [-60,60] | 陆地        |
| ASTER GDEM   | 1 弧秒 (约 30m)   | 纬度 [-83,83] | 陆地        |

说明如下：

-   GEBCO 是目前空间分辨率最高的全球地形起伏数据；
-   ASTER GDEM 是目前空间分辨率最高的数字高程数据；
-   对于全球尺度或者大尺度地形图来说，可以使用 etopo1 甚至 etopo5 数据；
-   对于 3 度 \*3度-10度\*10 度的区域，可以使用 SRTM30\_PLUS 数据；
-   对于 3 度 \*3 度以下的区域，可以使用 SRTM 或 ASTER GDEM 数字数据。
-   如果有特殊需求的话，可以用 ASTER
    GDEM 绘制陆地地形，用 GEBCO 绘制海底地形；

## 修订历史

-   2013-09-30：初稿；
-   2015-04-07：增加了 SRTM15\_PLUS；
