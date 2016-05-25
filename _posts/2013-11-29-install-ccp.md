---
title: CCP1.0 编译
date: 2013-11-29
updated: 2016-03-12
author: SeisMan
categories: 地震学软件
tags: [接收函数, 编译]
---

Prof. Lupei Zhu 最近又在网上公开了两个程序包，CCP 和 CAP。

CCP，即 Common-Conversion-Point，用于共转换点地震数据的叠加，这个程序主要与
[hk1.3](/compilation-of-hk.html) 一起使用，用于接收函数的研究。

<!--more-->

安装方法以及一些修改与 hk1.3 类似：

## 下载与解压

``` bash
$ wget http://www.eas.slu.edu/People/LZhu/downloads/ccp1.0.tar
$ tar -xvf ccp1.0.tar
$ cd ccp
$ make clean
```

## 修改 Makefile

在 Makefile 中加入如下两行，定义变量 `GMT_INC` 和 `GMT_LIB` ：

``` makefile
GMT_INC = -I/opt/GMT/include
GMT_LIBS = -L/opt/GMT/lib -lgmt -lpsl -lnetcdf -lm -s
```

## 编译

    $ make

## BUG 及其解决办法

在按照 CCP 包里的说明文档执行程序 3Dslice 时，会出现如下信息及错误:

    interpolation order = 1
    GMT Warning: scale_factor should not be 0. Reset to 1.
    段错误 (核心已转储)

这个错误是由于 3Dslice 中调用 `GMT_write_grd` 导致的。具体原因尚不清楚，可能是
由于 GMT 不同版本之间该函数的定义有变化导致的。

整个程序的作用在于从一个 3D 的网格文件中提取一个切片，然后将该切片上的数据写到 2D 网格文件中，
调用 `GMT_write_grd` 的目的就是将 2D 的网格数据以 netCDF 格式写入到文件中。

因而，解决这个问题的思路有三个：

1.  读 GMT 源码，了解 `GMT_write_grd` 这个函数，找到可能出错的原因
2.  尝试安装稍老版本的 GMT4，比如 GMT 4.5.5，也许可以用
3.  在 3Dslice 源码的最后，删除对 `GMT_write_grd` 的调用，自己写代码，直接
    输出 XYZ 数据。然后在外部调用 `xyz2grd` 生成 netCDF 即可

推荐使用方法 3。当然，如果有人用方法 1 解决了问题，可以告诉我。
