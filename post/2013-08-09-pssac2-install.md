---
title: pssac2 的安装
date: 2013-08-09
lastmod: 2015-07-17
author: SeisMan
categories:
  - 地震学软件
tags:
  - pssac2
  - 编译
slug: pssac2-install
---

`pssac2` 是由 Brian Savage 基于 Lupei Zhu 的 `pssac` 修改得到的，其继承了 `pssac`
的优质特性，同时在很多方面又有了进一步的提高。

`pssac2` 目前有两个版本，一个支持 GMT4，一个支持 GMT5。

<!--more-->

## GMT4 版

GMT4 版本的 `pssac2` 没有官方下载地址，目前只在 [specfem3d](https://github.com/geodynamics/specfem3d/tree/master/utils/ADJOINT_TOMOGRAPHY_TOOLS/measure_adj/UTIL/pssac2) 程序包中找到有
`pssac2` 的源码。

由于 specfem3d 中的 pssac2 下载起来有些麻烦，这里我整理了一个版本供读者下载：
[pssac2_GMT4.tar.gz](/downloads/pssac2_GMT4.tar.gz)

本文提供的版本在 specfem3d 给的源码的基础上做了如下操作与修改：

1.  将源码压缩成 `tar.gz` 格式，方便下载；
2.  `configure` 文件的第 2467 行原为:

        LDFLAGS+="-L${withval}/lib "

    修改为:

        LDFLAGS+="-L${withval}/lib -L${withval}/lib64"

    修改后的版本同时考虑了 GMT 库文件在 `lib` 和 `lib64` 的两种可能性。

安装方法如下：

``` bash
$ tar -xvf pssac2_GMT4.tar.gz
$ cd pssac2_GMT4
$ ./configure --with-gmt=/opt/GMT-4.5.13
$ make
```

如果成功执行，则会在当前目录生成可执行文件 `pssac2` ，即可直接使用。

某些版本可能会出现如下错误:

    pssac2.c:27: error: conflicting types for 'BOOLEAN'
    /opt/GMT4/include/gmt.h:278: note: previous declaration of 'BOOLEAN' was here

出错的原因是 `BOOLEAN` 类型在两个地方的定义有冲突，把 `pssac2.c` 中第 27 行的
`typedef GMT_LONG BOOLEAN` 删除即可。

## GMT5 版

GMT5 版本的 pssac2 似乎有不少 bug，谨慎使用。

``` bash
$ git clone https://github.com/savage13/pssac2.git
$ ./configure --with-gmt=/opt/GMT-5.1.2
$ make
```

## 修订历史

-   2013-08-09：初稿；
-   2015-01-03：添加了 pssac2 的 GMT5 版本并简化了 GMT4 版本的说明；
-   2015-04-01：更新了 pssac2 的 GMT4 版本的地址；
-   2015-07-17：为 GMT4 版本的 pssac2 提供了新的下载链接；
