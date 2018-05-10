---
title: Intel 非商业开发工具
date: 2013-09-10
lastmod: 2015-04-08
author: SeisMan
categories:
  - 编程
tags:
  - 安装
  - Intel
  - C
  - Fortran
slug: intel-non-commercial-software
---

Intel 的软件开发工具包括：C/C++ 编译器、Fortran 编译器、MKL 数学库、MPI 并行库等。

这一套开发工具价格很贵，但是 Intel 为科研工作者、学生、教育者以及开源贡献者提供了免费的版本。

[主页](https://software.intel.com/en-us/qualify-for-free-software)
[学生申请](https://software.intel.com/en-us/qualify-for-free-software/student)

对于学生，intel 提供了全套开发工具一年的使用权。Linux 和 Windows 用户可以申请 Intel Parallel Studio XE
的 Cluster 版本（包含全部工具）；对于 OS X 用户，则只能申请 Composer 版本（只包含 C 编译器、Fortran 编译器以及 MKL 数学库）。

对于 Linux 用户，进入学生申请页，点击 “Linux” 即可申请。申请时需要填写 edu 邮箱，再填写其他一些必要的信息即可。

若学校的 edu 邮箱不在 Intel 的邮箱列表中，则无法申请，可以发邮箱给 Intel，申请把学校的邮箱加入到邮箱列表中。
申请完成后，Intel 会向注册邮箱内发送 license 以及下载链接。License 有效期一年，一年后需要重新申请。

## 依赖关系

安装之前需要先安装如下包:

    sudo yum install kernel-devel gcc gcc-c++ gcc-gfortran pangox-compat-devel libunwind-devel

除此之外，64 位系统还需要安装一些 32 位的库文件:

    sudo yum install glibc.i686 glibc-devel.i686 libgcc.i686 libstdc++.i686

## 解压

``` bash
$ tar -xvf parallel_studio_xe_2015_update3.tgz
$ cd parallel_studio_xe_2015_update3
$ su
# ./install_GUI.sh   # 图形化界面，也可以直接执行./install.sh
```

## 安装过程

1.  检测依赖性

    检测依赖的过程中，会有 “Unsupported OS” 的错误，除非系统非常老，否则该错误都可以忽略。
    如果出现其他错误，需要 “detailed info about issues” 逐一排查。

2.  License
3.  激活

    点击 “Use serial number to active and install product”，并到邮箱中找到序列号。
    序列号的格式为 `XXXX-XXXXXXXX` 。

4.  安装选项

    可以直接使用默认值，也可以自定义指定安装路径以及要安装哪些组件。

## 修改环境变量

对于 bash 用户，在 `~/.bashrc` 中加入如下语句

``` bash
# Intel
source /opt/intel/vtune_amplifier_xe_2015/amplxe-vars.sh quiet
source /opt/intel/inspector_xe_2015/inspxe-vars.sh quiet
source /opt/intel/advisor_xe_2015/advixe-vars.sh quiet
source /opt/intel/bin/compilervars.sh intel64
```

然后执行 `source .bashrc` 使环境变量生效。对于 csh 用户，类似。

说明：2015\_update3 版本，直接 `source` 会报错:

    /opt/intel/composer_xe_2015/ipp/bin/ippvars.sh:19: = not found

这似乎是一个 bug，把 `/opt/intel/composer_xe_2015/ipp/bin/ippvars.sh` 第 19 行的 `==` 改成 `=` 即可。

## 修订历史

-   2013-09-10：初稿 for CentOS 6.5；
-   2014-07-15：加入了依赖包 for CentOS 7.0；
-   2015-04-08：Intel 非商业软件在停止一段时间后重新接受申请；
-   2015-07-17：学生可申请完整版开发工具（含 Fortran）；
