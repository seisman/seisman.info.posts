---
title: GMT 4.5.17 在 Linux 下的安装
date: 2013-11-07
author: SeisMan
lastmod: 2016-10-07
categories:
  - GMT
tags:
  - 安装
  - GMT
slug: install-gmt4-under-linux
---

## 说明

本文介绍如何在 Linux 下编译 GMT4 的最新版本：GMT 4.5.17。

很多 Linux 发行版的源中带有 GMT 软件包，但是版本一般较老，因而这里假定想要自己编译 GMT4 的读者，下载和编译的都是 GMT4 的最新版本，因而本文会随着 GMT4 新版本的发行而不断作出修改。

<!--more-->

## 下载

- 官方 ftp：<ftp://ftp.soest.hawaii.edu/gmt>
- 国内镜像：<http://mirrors.ustc.edu.cn/gmt/>


需要下载的包包括：

- [gmt-4.5.17-src.tar.bz2](http://mirrors.ustc.edu.cn/gmt/gmt-4.5.17-src.tar.bz2)
- [gshhg-gmt-2.3.7.tar.gz](http://mirrors.ustc.edu.cn/gmt/gshhg-gmt-2.3.7.tar.gz)

注：GMT 中的 `triangulate` 命令有两个不同的源码，其中一个遵循 GPL 协议，另一个不遵循 GPL 协议。GMT 的 src 包中包含了前者。若有特殊需求，需要使用后者源码的功能，可以下载 [gmt-4.5.17-non-gpl-src.tar.bz2](http://mirrors.ustc.edu.cn/gmt/gmt-4.5.17-non-gpl-src.tar.bz2) ，并将解压后的 triangulate 源码覆盖 `gmt-4.5.17-src.tar.bz2` 中的相应源码。

下载完成后，可以用 `md5sum` 检查压缩文件的 md5 值，以保证该文件是完整且未被篡改的:

    $  md5sum gmt-4.5.17-src.tar.bz2 gshhg-gmt-2.3.7.tar.gz
    1d6f9d927e5334e30407171e16d8831f  gmt-4.5.17-src.tar.bz2
    8ee2653f9daf84d49fefbf990bbfa1e7  gshhg-gmt-2.3.7.tar.gz

## 依赖关系

### 基础依赖包

编译 GMT 时需要一些开发工具（ `gcc` 、 `g++` 和 `make` ）以及底层的库文件 `libc.so` 和 `libm.so` 。

对于 Ubuntu/Debian:

    sudo apt-get update
    sudo apt-get install gcc g++ make libc6

对于 CentOS/RHEL/Fedora:

    sudo yum install gcc gcc-c++ make glibc

### netCDF 库

GMT4 主要依赖于 netCDF4，可以直接使用 Linux 发行版官方源中提供的 netCDF 包。除了 netCDF 之外，建议还安装 gdal 包。虽然 GMT 不依赖于 gdal，但 gdal 可以轻松地将其他数据格式转换为 GMT 可识别的格式。

对于 Ubuntu/Debian:

    sudo apt-get update
    sudo apt-get install libnetcdf-dev libgdal-dev python-gdal

备注： `libgdal-dev` 在某些版本的 Ubuntu 下叫 `libgdal1-dev`

对于 RHEL/CentOS/Fedora:

    sudo yum install netcdf netcdf-devel gdal gdal-devel gdal-python

注意：

1.  一定不要试图自己手动编译 netCDF。如果在阅读本文之前曾经手动编译过，一定要将原来手动编译生成的文件删除干净。通常可以使用 `locate netcdf` 找到 `/usr/local` 目录下的与 netCDF 相关的文件，直接删除即可。
2.  CentOS 和 RHEL 的官方源中没有 netCDF，需要首先添加 EPEL 源再安装 netCDF；Fedora 官方源中自带 netCDF；

### X 相关库

GMT4 中的 `xgridedit` 命令是一个很简易的带 GUI 的网格文件编辑器，其依赖于一堆图形界面相关库文件:

    libICE.so   libSM.so   libX11.so  libXaw.so
    libXext.so  libXmu.so  libXt.so

对于 Ubuntu/Debian:

    sudo apt-get update
    sudo apt-get install libxaw7-dev
    sudo apt-get install libice-dev libsm-dev libx11-dev
    sudo apt-get install libxext-dev libxmu-dev libxt-dev

对于 CentOS/RHEL/Fedora:

    sudo yum install libXaw-devel
    sudo yum install libICE-devel libSM-devel libX11-devel
    sudo yum install libXext-devel libXmu-devel libXt-devel

## 安装 GMT

### 编译 GMT 源码

``` bash
$ tar -xvf gmt-4.5.17-src.tar.bz2
$ cd gmt-4.5.17
$ ./configure --prefix=/opt/GMT-4.5.17
$ make
$ sudo make install-all       # 注意：这里是 install-all 不是 install
```

其中 `--prefix` 指定了 GMT 安装路径，你可以指定为其他路径，但要注意后面其他步骤要与这里的路径统一。

### 安装海岸线数据

``` bash
$ cd ../
$ tar -xvf gshhg-gmt-2.3.7.tar.gz
$ sudo mv gshhg-gmt-2.3.7 /opt/GMT-4.5.17/share/coast
```

### 修改环境变量

向 `~/.bashrc` 中加入 GMT4 的环境变量，并使环境变量生效：

``` bash
$ echo 'export GMT4HOME=/opt/GMT-4.5.17' >> ~/.bashrc
$ echo 'export PATH=${GMT4HOME}/bin:$PATH'>> ~/.bashrc
$ echo 'export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${GMT4HOME}/lib64'>> ~/.bashrc
$ exec $SHELL -l
```

说明：

-   第一个命令向 `~/.bashrc` 中添加环境变量 `GMT4HOME`
-   第二个命令修改 `~/.bashrc` ，将 GMT4 的 bin 目录加入到 `PATH` 中
-   第三个命令将 GMT4 的 lib 目录加入到动态链接库路径中，若为 32 位系统，则为 `lib` ；64 位系统则为 `lib64`
-   第四个命令是重新载入 bash，相当于 `source ~/.bashrc`

## 命令测试

在终端键入 `psxy -` ，若出现如下输出，则安装成功:

    $ psxy -
    psxy 4.5.17 [64-bit] - Plot lines, polygons, and symbols on maps

## 个人笔记

1.  查看 GMT 需要哪些动态链接库:

        $ cd /opt/GMT-4.5.17/bin
        $ readelf -d * | grep 'Shared library' | sort -u

2.  Ubuntu 下查找哪个软件包提供某个特定库文件： <http://packages.ubuntu.com/>
3.  CentOS 下查找哪个软件包提供某个特定库文件： `yum provides libICE.so.6`

## 修订历史

-   2013-11-07：针对 GMT 4.5.11 发布初稿
-   2014-03-02：针对 GMT 4.5.12 进行更新
-   2014-03-08：`make install`->`make install-all`
-   2014-07-10：更新 gshhg 为 2.3.1 版；GMT4 不依赖 `gdal`
-   2014-09-14：更新 gshhg 为 2.3.2 版
-   2014-09-26：Ubuntu 下 `libxaw-dev` 应为 `libxaw7-dev`
-   2014-10-14：修正了若干细节
-   2014-11-04：修改环境变量 `LD_LIBRARY_PATH`
-   2015-01-01：更新至 GMT 4.5.13
-   2015-09-06：推荐安装 GDAL 的 Python 绑定（内含 `gdal_merge.py` ）
-   2015-09-18：下载后检查压缩文件的 md5 值
-   2015-10-11：重新整理了软件的依赖关系
-   2015-11-01：更新至 GMT 4.5.14
-   2016-10-07：更新至 GMT 4.5.15 和 GSHHG 2.3.6
-   2018-01-02：更新至 GMT 4.5.17 和 GSHHG 2.3.7
