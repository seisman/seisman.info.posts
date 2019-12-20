---
title: fk3.3 编译
date: 2013-09-01
lastmod: 2019-12-19
author: SeisMan
categories:
  - 地震学软件
tags:
  - 理论地震图
  - 编译
  - C
  - Fortran
  - Perl
slug: fk-install
---

fk 是 [Prof. Lupei Zhu](http://www.eas.slu.edu/People/LZhu/home.html) 写的一个计算水平分层介质中理论地震图的小程序。

<!--more-->

## 下载

下载地址： [fk3.3.tar](http://www.eas.slu.edu/People/LZhu/downloads/fk3.3.tar)

## 解压

    $ tar -xvf fk3.3.tar

## 修改 Makefile

fk3.3 自带的 Makefile 无法直接使用，需要做一些小修改。

下面提供了修改后的 Makefile，读者可以直接下载这个文件，然后重命名为 `Makefile`，并覆盖 fk 自带的 Makefile。

修改版 Makefile 下载地址： [Makefile.fk.3.3](/downloads/Makefile.fk.3.3)

修改版 Makefile 相对于原版 Makefile 做了如下修改:

1. 添加 `FC=gfortran` 指定 gfortran 为默认的Fortran编译器
2. 向 FFLAGS 中加入了 `-ffixed-line-length-none` 使得 Fortran 一行可以超过72字符
3. 假定用户已正确安装SAC，将第二个 `CFLAGS` 和 `SACLIB` 前的注释符号 `#` 去掉，以使得 fk 可以利用 SAC 提供的滤波函数
4. 增加了 `fk2mt` 的编译指令

## 编译

    $ make

## 安装

为了使用的方便，建议将编译生成的二进制文件 `fk`、`st_fk`、`syn`、`trav`、`sachd` 和 `fk2mt`
以及脚本文件 `fk.pl` 复制到 `$HOME/bin` 或者其他可搜索的路径中即可。

-   `fk`：程序的核心，负责计算格林函数；
-   `st_fk`：与 fk 相似，负责计算静态位移；
-   `trav`：计算到时；
-   `syn`：利用 `fk` 计算出的格林函数合成最终地震图；
-   `sachd`：用于修改 SAC 文件的头段信息；
-   `fk2mt`：将FK生成的格林函数转换为另一种Moment Tensor格式的格林函数，即Moment Tensor的每个分量分别对应3个格林函数；
-   `fk.pl`：`fk` 的 Perl 封装，相对 `fk` 来说更易于使用，其调用了 `fk`、`trav` 和 `sachd`；

## 修订历史

-   2013-09-01：初稿；
-   2013-10-07：关于 fk 3.2 的一点修改；
-   2014-10-22：更新至 fk 3.2；
-   2019-12-19：更新至 fk 3.3；
