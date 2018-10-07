---
title: rdseed 的安装
date: 2014-10-07
author: SeisMan
categories:
  - 地震学软件
tags:
  - SAC
  - 格式转换
slug: rdseed-install
---

rdseed 用于将 SEED 格式的数据转换为 SAC 格式。

<!--more-->

## 下载

到这个地址找到最新版本的rdseed： <http://ds.iris.edu/pub/programs/>。
目前最新的是 `rdseedv5.3.1.tar.gz` 。

## 解压

    $ tar -zxvf rdseedv5.3.1.tar.gz
    $ cd rdseedv5.3.1

## 安装

rdseed 提供了源代码，也提供了在不同平台下编译好的二进制文件。

-   如果是 Linux 64 位系统，则使用 `rdseed.rh6.linux_64` ；
-   如果是 Mac 64 位系统，则使用 `rdseed.mac.x86_64` ；
-   如果是运行在 Sun/Sparc 平台上的 Solaris，则使用 `rdseed.solaris.sparc_64` ；
-   如果是运行在 Sun/Intel 平台上的 Solaris，则使用 `rdseed.solaris.x86_64`；
-   如果是在 32 位 Windows 7 下运行 Cygwin，则使用 `rdseed.windows.cygwin_32.exe` ；

以 64 位 Linux 为例，应选择二进制文件 `rdseed.rh6.linux_64`，直接执行:

    $ ./rdseed.rh6.linux_64

若输出如下:

    <<IRIS SEED Reader, Release 5.3.1>>
    Input  File (/dev/nrst0) or 'Quit' to Exit:

则表示该二进制文件在当前系统可以直接使用，将其重命名，并放置到 PATH 中即可:

    mv rdseed.rh6.linux_64 ~/bin/rdseed

若你的 Linux 系统为 32 位，或者其他一些特殊的原因，该二进制可能无法执行，则需要自己手动编译。

## 编译

若二进制文件可以直接使用，则可以忽略这一步。

1.  `make clean`
2.  修改 Makefile

    Makefile 中默认的 CFLAGS 为 `-O -m64 -g`，若为 32 位系统，则应设置 CFLAGS 的值 `-O -m32 -g` 。

3.  `make`
4.  此时生成了可执行文件 `rdseed` ，将其复制到 PATH 中即可:

        mv rdseed ~/bin/

注意：5.3.1 版本目前存在 bug，使用较新的 gcc 编译器虽然可以编译通过，但无法
正确解压 SEED 数据，因而不建议自己手动编译。

CentOS7 下，gcc 编译器的版本为 4.8.3，编译通过，但无法解压数据。

如果一定需要手动编译的话，可以将 Makefile 以及各子目录下的 makefile 中的 CC 设置成 icc，
即使用 Intel C 编译器。

## Jrdseed

rdseed 还有一个 Java 版本，即 [Jrdseed](http://www.iris.edu/forms/jrdseed_request.htm)。

由于是 Java 写的，所以具有很好的跨平台特性，直接下载解压即可使用。

执行方法为:

    java -jar JrdseedVer0.10.1.jar

用法与 rdseed 类似。
