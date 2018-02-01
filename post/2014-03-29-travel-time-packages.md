---
title: 走时计算软件包
author: SeisMan
date: 2014-03-29
lastmod: 2017-03-31
categories:
  - 地震学软件
tags:
  - 走时
  - TauP
slug: travel-time-packages
---

地震波走时的计算是地震学的一个基本问题。下面列出几个目前已知的几个可以计算地震波走时的包。

<!--more-->

以下软件按照功能性、方便性等综合排序：

1.  TauP Toolkit

    网址： <http://www.seis.sc.edu/taup/>

    Java 版，具体良好的跨平台能力。包含图形界面和命令行工具，是目前来说最好用的走时计算工具，但是其还是有一些缺憾，最明显的一点是在命令行的输出对于脚本批量处理不算友好。

2.  ObsPy TauP

    网址： <http://docs.obspy.org/packages/obspy.taup.html>

    Python 版本，简单易用，但目前功能还没有Java版TauP丰富。相比于Java版的优势在于，其可以将数据以完整精度输出，而 Java 版 TauP 很多数据只能输出小数点后两位。

3.  MatTauP

    网址：<https://github.com/g2e/seizmo/tree/master/mattaup>

    Matlab 版，是 seiszmo 项目的一部分，底层貌似调用了 Java 版 TauP 的代码。

4.  Cake

    网址： <http://emolch.github.io/pyrocko/current/cake_doc.html>

    Python 版，Pyrocko 项目的一部分，支持自定义模型，且可以处理更复杂的震相名。

5.  George Helffrich 修改版

    网址： <http://www1.gly.bris.ac.uk/~george/sac-bugs.html#ttimes>

    Fortran 版本，该版本是在 ttimes 的基础上修改得到，相比 ttimes，加入了更多的速度模型，可以直接编译使用。

6.  iaspei-tau

    网址： <https://seiscode.iris.washington.edu/projects/iaspei-tau>

    原始的 ttimes 的修改版本，支持 ak135 和 iasp91 模型。

7.  IASPEI Travel Time Software - AK135 version

    网址： <http://rses.anu.edu.au/seismology/soft/ttsoft.html>

    这个版本的源码比较古老，可能是用 Fortran77 甚至更老的版本写的。曾经试图编译，发现很多语法编译器已经不再支持，改起来应该不困难，但是有些繁琐，不建议使用。且该版本只支持 ak135 模型。

这几个软件都是基于同一个原理，参考如下：

Buland, R. and C. H. Chapman (1983). The Computation of Seismic Travel Times, Bull. Seism. Soc. Am. 73(5),1271–1302.

## 修订历史

-   2014-03-29：初稿
-   2016-02-24：新增 cake
-   2017-03-31：新增 obspy.taup
