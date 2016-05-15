---
title: fk3.2 编译
date: 2013-09-01
updated: 2014-10-22
author: SeisMan
categories: 地震学软件
tags: [理论地震图, 编译, C, Fortran, Perl]
---

fk 是 Prof. Lupei Zhu 写的一个计算水平分层介质中理论地震图的小程序。

<!--more-->

## 下载

下载地址： [fk3.2.tar](http://www.eas.slu.edu/People/LZhu/downloads/fk3.2.tar)

## 解压

    $ tar -xvf fk3.2.tar

## 修改 Makefile

fk3.2 自带的 Makefile 有一堆问题，下面会说明遇到的问题以及如何解决。

这里先提供我修改好的 Makefile，读者可以直接下载这个文件，然后重命名为 `Makefile` ，并覆盖 fk 自带的 Makefile 即可。

修改版 Makefile 下载地址： [Makefile.fk.3.2](http://seisman.qiniudn.com/downloads/Makefile.fk.3.2)

### 修改 Fortran 编译器选项

程序的大部分代码是用 Fortran 77 的语法写的，由于 Fortran 77 规定每行超过第 72 列的字符会被忽略，
而代码中部分行超过了 72 列。因而要修改编译器选项，加入语句如下:

    FC=gfortran -ffixed-line-length-none

其中 `-ffixed-line-length-none` 表示不限制每一行的长度。

### SAC 子程序支持

部分代码中调用了 SAC 提供的子程序，如果已经安装了 SAC，那么可以将 `CFLAGS` 和 `SACLIB` 两行去除
注释，并根据自己的 SAC 安装路径做修改。

### sachd 链接数学库

按照上面所说进行修改，make 之后出现如下错误：

    cc -O    -o sachd sachd.o sacio.o
    sacio.o: In function `read_sac2':
    sacio.c:(.text+0x831): undefined reference to `rintf'
    sacio.c:(.text+0x8e0): undefined reference to `rintf'
    collect2: ld 返回 1
    make: *** [sachd] 错误 1

这是由于 sachd 在链接时没有链接数学库 `-lm` ，将

    sachd: sachd.o sacio.o
        ${LINK.c} -o $@ $^

改成:

    sachd: sachd.o sacio.o
        ${LINK.c} -o $@ $^ -lm

即可。

## 编译

    $ make

## 安装

为了使用的方便，建议将编译生成的二进制文件 `fk` 、 `st_fk` 、 `syn` 和 `trav` 、 `sachd`
以及脚本文件 `fk.pl` 复制到 `$HOME/bin` 或者其他可搜索的路径中即可。

-   `fk` ：程序的核心，负责计算格林函数；
-   `st_fk` ：与 fk 相似，负责计算静态位移；
-   `trav` ：计算到时；
-   `syn` ：利用 `fk` 计算出的格林函数合成最终地震图；
-   `sachd` ：用于修改 SAC 文件的头段信息；
-   `fk.pl` ： `fk` 的 Perl 封装，相对 `fk` 来说更易于使用，其调用了 `fk`
    、 `trav` 和 `sachd` ；

## 修订历史

-   2013-09-01：初稿；
-   2013-10-07：关于 fk 3.2 的一点修改；
-   2014-10-22：更新至 fk 3.2；
