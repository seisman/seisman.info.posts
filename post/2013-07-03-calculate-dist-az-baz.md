---
title: 震中距、方位角和反方位角的计算
date: 2013-07-03
lastmod: 2014-10-28
author: SeisMan
categories:
  - 地震学软件
tags:
  - C
  - Fortran
  - Java
  - Python
  - Matlab
  - 名词解释
slug: calculate-dist-az-baz
---

给定震中经纬度以及球面上任意一点（一般是台站）的经纬度，计算震中距、方位角以及反方位角。
这是地震学的一个基本问题。

<!--more-->

## 名词解释

-   震中距：**地面**上任意一点到**震中**的球面距离；
-   方位角：震中到台站的连线与地理北向的夹角；
-   反方位角：台站到震中的连线与地理北向的夹角；

一张图可以说明一切:

![图 1：震中距、方位角 (az)、反方位角 (baz) 示意图](/images/2013070301.png)

## 数学推导

公式的推导需要简单的球面三角函数的知识。具体的推导可以参考 Robert B. Herrmann 的
[作业题](http://www.eas.slu.edu/People/RBHerrmann/Courses/EASA462)。
作业题中的 Ass06、Ass07、Ass08 给出了计算震中距和方位角的原理。

## 相关代码

广为流传的一个程序是 `distaz`。在 GMT、SAC 等的源码里都可以找到。`distaz` 代码很短，简单易懂，
其采用的地球模型为椭球模型，精度上可以满足需求。

-   C、Fortran、Java、Python 以及 CGI 版本： [由 USC的一个小组 整理](http://www.seis.sc.edu/software/distaz/)
-   Matlab 版本： [由 specfem3d\_globe 提供](https://github.com/geodynamics/specfem3d_globe/blob/master/utils/Visualization/VTK_ParaView/matlab/distaz.m)

## 使用方法

仅以 C 语言版本的 `distaz` 为例，用如下命令即可编译:

    cc distaz.c -o distaz -lm

其输入为 `sta_lat sta_lon evt_lat evt_lon` ，输出为 `Delta Baz Az` 。

    $ ./distaz 10 14 40 50
    43.731 40.781 236.882

## 修订历史

-   2013-07-03：初稿；
-   2014-07-06：加入了对 `distaz` 的用法的说明；删除了 CPS330 的部分；
-   2014-10-28：新增 matlab 版本；
