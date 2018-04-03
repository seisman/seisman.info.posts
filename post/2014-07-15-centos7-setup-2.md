---
title: CentOS 7 配置指南 — 开发环境篇
slug: centos7-setup-2
---
为了搭建一个稳定的系统，尽量避免因为各种瞎折腾而导致的系统问题，特订立了一些软件安装的原则。
具体参见《[CentOS7 下的软件安装方法与策略](/how-to-install-softwares-under-centos-7/)》。
## 基础开发环境

### GCC 系列

    sudo yum install gcc                     # C 编译器
    sudo yum install gcc-c++                 # C++ 编译器
    sudo yum install gcc-gfortran            # Fortran 编译器
    sudo yum install compat-gcc-44           # 兼容 gcc 4.4
    sudo yum install compat-gcc-44-c++       # 兼容 gcc-c++ 4.4
    sudo yum install compat-gcc-44-gfortran  # 兼容 gcc-fortran 4.4
    sudo yum install compat-libf2c-34        # g77 3.4.x 兼容库

### 软件开发辅助工具

    sudo yum install make
    sudo yum install gdb     # 代码调试器
    sudo yum install cmake   # Cmake
    sudo yum install git     # 版本控制


## 进阶开发环境

### Java 环境

Java 的一大特色在于跨平台，安装了 Java 运行环境，即可运行 Java 程序:

    sudo yum install java                        # java 运行环境

### Clang 系列

Clang 可以认为是 GCC 的替代品，可以用于编译 C、C++、Objective-C 和 Objective-C++。其提供了更友好的
报错信息，在有些方面比 GCC 更友好，同时其提供了一个代码静态分析器，可以用于分析代码中可能出现的 bug 和内存溢出问题。

    sudo yum install clang             # clang 编译器
    sudo yum install clang-analyzer    # clang 静态分析器

### Intel 系列

Intel 的大部分软件都是非开源且收费的，但同时部分软件也提供了 Linux 下的非商业免费版。
比如 icc、mkl 数学库以及代码性能分析工具等。

Intel 软件的申请以及安装参考《[Intel 非商业免费开发工具](/intel-non-commercial-software.html)》。

还有一点需要注意的是，Intel 也提供了并行相关的几个命令，比如 mpicc、mpirun。所以 openmpi、mpich
和 intel 三者，在并行时只能用其中一个。

### 并行计算

并行可以用 openmpi，也可以用 mpich，二者的功能可以认为是完全相同的。由于二者提供了几乎一样的命令，
所以二者可以同时安装，但是不可以同时处于使用状态。

#### openmpi

安装 openmpi:

    sudo yum install openmpi openmpi-devel

安装后，二进制文件位于 `/usr/lib64/openmpi/bin` 下，动态库文件位于 `/usr/lib64/openmpi/lib`
下，因而实际使用的话还需要额外的配置，在 `.bashrc` 中加入如下语句:

    export PATH=/usr/lib64/openmpi/bin/:${PATH}
    module load mpi/openmpi-x86_64

PS：要使用 `module` 命令需要先安装 `environment-modules` 包。

#### mpich

安装 mpich:

    sudo yum install mpich mpich-devel

安装后，二进制文件位于 `/usr/lib64/mpich/bin` 下，动态库文件位于 `/usr/lib64/mpich/lib` 下，
因而实际使用的话还需要额外的配置，在 `.bashrc` 中加入如下语句:

    export PATH=/usr/lib64/mpich/bin/:${PATH}
    module load mpi/mpich-x86_64
