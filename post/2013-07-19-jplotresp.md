---
title: JPlotResp：绘制地震仪器响应
date: 2013-07-19
author: SeisMan
categories:
  - 地震学软件
tags:
  - Java
  - 仪器响应
slug: jplotresp
---

要理解仪器响应，就要看 RESP 的格式，更重要是直观地看仪器响应的振幅相位谱。

前面介绍的 [RESP 文件](/simple-analysis-of-resp.html) 和 [SAC PZ](/simple-analysis-of-sac-pz.html)
文件都只是给出了一堆零极点以及放大系数等各种参数。JPlotResp 是用来绘制地震仪器响应的
软件，可以帮助直观地看到任意台站的仪器响应。

主页： <http://www.isti2.com/JPlotResp/>

<!--more-->

## 简介

-   Java 语言
-   底层由 JEvalResp 计算仪器响应
-   JEvalResp 是 evalresp 的 Java 版本

## 功能

-   支持在线查询，指定台网、台站以及时间即可；
-   直接绘制本地 Resp 文件；
-   支持多种仪器响应：速度、加速度、位移；
-   绘制振幅相位谱、复数谱；
-   指数坐标或者线性坐标；

## 截图

![JPlotResp 启动界面](/images/2013071901.jpg)

![读取本地RESP文件](/images/2013071902.jpg)

![绘制振幅响应谱](/images/2013071903.jpg)
