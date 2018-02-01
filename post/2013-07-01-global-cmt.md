---
title: Global CMT 信息整理
date: 2013-07-01
author: SeisMan
categories:
  - 地球物理相关资源
tags:
  - 地震目录
  - 震源机制解
  - 震级
slug: global-cmt
---

Global CMT 全称 Global Centroid-Moment-Tensor Project，前身是 Harvard CMT，
是地震学常用的地震目录和震源机制之一。其给出了自 1976 年以来上万个地震的
地震目录以及震源机制。

<!--more-->

## 主页

<http://www.globalcmt.org/>

## Catalog 在线查询

<http://www.globalcmt.org/CMTsearch.html>

可以指定时间段、震级范围、震中范围、深度范围，也可以对震源时间函数以及 T 轴
和 N 轴进行限制。并支持多种输出格式，其中的 `GMT psmeca input` 格式可以直接
用于 GMT 绘图。

## Catalog 直接下载

<http://www.globalcmt.org/CMTfiles.html>

很多时候我们需要根据其他条件对 catalog 进行筛选，得到符合自定义条件的地震事件，所以 ASCII 格式的
目录文件就很重要了。GCMT 提供了 1976 年到现在的地震目录，其中 1976-2004 年的地震目录为 dek 格式，
包含在一个文件中。2005 年以后的地震目录为 ndk 格式，每月一个文件。对于 2005 年以后的地震目录可以
将一年的目录合并到一个文件中，方便管理且不会导致文件过大。

- [1976-2004 目录](http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/jan76_dec04.dek)
- [2005 以后目录](http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/NEW_MONTHLY/)
- [ndk 格式说明](http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/allorder.ndk_explained)
- [dek 格式说明](http://www.ldeo.columbia.edu/~gcmt/projects/CMT/catalog/allorder.dek_explained)

## 关于 GCMT 的文章

-   [1981](http://www.agu.org/pubs/crossref/1981/JB086iB04p02825.shtml)
-   [1983](http://www.agu.org/pubs/crossref/1983/JB088iB04p03247.shtml)
-   [2012](http://www.sciencedirect.com/science/article/pii/S0031920112000696)

## 备注

-   GCMT 中给出的地震矩单位是 `dyne-cm`，而不是国际单位制的 `N-m`。
-   GCMT 目录的 ASCII 文件中震级采用 mb 和/或 MS，为什么不用矩震级？使用面波和体波震级的最大问题是
    震级饱和，导致震级基本不会超过 8 级。
