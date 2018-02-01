---
title: IRIS 的理论地震图生成引擎
author: SeisMan
date: 2016-05-26 12:41:18
categories:
  - 地震学软件
tags:
  - IRIS
  - 理论地震图
slug: iris-syngine
---

通过看理论地震图有助于我们理解实际数据中的很多现象，但自己算理论地震图却不是
一个简单的事情，既需要有相关代码还需要理解理论地震图计算的原理，还需要足够的
计算机资源以及计算时间。

IRIS 的 Syngine 服务使用 [AxiSEM](http://seis.earth.ox.ac.uk/axisem/) 计算得到
格林函数，并使用 [Instaseis](http://www.instaseis.net/index.html) 得到理论地震图。
该服务提供了 PREM、AK135、iasp91 等多个模型下高达 1 Hz 的理论地震图，用户可直接
下载使用，省去了自己计算的麻烦。

下面列出相关网页：

1. 项目主页： <http://ds.iris.edu/ds/products/syngine/>
2. 网页版下载工具： <https://service.iris.edu/irisws/syngine/1>
3. 命令行下载工具： [FetchSyn](https://seiscode.iris.washington.edu/projects/ws-fetch-scripts/wiki/FetchSyn_usage)
4. 用 ObsPy 下载理论地震图： [Using Syngine with ObsPy](http://nbviewer.jupyter.org/gist/krischer/3e655576e4d17e6c95f2)
5. AxiSEM 计算时所使用的输入模型文件: http://ds.iris.edu/ds/products/emc-syngine/
