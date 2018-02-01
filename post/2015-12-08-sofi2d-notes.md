---
title: SOFI2D 笔记
date: 2015-12-08
author: SeisMan
categories:
  - 地震学软件
tags:
  - 理论地震图
  - 有限差分
  - 笔记
mathjax: true
slug: sofi2d-notes
---

SOFI2D 是一个二维 PSV 交错网格有限差分代码。要使用该程序，至少需要阅读如下几篇参考文献：

-   Virieux, J. 1986. P-SV wave propagation in heterogeneous media:
    velocity-stress finite- difference method. Geophysics, 51(4), 889–901.
-   Levander, A.R. 1988. Fourth-order finite-difference P-SV seismograms. Geophysics, 53(11), 1425–1436.
-   SOFI2D User Guide

具体的用法及每个参数的意义在官方文档已经介绍的很详细，本文是我使用 SOFI2D 过程中的经验总结。

注：本文使用的是 2015 年 10 月 28 日发布的 SOFI2D。

<!--more-->

运行 SOFI2D 所需的文件都在 `par` 目录下，其中需要修改的文件包括：

-   `in_and_out/sofi2D.json`
-   `model/test`
-   `source/source.dat`
-   `receiver/receiver.dat`

`in_and_out/sofi2d.json` 是程序的输入配置文件，配置文件是用 json 语法写的，并且将众多的
变量分成了若干类。在设计不同的速度模型时，某些变量基本不需要改动，某些变量则可能需要经常改动。

在设计模型时，可以按照如下顺序逐一修改或检查如下参数：

1.  生成速度模型：2D 速度模型需要自己写程序生成，参考 `src/hh_elastic.c`
    和 `genmod/2layer.c` ，并将生成的模型保存到 `model` 目录下
2.  `source/source.dat` 中指定震源时间函数的中心频率（也可从文件中读入震源时间函数）、振幅和时间延迟
3.  估算震源时间函数的最大频率。如果是使用内置震源时间函数，可以近似认为最大频率是
    中心频率的两倍，如果是从文件中读入自定义的震源时间函数，可以对其做 FFT，将振幅谱中的拐点作为最大频率
4.  频散条件要求一个波长内要至少有 n 个网格点，因而要根据最大频率和最小速度计算出最大的网格间隔。在满足公式

    $$dh \le \frac{V_{min}}{n f_{max}}$$

    的前提下选择 $dh$ ，其中 n 由 `FDORDER` 决定

5.  为了满足稳定性条件，要根据网格间隔和模型中的最大速度选择合适的时间步长。在满足公式

    $$dt \le \frac{dh}{h \sqrt{2} V_{max}}$$

    的前提下选择 $dt$ 值，其中 h 由 `FDORDER` 决定

6.  修改 `in_and_out/sofi2d.json` 中的 `DH` 和 `DT`
7.  `source/source.dat` 中指定震源位置
8.  `receiver/receiver.dat` 中指定台站位置
9.  修改配置文件中的 2-D Grid 部分，指定 `NX` 和 `NY`
10. 根据计算机的核数以及 `NX` 和 `NY` 的值，修改 Domain Decomposition 部分
11. `startSOFI2D.sh` 中 `-np` 后面的进程数应与 `NPROCX*NPROCY` 相等
12. 修改配置文件中的 Time Stepping 部分
13. 如果要生成波场快照的话，则修改 Snapshots 部分

然后就可以开始计算了，每次修改模型之后，都需要按照上面的顺序检查各个参数。

使用过程中需要注意的一些地方：

1.  运行 SOFI2D 时目录名必须为 `par` ，该目录下各个子目录的名字不可变

    理论上运行目录是不是 `par` 都可以，各个子目录的名字在 `json`
    文件中也是可以任意设定的。但实际运行的过程中如果运行目录不是 `par`
    或者各个子目录的名字与默认的子目录名不一样都会直接报错退出。这实际上是代码
    `src/check_fs.c` 的 bug 导致的，该代码的目的在于检查文件系统，即目录
    是否存在，以及文件是否可读、可写。由于该代码将所有目录名硬编码在源码中，
    所以导致各个目录名不可修改。解决办法有两个：

    1.  把主程序中对 `check_fs` 的调用注释掉
    2.  保留原 par 目录，每次自己新建目录，这样 `check_fs` 每次都会检查
        `par` 目录，而不会检查新建的目录

2.  默认四个边界都是吸收边界， `FREE_SURF` 控制上表面是否为自由边界，
    `BOUNDARY` 控制左右是否为周期性边界条件
3.  交错网格结构的定义如下:

        Txx,Tzz   Ux


        Uz        Txz

    因而同一个网格点内的垂直分量要比水平分量深半个网格点。

4.  源码中 `src/update_v_interior.c` 是时间二阶，空间二阶有限差分格式，
    对应于 Virieux 1986，是最简单的一个
5.  计算出的理论地震图，到时应以 onset 为准，而不是以 peak 为准。
6.  sofi2d 与 fk，即便用完全相同的震源时间函数，其波形也是无法直接做对比的，
    因为 fk 计算的是点源三维波场，sofi2d 计算的是线源二维波场，因而 sofi2d 计算的结果需要做线源到点源的转换
