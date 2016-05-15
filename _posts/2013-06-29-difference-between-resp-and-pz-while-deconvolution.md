---
title: 用 RESP 和 PZ 去除仪器响应的差别
date: 2013-06-29
updated: 2013-07-06
author: SeisMan
categories: 地震学基础
tags: 仪器响应
---

前面介绍了 [仪器响应文件 RESP](/simple-analysis-of-resp.html) 和
[仪器响应文件 SAC\_PZ](/simple-analysis-of-sac-pz.html)，下面分别用两种
响应文件进行去仪器响应，比较二者的区别。

<!--more-->

## 样例下载地址

[SAC 数据](http://seisman.qiniudn.com/downloads/2013.144.05.40.09.0195.IU.COLA.00.BHZ.M.SAC)
[RESP 文件](http://seisman.qiniudn.com/downloads/RESP.IU.COLA.00.BHZ)
[PZ 文件](http://seisman.qiniudn.com/downloads/SAC_PZs_IU_COLA_BHZ_00)

## RESP 去除仪器响应

    $ sac
    SEISMIC ANALYSIS CODE [02/01/2012 (Version 101.5c)]
    Copyright 1995 Regents of the University of California

    SAC> r ./2013.144.05.40.09.0195.IU.COLA.00.BHZ.M.SAC
    SAC> rmean; rtr; taper
    SAC> trans from evalresp fname ./RESP.IU.COLA.00.BHZ to none freq 0.01 0.05 5 7
    Using response from user-specified file: (./RESP.IU.COLA.00.BHZ).
    Extracting evresp response for COLA, BHZ...
    Station (COLA), Channel (BHZ)
    SAC> w RESP.SAC
    SAC> q


## PZ 去除仪器响应

    $ sac
    SEISMIC ANALYSIS CODE [02/01/2012 (Version 101.5c)]
    Copyright 1995 Regents of the University of California

    SAC> r ./2013.144.05.40.09.0195.IU.COLA.00.BHZ.M.SAC
    SAC> rmean; rtr; taper
    SAC> trans from polezero subtype ./SAC_PZs_IU_COLA_BHZ_00 to none freq 0.01 0.05 5 7
    Using polezero response for COLA, BHZ, IU, 00...
    Station (COLA), Channel (BHZ)
    SAC> w PZ.SAC
    SAC> q

## 结果对比

-   对比生成的两个 SAC 文件，波形很类似。 `RESP.SAC` 的最值在 10 的 6 次方量级， `PZ.SAC` 的最值在
    10 的 -3 次方量级，这是 **单位** 的问题。首先 SAC 的默认的位移单位为 `nm`。RESP 文件中有指定仪器的
    输入单位为 `m/s`，这行虽然以 `#` 开头，其在去仪器响应的时候是可以被 SAC 读取的，因而利用 RESP 去仪
    器响应时 SAC 知道输入的单位是什么，SAC 自然也会进行单位的转换。而 PZ 文件中虽然给出了输入单位为 `m`，
    但 PZ 文件中以 `*` 开头的行是被忽略的，所以 SAC 其实并不知道仪器的输入单位是什么，直接去仪器响应，
    得到的波形单位为 m，而 SAC 在不知道单位的情况下 “自作聪明” 直接将其单位改写成了 `nm`，这就导致了波形
    振幅量级上的错误。因而 **SAC 在利用 PZ 文件去仪器响应的时候要乘以 10 的 9 次方进行单位转换**。
-   对单位进行校正后，对二者做互相关，发现互相关的结果峰值位于 0 处，这意味着二者不存在时间延迟的问题。
    PZ 文件中没有任何时间延迟的概念，而 RESP 中在滤波过程中存在时间延迟，并给出了延迟估计和延迟校正。
    互相关峰值在 0 处意味着在用 RESP 做反卷积的时候对数字滤波器做了反卷积，并且对时间问题做了校正。
-   对两个相似的波形做差，其差值在 10 的 2 次方量级，大概占信号的千分之一，这个误差也许是因为 PZ 文件
    没有将全部阶段考虑进去导致的，不过这个影响很小。
-   PZ 文件中没有考虑 FIR 滤波器的响应函数，因而在 Nyquist 频率附近会出现失真。

## 参考

1.  [EarthScope 2009 workshop](http://www.iris.edu/hq/es_course/content/2009.html)
    Session 2

## 修订历史

-   2013-06-29：初稿；
-   2013-07-06：修改了 “结果对比” 中第一点的说明；
-   2015-11-11：PZ 文件中有无注释行对运行效率基本没有影响
