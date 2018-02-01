---
title: 安装 evt2sac
date: 2015-07-31
author: SeisMan
categories:
  - 地震学软件
tags:
  - SAC
  - 格式转换
  - 软件
slug: install-evt2sac
---

`evt2sac` 用于将 NEIC 的 EVT 格式的数据转换为 SAC 格式。

主页： <https://seiscode.iris.washington.edu/projects/evt2sac>

<!--more-->

`evt2sac` 最近一次更新是 1993 年，20 多年前的代码编译起来还是有些困难的，因而
一点一点介绍如何修改代码就太麻烦了，本文直接给出我修改后可编译的版本。

修改后的代码下载：[evt2sac.tar.bz2](http://7j1zxm.com1.z0.glb.clouddn.com/downloads/evt2sac.tar.bz2)

对官方代码的修改列举如下：

1.  修改并简化 Makefile，使用 gcc 和 gfortran 编译器
2.  删除了不需要的文件
3.  `evt2sac.c` 、 `evt_subs.c` 、 `ndt_subs.c` 中 include 了 `stdlib.h`、 `string.h` 等头文件
4.  `fglue2.F` 中，subroutine 中的 include 语句需要放在变量定义之前
5.  修复了 `fprintf` 的语法错误
6.  `distaz_` 改为 `distaz` ，请删除了前两个参数中的 `&` 符号。主要是因为 SAC 的源码已经从 Fortran 变成了 C。

修改后的版本可以直接编译（可能需要修改 Makefile 中的 `SACLIB` 变量）。但是否能够正常使用，尚不确定。
