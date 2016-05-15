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

WIN32 格式是很线性的，如果需要的话很容易自己写程序实现 win32 格式数据的合并、转换的。Hi-net 提供了 win32tools，可以实现一些基本的功能。
