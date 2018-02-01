---
title: 使用 EPEL 和 RPMforge 源安装 netcdf 时的冲突
author: SeisMan
date: 2014-03-03
categories:
  - Linux
tags:
  - CentOS
  - GMT
slug: conflict-between-epel-and-rpmforge
---

新版本的 GMT 的编译与运行要求 netCDF 的版本大于 4，且支持 netCDF4/HDF5。即如果想要手动编译 netCDF4 以上的版本，则同时需要编译 hdf5，而 hdf5 又依赖于 zlib 和 szlib 等等包，所以手动编译 netcdf 相当不合算。

大多数发行版中应该都有 netcdf4，所以不会出现太多的问题。

CentOS 官方源中没有 netcdf，因而需要使用第三方源，直接将别人已经编译好的文件拿过来使用。其中最常用的就是 EPEL 和 RPMforge。而恰好二者都包含了 netcdf、netcdf-devel、hdf5、hdf5-devel 包。由此引发了一些冲突。

<!--more-->

EPEL 中的 netcdf 版本为 4.1.1，其编译过程中依赖于 hdf5，因而当通过

    sudo yum install netcdf netcdf-devel

安装 netcdf 时，hdf5 以及 hdf5-devel 会由于依赖关系而被自动安装。

而 RPMforge 中 netcdf 的版本为 4.1.2，其编译过程中没有加入 hdf5 依赖，所以当

    sudo yum install netcdf netcdf-devel

时，hdf5 由于没有被依赖，所以不会被安装。

所以通过 EPEL 安装的 netcdf4 是可以被 GMT 使用的，而通过 RPMforge 安装的 netcdf4 是不能被使用的。而由于 RPMforge 的 netcdf 版本比 EPEL 的版本高，因而两个源共存时，RPMforge 的 netcdf 会被优先安装。（利用优先级插件设置之后好像没有用）

因而当遇到如下报错时:

    -- Looking for nc_def_var_deflate
    -- Looking for nc_def_var_deflate - not found
    CMake Error at cmake/modules/FindNETCDF.cmake:127 (message):
    Library found but netCDF-4/HDF5 format unsupported. Do not configure
    netCDF-4 with --disable-netcdf-4.
    Call Stack (most recent call first):
    src/CMakeLists.txt:39 (find_package)

需要确认 netcdf 究竟来自于 EPEL 还是 RPMforge。

用来检查的命令如下:

1.  查看当前系统中所使用的源 :

        yum repolist

2.  查看优先的 netcdf-devel 的版本以及来自哪个源 :

        yum info netcdf-devel

3.  查看 netcdf-devel 包依赖于哪些其他包 :

        yum deplist netcdf-devel

4.  查看当前系统中已安装的相关包 :

        rpm -qa | grep netcdf
        rpm -qa | grep hdf5

通过以上四个方法确认 netcdf 以及 hdf5 均来自于 EPEL，则没问题。

如果确认无误，依然出现如上报错，一个可能的原因是自己曾经尝试编译过 netcdf，并禁用了 hdf5 相关功能，而删除 netcdf 时没有删除干净，或者怎样。

如果真的没招了，可以查看编译 GMT 时的 `build/CMakeFiles` 目录下的 `CMakeError.log` 和 `CMakeOutput.log` 这两个日志文件，寻找与 netcdf 相关的部分。

其实质是找到 netcdf 的动态链接库，并通过如下 C 代码

``` C
#include <netcdf.h>

int main(int argc, char** argv)
{
    (void)argv;
    #ifndef nc_def_var_deflate
        return ((int*)(&nc_def_var_deflate))[argc];
    #else
        (void)argc;
        return 0;
    #endif
}
```

检测动态链接库中是否定义了函数 `nc_def_var_deflate` 。
