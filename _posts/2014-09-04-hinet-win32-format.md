---
title: Hi-net WIN32 格式
date: 2014-09-04
author: SeisMan
categories: 地震学基础
tags: [Hinet, 格式, 数据]
---

对于连续波形数据而言，从 Hi-net 下载的文件为 zip 压缩文件，其中包含了多个后缀为
`cnt` 的文件。每个 cnt 文件中包含了多台站多分量的一分钟的波形数据。

这些 cnt 文件即为 WIN32 格式。WIN32 格式是在 WIN 格式上修改得到的，而 WIN 格式是日本
某机构自行设计的一种数据格式，主要用于一套称为 “WIN System” 的软件中。

[WIN32 格式官方文档](http://www.hinet.bosai.go.jp/REGS/manual/dlDialogue.php?r=win32format&LANG=en)

WIN32 是个相当变态的格式，为了对数据大小进行压缩，win32在存储的过程中使用了差异压缩算法，以0.5、1、2、3、4个字节来保存数据，自己写程序去读数据时需要非常小心。


幸好，Hi-net 提供了 win32tools，可以实现一些基本的功能。
