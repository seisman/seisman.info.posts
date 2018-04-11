---
title: CentOS 7 配置指南 — 开发环境篇
author: SeisMan
date: 2014-07-15
lastmod: 2018-04-11
slug: centos7-setup-2
---

## C/C++编译器

### GCC 系列

GCC 系列提供的 C/C++ 编译器是 Linux 下最常用的 C/C++ 编译器 `gcc` 和 `g++`:

    sudo yum install gcc                     # C 编译器
    sudo yum install gcc-c++                 # C++ 编译器
    sudo yum install compat-gcc-44           # 兼容 gcc 4.4
    sudo yum install compat-gcc-44-c++       # 兼容 gcc-c++ 4.4

### Clang 系列

[Clang](https://clang.llvm.org/) 是 GCC 的一大竞争者，其提供了 C、C++、
Objective-C 和 Objective-C++ 的编译器，名为 `clang`。

其具有如下优点：

1. 更友好的报错信息，方便在报错时尽快找到错误
2. 提供了一个代码静态分析器，可以用于分析代码中可能出现的 bug 和内存溢出问题

安装：

    sudo yum install clang             # clang 编译器
    sudo yum install clang-analyzer    # clang 静态分析器

### Intel 系列

Intel 公司开发了一套开发工具，其是不开源且收费的，但部分软件有 Linux 下的
非商业免费版，其中包含了 C/C++ 编译器 `icc`。

Intel 软件的申请以及安装参考 [Intel 非商业免费开发工具](/intel-non-commercial-software/) 一文。

优点：

1. 编译速度慢，但执行速度更快
2. 提供了 MKL 数学库，可以实现很多数学常用运算
3. 提供了代码性能分析工具等

## Fortran编译器

### GCC 系列

GCC 提供了 Fortran 编译器 `gfortran`:

    sudo yum install gcc-gfortran            # Fortran 编译器
    sudo yum install compat-gcc-44-gfortran  # 兼容 gcc-fortran 4.4
    sudo yum install compat-libf2c-34        # g77 3.4.x 兼容库

CentOS 7 下不再有老的 Fortran 编译器 `f77`、`g77` 等。

### Intel 系列

Intel 提供的 Fotran 编译器 `ifort`，安装方式见上面的链接。

## Java 环境

Java 的一大特色在于跨平台，安装了 Java 运行环境，即可运行 Java 程序:

    sudo yum install java                        # java 运行环境

## 并行计算

并行可以用 openmpi，也可以用 mpich，二者的功能可以认为是完全相同的，
二者提供了几乎一样的命令，另外，intel 也提供了并行相关命令。
所以三者虽然可以同时安装，但不可以同时处于使用状态。

### openmpi

安装 openmpi:

    sudo yum install openmpi openmpi-devel

安装后，二进制文件位于 `/usr/lib64/openmpi/bin` 下，动态库文件位于
`/usr/lib64/openmpi/lib` 下，因而实际使用的话还需要额外的配置。

在 `.bashrc` 中加入如下语句:

    export PATH=/usr/lib64/openmpi/bin/:${PATH}
    module load mpi/openmpi-x86_64

### mpich

安装 mpich:

    sudo yum install mpich mpich-devel

安装后，二进制文件位于 `/usr/lib64/mpich/bin` 下，动态库文件位于
`/usr/lib64/mpich/lib` 下，因而实际使用的话还需要额外的配置。

在 `.bashrc` 中加入如下语句:

    export PATH=/usr/lib64/mpich/bin/:${PATH}
    module load mpi/mpich-x86_64

### Intel 系列

Intel 也提供了并行相关的几个命令，安装方式见上面的链接。

## 软件开发辅助工具

软件开发过程中常用的一些工具:

    sudo yum install make
    sudo yum install gdb     # 代码调试器
    sudo yum install cmake   # Cmake
    sudo yum install git     # 版本控制软件
