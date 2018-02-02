---
title: 由矩张量计算双力偶断层参数
date: 2013-07-16
author: SeisMan
categories:
  - 地震学软件
tags:
  - 震源机制解
  - 断层
slug: moment-tensor-to-double-couple
---

Double Couple 由四个参数描述：Strike、Dip、Rake、Moment；Moment Tensor 由 9 个量描述，
由于对称性，减少到六个。

任意一个 double couple 都可以写成 moment tensor 的形式，但并非所有的 moment tensor
都可以写成 double couple 形式。double couple 只是 moment tensor 的一个子集而已。

若干月前，有人问到如何将 moment tensor 转换成 double couple，搜了一下，发现了
一个别人写的代码。做了一下排版，试了一个例子，结果是对的，没有再看细节。

代码分为三个部分：

-   ten2axe：将 moment tensor 转换成主轴坐标系；
-   axe2dc：将主轴坐标系下的结果转换为 double couple 解；
-   ten2dc.pl：我写的 perl 脚本，实现两个程序的衔接（作者给的是 shell 脚本）

原文链接： [链接已死](http://www.fcaglp.unlp.edu.ar/~esuarez/gmt/1998/0102.html)

代码下载： [ten2dc.tar.gz](http://seisman.qiniudn.com/downloads/ten2dc.tar.gz)

PS：没看过代码，不确定原理，不确定正确性。
