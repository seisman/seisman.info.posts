---
title: SAC 二进制文件读取模块 sacio_Fortran
date: 2017-07-13
author: 王亮
categories: SAC
tags: [Fortran, SAC技巧]
---

sacio_Fortran 是一个用 Fortran 90写的模块，将其加入自己的程序中，即可实现 SAC 二进制文件的读写。
<!--more-->

## 如何获取

http://wangliang1989.github.io/sacio_Fortran/

## 文件列表

下载后，有如下文件:

1. `sacio.f90`: sacio模块的源代码 (这个文件就是你需要加入你自己的程序的全部!)
2. 例子程序文件: `test/test_sacio_*.f90` 如何使用sacio模块内的子程序的示例
3. `Makefile`: Makefile 文件
4. `README.md`: 说明文件
5. `.log.md`: 日志文件(中文，其他文件都是英文)
6. 例子数据: `test/testin.sac`: 用于试验的 SAC 二进制文件

所有文件都是 Unicode 字符，并用Linux/Unix换行符，Windows 记事本用户打开文件会出现中文字符乱码或者换行不正常。

## 如何编译与链接

以 gfortran 为例：

~~~bash
$ gfortran -c sacio.f90
$ gfortran -c your_program.f90
$ gfortran your_program.o sacio.o -o your_program
~~~

## 各个子程序的使用

模块中包含了 6 个子程序(subroutine):

1. `sacio_readhead`: 仅读取SAC文件头段
2. `sacio_readsac`: 读取SAC文件
3. `sacio_writesac`: 写SAC文件
4. `sacio_readsac_cut`: 带 cut 选项的读取SAC文件
5. `sacio_nullhead`: 修改 SAC 文件头段变量为 undef
6. `sacio_newhead`: 生成一个空数据的 SAC 头段

要使用哪个子程序，按照Fortran 90一般的方式即可调用。至于如何调用，请参考对应的例子程序文件，没有比例子更好的讲解。

## 协议和其他

sacio_Fortran 是[我](https://wangliang1989.github.io/)和 Seisman 在 2015 年 9 月一起写的，当时就在网上公开了。今借 SeisMan 这块宝地写一个简短的介绍，希望这个程序能被更多的人使用。本程序目前是按照 [Apache 开源协议](http://www.apache.org/licenses/LICENSE-2.0.html)发布的。如果你只是使用，或者为了适应自己的需要修改，只要不涉及再分发，你不需要太在意协议的问题，但是当要将这个程序给别人时，或者修改后给别人时，你应该注意遵循协议的内容。无论你如何使用本程序，我们都不寻求任何回报，当然也不对任何可能造成的损失负责。如果你发现程序有问题，欢迎告诉我们。如果你贡献大，我们会把你列为作者(贡献大不大完全由我们来确定)。

## 修订历史

-   2017-07-13：王亮 原稿；
