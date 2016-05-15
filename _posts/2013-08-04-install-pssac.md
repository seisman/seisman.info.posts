---
title: 安装 pssac
date: 2013-08-04
updated: 2015-07-16
author: SeisMan
categories: 地震学软件
tags: [pssac, 安装, GMT]
---

`pssac` 是 Prof. Lupei Zhu 根据 GMT 的 `psxy` 命令修改得到，用于绘制 SAC 格式的波形数据的
一个小程序。

该程序调用了 GMT 的绘图库，因而安装该程序之前需要首先安装 GMT4。需要注意，该程序不支持 GMT5。

<!--more-->

## 下载

``` bash
# 下载基于 GMT4.0 的 pssac 包
$ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.tar
$ tar -xvf pssac.tar      # 解压

# 下载基于 GMT4.5 的 pssac 源码
$ wget http://www.eas.slu.edu/People/LZhu/downloads/pssac.c

$ mv pssac.c pssac/       # 用基于 GMT4.5 的 pssac.c 替换基于 GMT 4.0 的 pssac.c
$ cd pssac
```

## 修改 Makefile

源码中的 Makefile 有些问题，需要进一步修改。修改之后的 Makefile 内容如下：

``` bash
GMTHOME=/opt/GMT-4.5.13
GMT_INC=-I${GMTHOME}/include
GMT_LIBS=-L${GMTHOME}/lib -lgmt -lpsl -lgmtps -lnetcdf -lm

CFLAGS = -O ${GMT_INC}

pssac: pssac.o sacio.o
     $(LINK.c) -o $@ $@.o sacio.o $(GMT_LIBS)

clean:
     rm -f pssac *.o
```

-   `GMTHOME` 是当前系统中 GMT4 的安装路径，需要根据自己的情况修改
-   `GMT_INC` 指定了 GMT 的头文件的位置
-   `GMT_LIBS` 指定了编译过程中所需要的库文件
-   `-L` 指定了在编译过程中要在哪些路径下寻找库文件

通常情况下，只需要根据自己的情况修改 `GMTHOME` 即可。

如果出现 `-lnetcdf` 找不到的情况，可能的原因是 netCDF 不是通过系统自带的
软件包管理器安装而是手动编译的，此时需要在 `GMT_LIBS` 中加上 netCDF 所对应的
路径，比如:

    GMT_LIBS=-L${GMTHOME}/lib -L/path/to/netcdf/lib -lgmt -lpsl -lgmtps -lnetcdf -lm

当然也有可能某些发行版下不是 `lib` 目录，而是 `lib64` 目录。

## 编译

编译过程就是简单的 make，正常情况下的输出如下：

``` bash
$ make
cc -O -I/opt/GMT-4.5.13/include   -c -o pssac.o pssac.c
cc -O -I/opt/GMT-4.5.13/include   -c -o sacio.o sacio.c
cc -O -I/opt/GMT-4.5.13/include    -o pssac pssac.o sacio.o -L/opt/GMT-4.5.13/lib -lgmt -lpsl -lgmtps -lnetcdf -lm
```

编译会生成可执行文件 `pssac` ，将该可执行文件复制到 `PATH` 中即可，比如
`/usr/local/bin` 、 `/opt/GMT-4.5.13/bin` 或 `${HOME}/bin` 。

## 执行

终端直接执行 `pssac` 就会出现命名的语法说明。

## 修订历史

-   2013-04-17：初稿；
-   2013-04-19：加入了对旧版本 `pssac.c` 的讨论；
-   2014-06-24：GMT4 的最近几个版本，都不再建议自己安装 netcdf3 了，最好还是自己利用系统自带的
    软件包管理器安装 netcdf4。在这种情况下，netcdf 会被安装到系统默认路径中，因而 Makefile 中不需要再指明 netcdf 的安装路径；
-   2014-07-16：在某些系统下，`GMT_LIBS` 需要加上 `-lm` ；
-   2015-07-16：整理，并删除对旧版本 `pssac.c` 的说明；
