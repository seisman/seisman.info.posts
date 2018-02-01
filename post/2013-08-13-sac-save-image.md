---
title: SAC 保存图像小结
date: 2013-08-13
author: SeisMan
categories:
  - SAC
tags:
  - SAC技巧
  - 图像
slug: sac-save-image
---

数据的处理很重要，数据的可视化更重要，数据可视化之后总会想把图保存起来，这里小结一下 SAC 中保存图像的方法。

<!--more-->

## 窗口绘图并截图

SAC 中的绘图窗口基于 XWindows。XWindows 大概是 Linux 下非常常见的视窗系统。在 SAC 中可以通过
plot，plot1，plot2，plotpk 等命令实现 SAC 数据的绘制以及各种交互动作（主要就是标记震相）。
最简单粗暴的方法大概就是截屏了。截屏的话 gnome 下有个 screenshot，可以截取整个屏幕；推荐安装
ImageMagick，其中的 import 命令可以通过鼠标拖曳一个区域进行截图，貌似支持保存为很多种格式。

## 生成 SGF 文件再转换

SGF 是 SAC Graphic
File 的简称，这是 SAC 自己设计的图像格式，里面包含了 SAC 图像的基本信息。在 SAC 中打开 SGF 设备 -\>
绘图产生 SGF 文件 -\> 退出 SAC-\> 利用 sgftops 将 sgf 文件转换为 ps 文件 -\>ps2pdf 转换为 pdf 文件。

    $ sac
    SEISMIC ANALYSIS CODE [02/01/2012 (Version 101.5c)]
    Copyright 1995 Regents of the University of California

    SAC> fg seis
    SAC> bd sgf
    SAC> p
    SAC> q
    [seisman@info ~]$ sgftops f001.sgf f001.ps 2 si
    First translates (x and y), then rotates, then scales:
    [Default] landscape: 8 0 90 1 to prompts
    Sample portrait: 0.5 0.5 0 0.75

    x translation : 0.5
    y translation : 0.5
    rotation angle: 0
    scale........ : 0.75
    [seisman@info ~]$

## SAVEIMG 直接保存图形文件

SAC 101.5 之后的版本加入了新功能，可以直接保存图形文件，这是个神器～目前支持的格式为 ps、
pdf、png、xpm。ps 和 pdf 是矢量格式，因而是绘图的首选格式，png 和 xpm 是位图图形格式，绘图
精度较差，因而不建议使用。考虑到图像不清晰，且 png 和 xpm 需要格外的库文件，在 SAC 101.6 发布的
二进制文件中不再支持 png 和 xpm。

    $ sac SEISMIC ANALYSIS CODE [02/01/2012 (Version
    Copyright 1995 Regents of the University of California

    SAC> fg seis
    SAC> p
    SAC> saveimg foo.ps save file foo.ps [PS]
    SAC> q

## pssac 绘制 ps 文件

`pssac` 利用 GMT 的 ps 库直接绘制 SAC 文件，`pssac` 的具体细节可以站内搜索 `pssac`。

## 小结

-   Xwindows 窗口最快最省事，截图的话平时看看还行，见不了大世面；
-   sgf 转换有点麻烦，生成的 ps 文件线条看上去有点模糊，偶尔会出现 bug，ps 文件上多出了额外的线条；
-   saveimg 是后起之秀，建议使用；
-   pssac 功能强大，在需要设计复杂图形时有用，当然用起来需要花点时间学。
